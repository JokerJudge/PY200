"""Задание:

Дан каталог книг. Реализуйте библиотеку для хранения данных книг и поиску по каталогу. Каталог должен поддерживать
 возможность добавления и удаления книг, редактирования информации о книге, а также обладать персистентностью
(т.е. сохранять библиотеку в внешнем файле и подгружать обратно). Также необходимо оформить точку входа и поддерживать
поиск по различным параметрам.

"""
import re
import json
from weakref import ref


class Book:
    def __init__(self, prev=None, next_=None, data = None):
        if prev is not None and not isinstance(prev, type(self)):
            raise TypeError('prev must be Node or None')

        if next_ is not None and not isinstance(next_, type(self)):
            raise TypeError('next_node must be Node or None')

        self.prev = ref(prev) if prev is not None else None
        self.next_ = next_
        self.data = data

    def set_next(self, next_):
        if next_ is not None and not isinstance(next_, type(self)):
            raise TypeError("next_ must be Node or None")
        self.next_ = next_

    def set_prev(self, prev):
        if prev is not None and not isinstance(prev, type(self)):
            raise TypeError("prev must be Node or None")
        self.prev = ref(prev)

    def get_value(self):
        return self.data

    def set_value(self, data):
        self.data = data

    def __str__(self):
        return f"Книга: {self.data}"

    @classmethod
    def check(cls, pattern, to_check):
        """
        Функция для проверки на корректность введенных пользователем значений

        :param pattern: "word" - для проверки слов/названий, "page" - для проверки страниц, "year" - для проверки даты публикации
        :param to_check: значение, которое будет проверяться
        :return: если значение подходит под регулярное выражение - return True, если нет - False
        """
        if pattern == "word":
            pattern = r"^\b[\w\(\)\-@',\.\:\?\!]+(\s?[\w\(\)\-@',\.\:\?\!]+)*"  # проверка на отсутствие недопустимых символов в слове
        elif pattern == "page":
            pattern = r'^\b\d{1,7}'  # проверка на корректность ввода страниц
        elif pattern == "year":
            pattern = r'^\b(1[4-9][0-9]{2})|(20[0-2][0-9])'  # проверка на корректность ввода года
        temp = re.fullmatch(pattern, to_check)
        if temp is None:  # если введенное пользователем является некорректным
            return False
        else:
            return True

class Library:
    def __init__(self, books=None):
        if books is None:
            self.head = None
            self.tail = None
        elif isinstance(books, Book):
            self.head = books # указываем, что это тот же нод
            self.tail = books # указываем, что это тот же нод
        elif isinstance(books, list):
            if len(books) == 0:
                self.head = None
                self.tail = None
            elif len(books) == 1:
                if not isinstance(books[0], Book):
                    raise TypeError("Передаваться должен Book или список из Book")
                self.head = books[0]
                self.tail = books[0]
            elif len(books) > 1:
                for i in books:
                    if not isinstance(i, Book):
                        raise TypeError("Передаваться должен Book или список из Book")
                self.head = books[0]
                self.tail = books[-1]
                self.linked_books(books) # связываем Node в порядке подачи в списке

        else:
            raise TypeError("Передаваться должен Book или список из Book")

    def __len__(self): # считаем количество Book в Library
        if self.head is None:
            return 0
        elif self.head == self.tail:
            return 1
        else:
            current_book = self.head
            current_book = current_book.next_
            index = 1 # счетчик
            while current_book != self.head:
                index += 1
                current_book = current_book.next_
            return index

    def linked_books(self, books):
        # установили ссылки для первого нода
        books[0].set_prev(books[-1])
        books[0].set_next(books[1])


        for i in range(1, len(books) - 1): # установили ссылки для остальных, кроме последнего
            books[i].set_prev(books[i - 1])
            books[i].set_next(books[i + 1])

        books[-1].set_prev(books[-2]) # установили ссылки для последнего нода
        books[-1].set_next(books[0])

    def __str__(self):
        l = []
        if self.head is None:
            return f"{l}"
        current_book = self.head
        for i in range(len(self)):
            l.append(current_book.data)
            current_book = current_book.next_

        print("===========================")
        print("============================" * 6)
        print("|", end=" ")
        print("Title", end=" " * 60)
        print("|", end=" ")
        print("Author", end=" " * 29)
        print("|", end=" ")
        print("Genre", end=" " * 15)
        print("|", end=" ")
        print("Pages", end=" " * 5)
        print("|", end=" ")
        print("Format", end=" " * 9)
        print("|", end=" ")
        print("Publish year", end=" " * 3)
        print("|", end=" ")
        print()
        print("============================" * 6)

        index = 0
        while index <= len(l) - 1:
            print("|", end=" ")
            print(l[index]["Title"], end=" " * (65 - len(l[index]["Title"])))
            print("|", end=" ")
            print(l[index]["Author"], end=" " * (35 - len(l[index]["Author"])))
            print("|", end=" ")
            print(l[index]["Genre"], end=" " * (20 - len(l[index]["Genre"])))
            print("|", end=" ")
            print(l[index]["Pages"], end=" " * (10 - len(str(l[index]["Pages"]))))
            print("|", end=" ")
            print(l[index]["Format"], end=" " * (15 - len(l[index]["Format"])))
            print("|", end=" ")
            print(l[index]["Publish year"], end=" " * (14 - len(str(l[index]["Pages"]))))
            print("|", end=" ")
            print()
            print("----------------------------" * 6)
            index += 1

        return "==========================="

    def add(self, d=None):
        """
        Метод добавления новой книги в каталог. Проверка на корректность введенных данных (возможно, стоит выделить в
        иную функцию)
        :param каталог, с которым работаем в формате [{"Title":"value_1", "Author":"value_2",
         "Genre":"value_3", "Pages":int, "Format":"value_4", "Publish year":int}, {...}]
        :param d - словарь значений для конкретной книги
        :return: Измененный catalog с добавлением новой книги
        """
        book = Book()

        if not isinstance(book, Book):
            raise TypeError("В node был передан не Book")
        if self.head is None:
            self.head = book
            self.tail = book
        self.tail.set_next(book)
        book.set_prev(self.tail)
        self.tail = book
        self.tail.set_next(self.head)
        self.head.set_prev(self.tail)

        if d is not None:
            book.data = d
        else:
            print("===========================")
            print("Adding a book in the catalog... \n"
                  "If you don't know what to enter - enter <space>")
            title = input("Enter book title: ")
            author = input("Enter author of the book: ")
            genre = input("Enter genre of the book: ")
            pages = input("Enter number of pages: ")
            format = input("Enter format of the book: ")
            publish_year = input("Enter year of the first publishing of the book: ")

            book.data = {"Title": title,
                         "Author": author,
                         "Genre": genre,
                         "Pages": pages,
                         "Format": format,
                         "Publish year": publish_year}

            for k, v in book.data.items():
                if k == "Title" and v == " ":
                    while v == " ":
                        print("No way! Book without a title is nonsense. Please, enter a title: ")
                        book.data[k] = input()
                        v = book.data[k]
                if v == " ":
                    book.data[k] = "None"  # заполняем неизвестные столбцы строкой None
                else:
                    if k == "Title" or k == "Author" or k == "Genre" or k == "Format":
                        while Book.check("word", v) == False:
                            print(k + " contains an error. Enter correct " + k + ": ")
                            book.data[k] = input()
                            v = book.data[k]
                    elif k == "Pages" or k == "Publish year":
                        if book.data[k] != "None":
                            ch = False
                            while ch == False:
                                if k == "Pages":
                                    ch = Book.check("page", v)
                                else:
                                    ch = Book.check("year", v)
                                if ch == False:
                                    print(k + " contains an error. Enter correct " + k + ": ")
                                    book.data[k] = input()
                                    v = book.data[k]
                            book.data[k] = int(book.data[k])

            print("===========================")
            print("The book is successfully added to the catalog")
            print("===========================")

    def clear(self):
        del self.head.next_
        self.head = None

    def search(self):
        """
        Функция поиска книг в каталоге
        :param: каталог, с которым работаем в формате [{"Title":"value_1", "Author":"value_2",
         "Genre":"value_3", "Pages":int, "Format":"value_4", "Publish year":int}, {...}]
        :return: new_catalog: Каталог с найденными книгами
        """
        print("===========================")

        lib2 = Library() # здесь будут результаты поиска
        new_catalog = []

        while True:
            print("""Choose the search property:
            1 - by Title
            2 - by Author
            3 - by Genre
            4 - by Number of pages
            5 - by Format of the book (ebook, hardback, paperback, audiobook)
            6 - by Publishing year
            8 - return to the main menu""")
            prop = input("Enter the search property: ")

            inp_prop = None

            if prop == "1":
                inp_prop = "Title"
            elif prop == "2":
                inp_prop = "Author"
            elif prop == "3":
                inp_prop = "Genre"
            elif prop == "4":
                inp_prop = "Pages"
            elif prop == "5":
                inp_prop = "Format"
            elif prop == "6":
                inp_prop = "Publish year"
            elif prop == "8":
                break
            else:
                print("Incorrect answer. Try again")

            if inp_prop is not None:
                if prop == "1" or prop == "2" or prop == "3" or prop == "5":  # если поиск по нахождению подстроки в строке
                    inp = input("Enter {} of the book or part (search pattern): ".format(inp_prop))
                    inp = inp.lower()  # выравниваем регистр
                    pattern = r"{}".format(inp)
                    #TODO
                    current_book = self.head
                    index = 0
                    while index <= len(self) - 1:
                        temp_str = current_book.data[inp_prop]  # catalog[index] - словарь по конкретной книге
                        temp = re.search(pattern, temp_str.lower())
                        if temp is not None:
                            if current_book.data not in new_catalog:  # защита от дублирования в new_catalog найденных книг
                                new_catalog.append(current_book.data)
                                lib2.add(current_book.data) # добавляем в результаты поиска найденные книги
                        current_book = current_book.next_
                        index += 1

                elif prop == "4" or prop == "6":  # если поиск по нахождению чисел (страниц / год публикации)
                    while True:
                        print("""Choose the search property:
                            1 - Less/Earlier than
                            2 - More/Later than
                            8 - back""")
                        dig = input("Enter the search property: ")
                        if dig == "8":
                            print("===========================")
                            break
                        if dig == "1" or dig == "2":
                            inp = input("Enter the number of pages / publishing year: ")
                            if prop == "4":
                                pattern = r"^\b\d+"
                            if prop == "6":
                                pattern = r'^\b(1[4-9][0-9]{2})|(20[0-2][0-9])'
                            temp = re.fullmatch(pattern, inp)
                            if temp is not None:
                                digit = int(inp)
                                current_book = self.head
                                index = 0
                                while index <= len(self) - 1:
                                    temp_q = current_book.data[inp_prop]
                                    if temp_q == "None":
                                        temp_q = "0"
                                    if dig == "1":
                                        if digit >= int(temp_q):
                                            if current_book.data not in new_catalog:
                                                new_catalog.append(current_book.data)
                                                lib2.add(current_book.data)
                                        current_book = current_book.next_
                                        index += 1
                                    if dig == "2":
                                        if digit <= int(temp_q):
                                            if current_book.data not in new_catalog:
                                                new_catalog.append(current_book.data)
                                                lib2.add(current_book.data)
                                        current_book = current_book.next_
                                        index += 1
                                break
                            else:
                                print("You haven't entered a digit / correct year. Try again")
                        else:
                            print("Wrong answer. Try again")

                if len(new_catalog) == 0 or len(new_catalog) == 1:
                    if len(new_catalog) == 0:
                        print("No book was found. Do you want to try again?")
                    elif len(new_catalog) == 1:
                        print(lib2)
                        print("One book was found. Do you want to search again?")
                    while True:
                        answer = input("Press <y> for yes and <n> for no: ")
                        if answer == "y":
                            print("===========================")
                            if len(new_catalog) == 1:
                                new_catalog = []  # обнуляем найденные книги
                                lib2.clear()
                            break
                        elif answer == "n":
                            print("===========================")
                            break
                        else:
                            print("Wrong answer. Try again")
                    if answer == "n":
                        break

                else:
                    print(lib2)
                    print(f"Found {len(new_catalog)} book(s)")
                    print("===========================")
                    while True:
                        print("Do you want to search in the found books?")
                        answer = input("Press <y> for yes and <n> for no: ")
                        if answer == "y":
                            self = lib2
                            new_catalog = []  # для нового поиска новый список
                            break
                        elif answer == "n":
                            print("===========================")
                            break
                        else:
                            print("Wrong answer. Try again")
                    if answer == "n":
                        break

        if len(new_catalog) >= 1:
            return new_catalog


def base():
    """
    Точка входа. Основная функция, из которой начинается работа
    :return: текущий каталог
    """
    lib = Library()
    print("The catalog is empty")
    print("You can add a book to the catalog or download the catalog from the external file")
    print("===========================")
    while True:
        print("1 - add a book to the catalog")
        print("7 - download the catalog from the external file")
        print("8 - exit")
        choose = input("Enter the corresponding digit (1, 7 or 8): ")
        if choose == "1":
            lib.add()
            break
        elif choose == "7":
            catalog = download()
            break
        elif choose == "8":
            print("The catalog has been closed!")
            break
        else:
            print("Incorrect digit. Try again.")
            print("===========================")
    if choose != "8":
        while True:
            print("What do you want to do with the catalog?")
            print("1 - add a book to the catalog")
            print("2 - edit a book in the catalog")
            print("3 - remove a book from the catalog")
            print("4 - search for a book in the catalog")
            print("5 - display all the books in the catalog")
            print("6 - save the current version of the catalog to the external file")
            print("7 - download the catalog from the external file")
            print("8 - exit")
            choose = input("Enter the corresponding digit (1 - 8): ")
            if choose == "1":
                lib.add()
            elif choose == "2":
                edit(catalog)
            elif choose == "3":
                remove(catalog)
            elif choose == "4":
                lib.search()
            elif choose == "5":
                print(lib)
            elif choose == "6":
                save(catalog)
            elif choose == "7":
                catalog = download()
            elif choose == "8":
                print("The catalog has been closed!")
                break
            else:
                print("Incorrect digit. Try again.")
                print("===========================")
    #return catalog

if __name__ ==  "__main__":
    # пример заполнения каталога ниже. Это первые 3 значения из файла library.txt
    # catalog = [{'Title': 'The secret scripture',
    #             'Author': 'Sebastian Barry',
    #             'Genre': 'Contemporary',
    #             'Pages': 416,
    #             'Format': 'ebook',
    #             'Publish year': 2017},
    #            {'Title': 'The Deptford trilogy',
    #             'Author': 'Robertson Davies',
    #             'Genre': 'fiction',
    #             'Pages': 925,
    #             'Format': 'Hardback',
    #             'Publish year': 1983},
    #            {'Title': 'KING Kong theory',
    #             'Author': 'virginie despent',
    #             'Genre': 'non-Fiction',
    #             'Pages': 112,
    #             'Format': 'Ebook',
    #             'Publish year': 2019}
    #            ]
    base()
    # lib = Library()
    # lib.add()
    # print(lib)



