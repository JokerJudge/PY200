"""Задание:

Дан каталог книг. Реализуйте библиотеку для хранения данных книг и поиску по каталогу. Каталог должен поддерживать
 возможность добавления и удаления книг, редактирования информации о книге, а также обладать персистентностью
(т.е. сохранять библиотеку в внешнем файле и подгружать обратно). Также необходимо оформить точку входа и поддерживать
поиск по различным параметрам.

# Нужно доделать регулярки, чтобы работали знаки препинания, апострофы, вопросительные и восклицательные знаки
# TODO
"""
import re
import json


def add(catalog):
    """
    Функция добавления новой книги в каталог. Проверка на корректность введенных данных (возможно, стоит выделить в
    иную функцию)
    :param catalog: каталог, с которым работаем в формате [{"Title":"value_1", "Author":"value_2",
     "Genre":"value_3", "Pages":int, "Format":"value_4", "Publish year":int}, {...}]
    :return: Измененный catalog с добавлением новой книги
    """

    print("===========================")
    print("Adding a book in the catalog... \n"
          "If you don't know what to enter - enter <space>")
    title = input("Enter book title: ")
    author = input("Enter author of the book: ")
    genre = input("Enter genre of the book: ")
    pages = input("Enter number of pages: ")
    format = input("Enter format of the book: ")
    publish_year = input("Enter year of the first publishing of the book: ")

    temp_dict = {"Title": title,
                 "Author": author,
                 "Genre": genre,
                 "Pages": pages,
                 "Format": format,
                 "Publish year": publish_year}

    pattern_w = r'^\b[\w\(\)\-@]+(\s?[\w\(\)\-@]+)*' # проверка на отсутствие недопустимых символов
    for k, v in temp_dict.items():
        if k == "Title" and v == " ":
            while v == " ":
                print("No way! Book without title is nonsense. Please, enter a Title: ")
                temp_dict[k] = input()
                v = temp_dict[k]
        if v == " ":
            temp_dict[k] = "None"
        else:
            temp = None
            while temp is None:
                temp = re.fullmatch(pattern_w, v)
                if temp is None:  # если введенное пользователем является некорректным
                    print(k + " contains error. Enter correct " + k + ": ")
                    temp_dict[k] = input()
                    v = temp_dict[k]

    pattern_pages = r'^\b\d{1,7}' # проверка на корректность ввода страниц
    if temp_dict["Pages"] != "None":
        temp = None
        while temp is None:
            temp = re.fullmatch(pattern_pages, temp_dict["Pages"])
            if temp is None:  # если введенное пользователем является некорректным
                print("Pages contains error. Enter number of pages: ")
                temp_dict["Pages"] = input()

    if temp_dict["Pages"] != "None":
        temp_dict["Pages"] = int(temp_dict["Pages"])


    pattern_year = r'^\b(1[4-9][0-9]{2})|(20[0-2][0-9])' # проверка на корректность ввода года
    if temp_dict["Publish year"] != "None":
        temp = None
        while temp is None:
            temp = re.fullmatch(pattern_year, temp_dict["Publish year"])
            if temp is None:  # если введенное пользователем является некорректным
                print("Publish year contains error. Enter date (ex: 2015): ")
                temp_dict["Publish year"] = input()

    if temp_dict["Publish year"] != "None":
        temp_dict["Publish year"] = int(temp_dict["Publish year"])

    catalog.append(temp_dict)

    print("===========================")
    print("The book is successfully added in the catalog")
    print("===========================")
    return catalog


def edit(catalog):
    """
    Функция, принимающая каталог и вносящая изменение в свойства книги. Книгу и свойства пользователь может выбрать.
    :param catalog: каталог, в котором будет производиться изменение книги
    :return: Измененный каталог с книгами
    """
    print("===========================")
    print("What book do you want to edit? \n"
          "Search until you find one")
    new_catalog = search(catalog)
    if type(new_catalog) is not None:
        while True:
            if len(new_catalog) == 1:
                display(new_catalog)
                print("Do you wish to edit this one?\n"
                      "press <y> to edit, <n> to continue searching,"
                      "<x> to return to main menu: ")
                while True:
                    answer = input()
                    if answer == "y":
                        while True:
                            print("""What property do you need to edit?
                            1 - Title
                            2 - Author
                            3 - Genre
                            4 - quantity of pages
                            5 - Format of the book (ebook, hardback, paperback, audiobook)
                            6 - publishing year
                            8 - return to main menu
                            """)
                            prop = input("Enter the answer: ")

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
                                answer = "x"
                                break
                            else:
                                print("Incorrect answer. Try again")

                            if inp_prop is not None:
                                if prop == "1" or prop == "2" or prop == "3" or prop == "5":
                                    temp_val = input(f"Enter new value of {inp_prop}: ")
                                    pattern_w = r'^\b[\w\(\)\-@]+(\s?[\w\(\)\-@]+)*'
                                    temp = None
                                    while temp is None:
                                        temp = re.fullmatch(pattern_w, temp_val)
                                        if temp is None:  # если введенное пользователем является некорректным
                                            print(inp_prop + " contains error. Enter correct " + inp_prop + ": ")
                                            temp_val = input()

                                    temp_dict = catalog[catalog.index(new_catalog[0])] # catalog.index(new_catalog) - индекс элемента в изначальном каталоге
                                    temp_dict[inp_prop] = temp_val
                                    temp_lst = []
                                    temp_lst.append(temp_dict)
                                    display(temp_lst)
                                    print("===========================")
                                    print("The book successfully has been edited")
                                    print("===========================")
                                    break
                                elif prop == "4":
                                    temp_val = input(f"Enter new value of {inp_prop}: ")
                                    pattern_d = r'^\b\d{1,7}'
                                    temp = None
                                    while temp is None:
                                        temp = re.fullmatch(pattern_d, temp_val)
                                        if temp is None:  # если введенное пользователем является некорректным
                                            print(inp_prop + " contains error. Enter correct " + inp_prop + ": ")
                                            temp_val = input()
                                    temp_val = int(temp_val)

                                    temp_dict = catalog[catalog.index(
                                        new_catalog[0])]  # catalog.index(new_catalog) - индекс элемента в изначальном каталоге
                                    temp_dict[inp_prop] = temp_val
                                    temp_lst = []
                                    temp_lst.append(temp_dict)
                                    display(temp_lst)
                                    print("===========================")
                                    print("The book successfully has been edited")
                                    print("===========================")
                                    break
                                elif prop == "6":
                                    temp_val = input(f"Enter new value of {inp_prop}: ")
                                    pattern_year = r'^\b(1[4-9][0-9]{2})|(20[0-2][0-9])'
                                    temp = None
                                    while temp is None:
                                        temp = re.fullmatch(pattern_year, temp_val)
                                        if temp is None:  # если введенное пользователем является некорректным
                                            print(inp_prop + " contains error. Enter correct " + inp_prop + ": ")
                                            temp_val = input()
                                    temp_val = int(temp_val)

                                    temp_dict = catalog[catalog.index(
                                        new_catalog[0])]  # catalog.index(new_catalog) - индекс элемента в изначальном каталоге
                                    temp_dict[inp_prop] = temp_val
                                    temp_lst = []
                                    temp_lst.append(temp_dict)
                                    display(temp_lst)
                                    print("===========================")
                                    print("The book successfully has been edited")
                                    print("===========================")
                                    break
                        break
                    elif answer == "n":
                        new_catalog = search(catalog)
                        break
                    elif answer == "x":
                        break
                    else:
                        print("Wrong answer. Try again")
                if answer == "y" or answer == "x":
                    break

            else:
                print("To edit a book, you need to chose one")
                new_catalog = search(catalog)



def remove(catalog):
    """
    Функция, удаляющая книгу из каталога. Работает через вызов функции по поиску.
    Можно удалить как одну книгу, так и сразу несколько
    :param catalog: каталог, с которым работаем в формате [{"Title":"value_1", "Author":"value_2",
     "Genre":"value_3", "Pages":int, "Format":"value_4", "Publish year":int}, {...}]
    :return: None
    """
    print("===========================")
    print("What book do you want to delete from catalog? \n"
          "Search until you find one or several")
    new_catalog = search(catalog)
    if type(new_catalog) is not None:
        while True:
            if len(new_catalog) == 1:
                display(new_catalog)
                print("Do you wish to delete this one?\n"
                      "press <y> to delete, <n> to continue searching,"
                      "<x> to return to main menu: ")
                while True:
                    answer = input()
                    if answer == "y":
                        catalog.remove(new_catalog[0])
                        print("===========================")
                        print("The book successfully has been deleted")
                        print("===========================")
                        break
                    elif answer == "n":
                        new_catalog = search(catalog)
                        break
                    elif answer == "x":
                        break
                    else:
                        print("Wrong answer. Try again")
                if answer == "y" or answer == "x":
                    break

            elif len(new_catalog) > 1:
                display(new_catalog)
                print("Do you wish to delete all these books?\n"
                      "press <y> to delete and <n> to continue searching,"
                      "<x> to return to main menu: ")
                while True:
                    answer = input()
                    if answer == "y":
                        for i in new_catalog:
                            catalog.remove(i)
                        print("===========================")
                        print("The books successfully have been deleted")
                        print("===========================")
                        break
                    elif answer == "n":
                        new_catalog = search(catalog)
                        break
                    elif answer == "x":
                        break
                    else:
                        print("Wrong answer. Try again")
                if answer == "y" or answer == "x":
                    break
            else:
                print("To delete a book, you need to chose one")


def search(catalog):
    """
    Функция поиска книг в каталоге
    :param catalog: каталог, с которым работаем в формате [{"Title":"value_1", "Author":"value_2",
     "Genre":"value_3", "Pages":int, "Format":"value_4", "Publish year":int}, {...}]
    :return: new_catalog: Каталог с найденными книгами
    """
    print("===========================")
    new_catalog = [] # здесь будут результаты поиска
    while True:
        print("""Chose search property:
        1 - by Title
        2 - by Author
        3 - by Genre
        4 - by quantity of pages
        5 - by Format of the book (ebook, hardback, paperback, audiobook)
        6 - by publishing year
        8 - return to main menu""")
        prop = input("Enter search property: ")

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
            if prop == "1" or prop == "2" or prop == "3" or prop == "5": # если поиск по нахождению подстроки в строке
                inp = input("Enter {} of the book or part (search pattern): ".format(inp_prop))
                print(inp)
                inp = inp.lower()  # выравниваем регистр
                pattern = r"{}".format(inp)

                index = 0
                while index <= len(catalog) - 1:
                    temp_str = catalog[index][inp_prop]
                    temp = re.search(pattern, temp_str.lower())
                    if temp is not None:
                        if catalog[index] not in new_catalog:
                            new_catalog.append(catalog[index])
                    index += 1

            elif prop == "4" or prop == "6":  # если поиск по нахождению чисел (страниц / год публикации)
                if prop == "4":
                    while True:
                        print("""Chose search property:
                            1 - Less than
                            2 - More than
                            8 - back""")
                        dig = input("Enter search property: ")

                        if dig == "1":
                            inp = input("Enter quontity of pages: ")
                            print(inp)
                            pattern = r"^\b\d+"
                            temp = re.fullmatch(pattern, inp)
                            if temp is not None:
                                digit = int(inp)
                                index = 0
                                while index <= len(catalog) - 1:
                                    temp_q = catalog[index][inp_prop]
                                    if temp_q == "None":
                                        temp_q = "0"
                                    if digit >= int(temp_q):
                                        if catalog[index] not in new_catalog:
                                            new_catalog.append(catalog[index])
                                    index += 1
                                break
                            else:
                                print("You entered not a digit. Try again")

                        elif dig == "2":
                            inp = input("Enter quontity of pages: ")
                            print(inp)
                            pattern = r"^\b\d+"
                            temp = re.fullmatch(pattern, inp)
                            if temp is not None:
                                digit = int(inp)
                                index = 0
                                while index <= len(catalog) - 1:
                                    temp_q = catalog[index][inp_prop]
                                    if temp_q == "None":
                                        temp_q = "0"
                                    if digit <= int(temp_q):
                                        if catalog[index] not in new_catalog:
                                            new_catalog.append(catalog[index])
                                    index += 1
                                break
                            else:
                                print("You entered not a digit. Try again")

                        elif dig == "8":
                            print("===========================")
                            break
                        else:
                            print("Wrong answer. Try again")

                elif prop == "6":
                    while True:
                        print("""Chose search property:
                            1 - Earlier than
                            2 - Later than
                            8 - back""")
                        dig = input("Enter search property: ")

                        if dig == "1":
                            inp = input("Enter year: ")
                            print(inp)
                            pattern = r'^\b(1[4-9][0-9]{2})|(20[0-2][0-9])'
                            temp = re.fullmatch(pattern, inp)
                            if temp is not None:
                                digit = int(inp)
                                index = 0
                                while index <= len(catalog) - 1:
                                    temp_q = catalog[index][inp_prop]
                                    if temp_q == "None":
                                        temp_q = "0"
                                    if digit >= int(temp_q):
                                        if catalog[index] not in new_catalog:
                                            new_catalog.append(catalog[index])
                                    index += 1
                                break
                            else:
                                print("You entered incorrect year. Try again")

                        elif dig == "2":
                            inp = input("Enter year: ")
                            print(inp)
                            pattern = r'^\b(1[4-9][0-9]{2})|(20[0-2][0-9])'
                            temp = re.fullmatch(pattern, inp)
                            if temp is not None:
                                digit = int(inp)
                                index = 0
                                while index <= len(catalog) - 1:
                                    temp_q = catalog[index][inp_prop]
                                    if temp_q == "None":
                                        temp_q = "0"
                                    if digit <= int(temp_q):
                                        if catalog[index] not in new_catalog:
                                            new_catalog.append(catalog[index])
                                    index += 1
                                break
                            else:
                                print("You entered incorrect year. Try again")

                        elif dig == "8":
                            print("===========================")
                            break
                        else:
                            print("Wrong answer. Try again")

            if len(new_catalog) == 0:
                print("No books was found. Do you want to try again?")
                while True:
                    answer = input("Press <y> for yes and <n> for no: ")
                    if answer == "y":
                        print("===========================")
                        break
                    elif answer == "n":
                        print("===========================")
                        break
                    else:
                        print("Wrong answer. Try again")
            elif len(new_catalog) == 1:
                display(new_catalog)
                print("One book was found. Do you want a new search?")
                while True:
                    answer = input("Press <y> for yes and <n> for no: ")
                    if answer == "y":
                        print("===========================")
                        break
                    elif answer == "n":
                        print("===========================")
                        break
                    else:
                        print("Wrong answer. Try again")
                if answer == "n":
                    break

            else:
                display(new_catalog)
                print(f"Found {len(new_catalog)} book(s)")
                print("===========================")
                while True:
                    print("Do you want to search in found books?")
                    answer = input("Press <y> for yes and <n> for no: ")
                    if answer == "y":
                        catalog = new_catalog
                        new_catalog = [] # для нового поиска новый список
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



def display(catalog):
    """
    Функция отрисовки в консоли в виде таблицы каталога книг и выдержек из него
    :param catalog: каталог, с которым работаем в формате [{"Title":"value_1", "Author":"value_2",
     "Genre":"value_3", "Pages":int, "Format":"value_4", "Publish year":int}, {...}]
    :return: None
    """
    print("===========================")
    print("============================"*6)
    print("|", end=" ")
    print("Title", end=" " * 30)
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
    print("============================"*6)

    index = 0
    while index <= len(catalog) - 1:
        print("|", end=" ")
        print(catalog[index]["Title"], end=" " * (35 - len(catalog[index]["Title"])))
        print("|", end=" ")
        print(catalog[index]["Author"], end=" " * (35 - len(catalog[index]["Author"])))
        print("|", end=" ")
        print(catalog[index]["Genre"], end=" " * (20 - len(catalog[index]["Genre"])))
        print("|", end=" ")
        print(catalog[index]["Pages"], end=" " * (10 - len(str(catalog[index]["Pages"]))))
        print("|", end=" ")
        print(catalog[index]["Format"], end=" " * (15 - len(catalog[index]["Format"])))
        print("|", end=" ")
        print(catalog[index]["Publish year"], end=" " * (14 - len(str(catalog[index]["Pages"]))))
        print("|", end=" ")
        print()
        print("----------------------------"*6)
        index += 1

    print("===========================")

def save(catalog):
    """
    Функция, сериализирующая в формат json текущий вариант каталога книг и помещающая его в файл library.txt
    :param catalog: каталог, с которым работаем в формате [{"Title":"value_1", "Author":"value_2",
     "Genre":"value_3", "Pages":int, "Format":"value_4", "Publish year":int}, {...}]
    :return: None
    """
    print("===========================")
    with open("library.txt", "wt") as f:
        json.dump(catalog, f)
    print("Catalog successfully saved to library.txt")
    print("===========================")

def download():
    """
    Функция, десериализирующая объект json, находящийся в файле книжного каталога library.txt
    :return: Возвращает каталог в формате каталог, с которым работаем в формате [{"Title":"value_1", "Author":"value_2",
     "Genre":"value_3", "Pages":int, "Format":"value_4", "Publish year":int}, {...}], загруженный из library.txt
    """
    print("===========================")
    with open("library.txt", "rt") as f:
        catalog = json.load(f)
    print("Catalog successfully downloaded from library.txt")
    print("===========================")
    return catalog

def base():
    catalog = [] # объявляем пустой каталог
    print("Now catalog is empty")
    print("You can add a book into the catalog or download the catalog from external file")
    print("===========================")
    while True:
        print("1 - add a book into the catalog")
        print("7 - download the catalog from the external file")
        print("8 - exit")
        choose = input("Enter the corresponding digit (1, 7 or 8): ")
        if choose == "1":
            add(catalog)
            break
        elif choose == "7":
            catalog = download()
            break
        elif choose == "8":
            print("Catalog has been closed!")
            break
        else:
            print("Incorrect digit. Try again.")
            print("===========================")
    if choose != "8":
        while True:
            print("What do you want to do with the catalog?")
            print("1 - add a book into the catalog")
            print("2 - edit a book in the catalog")
            print("3 - remove a book from the catalog")
            print("4 - search for a book in the catalog")
            print("5 - display all the books in the catalog")
            print("6 - save the current version of the catalog in the external file")
            print("7 - download the catalog from the external file")
            print("8 - exit")
            choose = input("Enter the corresponding digit (1 - 8): ")
            if choose == "1":
                add(catalog)
            elif choose == "2":
                edit(catalog)
            elif choose == "3":
                remove(catalog)
            elif choose == "4":
                search(catalog)
            elif choose == "5":
                display(catalog)
            elif choose == "6":
                save(catalog)
            elif choose == "7":
                catalog = download()
            elif choose == "8":
                print("Catalog has been closed!")
                break
            else:
                print("Incorrect digit. Try again.")
                print("===========================")

if __name__ ==  "__main__":
    catalog = [{'Title': 'The secret scripture',
                'Author': 'Sebastian Barry',
                'Genre': 'Contemporary',
                'Pages': 416,
                'Format': 'ebook',
                'Publish year': 2017},
               {'Title': 'The Deptford trilogy',
                'Author': 'Robertson Davies',
                'Genre': 'fiction',
                'Pages': 925,
                'Format': 'Hardback',
                'Publish year': 1983},
               {'Title': 'KING Kong theory',
                'Author': 'virginie despent',
                'Genre': 'non-Fiction',
                'Pages': 112,
                'Format': 'Ebook',
                'Publish year': 2019}
               ]
    base()
