'''
То же самое, что и #7 в Date.py

1. Реализовать класс Date согласно шаблону
    1.1 Конструктор класса
    1.2 Свойства для дня, месяца, года
    1.3 Сеттеры и геттеры для свойств
2. Реализовать методы add_day, add_month, add_year
3. Переопределить магические методы для класса Date:
    __lt__(self, other) - x < y вызывает x.__lt__(y).
    __le__(self, other) - x ≤ y вызывает x.__le__(y).
    __eq__(self, other) - x == y вызывает x.__eq__(y).
    __ne__(self, other) - x != y вызывает x.__ne__(y)
    __gt__(self, other) - x > y вызывает x.__gt__(y).
    __ge__(self, other) - x ≥ y вызывает x.__ge__(y).
4. Перегрузка арифметических операторов для класса Date:
    __add__(self, other) - сложение. x + y вызывает x.__add__(y).
    __sub__(self, other) - вычитание (x - y).
    __radd__(self, other).
    __rsub__(self, other).
    __iadd__(self, other) - +=.
    __isub__(self, other) - -=.
5. Переопределить преобразование типа в int.
    __int__(self)
6. Перегрузить конструктор класса

---

7. Написать тесты для проверки реализованного функционала (Необязательное)

Доп информация
- https://habr.com/ru/post/261773/ -> формула нахождения количества дней в месяце
- https://habr.com/ru/post/458356/ -> формула нахождения для недели в произвольном году
- https://habr.com/ru/post/455796/ -> сравнение ООП Java и Python
- https://pythonworld.ru/osnovy/peregruzka-operatorov.html -> перегрузка операторов
'''


class Date:
    DAY_OF_MONTH = ((31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  #
                    (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31))  #

    def __init__(self, *args):
        if len(args) == 3:
            self.year = args[0]
            self.month = args[1]
            self.day = args[2]
        if len(args) == 1:
            pass
            # мы поймем, что это строка
            # проверить что это строка, проверить по регуляркам, распарсить, отсплитовать
        else:
            raise ValueError


    def __str__(self):
        return f'{self.day}.{self.month}.{self.year}'

    def __repr__(self):
        return f'Date({self.__year!r}, {self.__month!r}, {self.__day!r})'

    @staticmethod
    def is_leap_year(year):
        return False  #
    # делится на 4 и не кратно 100 и не кратно 400

    @classmethod
    def get_max_day(cls, year, month):
        pass
    #вводите год, вводится месяца
    #выясняется, количество дней в этом месяце.

    @property
    def date(self):
        return self.__str__
    #свойство ведет себя как аттрибут. Но вызываем как метод. Но скобки не нужны.


    @classmethod
    def __is_valid_date(cls, *args):
        pass

    @date.setter
    def date(self, value):
        pass

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        if isinstance(day, int):
            self.__day = day
        else:
            raise ValueError

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month):
        if isinstance(month, int):
            self.__month = month
        else:
            raise ValueError

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if isinstance(year, int):
            self.__year = year
        else:
            raise ValueError

    def add_day(self, day):
        pass

    def add_month(self, month):
        pass

    def add_year(self, year):
        pass

    @staticmethod
    def date2_date1(date2, date1):
        pass

    def date_to_days(self):
        return self.__year * 365 + self.__month * 30 + self.__day

    def __eq__(self, other):
        #self - то, что слева от операнда, а other - то, что справа
        if (self.day == other.day) and (self.month == other.month) and (self.year == other.year):
            return True
        else:
            return False

    def __lt__(self, other):
        if self.year < other.year:
            return True
        elif self.year > other.year:
            return False
        else:
            if self.month < other.month:
                return True
            elif self.month > other.month:
                return False
            else:
                if self.day < other.day:
                    return True
                elif self.day > other.day:
                    return False
                else:
                    return False

    def __add__(self, other):
        if not isinstance(other, int):
            raise ValueError
        else:
            self.__day += other


    def __radd__(self, other):
        if not isinstance(other, int):
            raise ValueError
        else:
            self.__day += other



date1 = Date(2019,12,22)

print(date1)
print(date1.date)
print(date1.date_to_days())


print("++++++++++")
d1 = Date(2020, 2, 7)
d1_1 = Date(2020, 2, 7)
d2 = Date(2020, 2, 6)
#print(d1.date_to_days() - d2.date_to_days())
print(d1 == d1_1)
print(d1 == d2)
print(d1 < d2)
print(d1 > d2)
d1 + 5
print(d1)
5 + d1
print(d1)