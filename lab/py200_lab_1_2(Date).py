#Лабораторная работа № 1.2 (4 ак.ч.)

# Слушатель (ФИО): Коваленко Е.Н.

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

---

7. Написать тесты для проверки реализованного функционала (Необязательное)

Доп информация
- https://habr.com/ru/post/261773/ -> формула нахождения количества дней в месяце
- https://habr.com/ru/post/458356/ -> формула нахождения дня недели в произвольном году
- https://habr.com/ru/post/455796/ -> сравнение ООП Java и Python
- https://pythonworld.ru/osnovy/peregruzka-operatorov.html -> перегрузка операторов
'''


class Date:
    DAY_OF_MONTH = ((31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  #
                    (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31))  #

    def __init__(self, *args):
        if len(args) == 3:
            if not isinstance(args[0], int) or not isinstance(args[1], int) or not isinstance(args[2], int):
                raise TypeError('Date must be str in format "YYYY.M[M].D[D]" or int <YYYY, M[M], D[D]>')
            year = args[0]
            month = args[1]
            day = args[2]
            try:
                Date.is_valid_date(year, month, day)
            except:
                raise ValueError('Not valid date')
            self.__year = args[0]
            self.__month = args[1]
            self.__day = args[2]
        elif len(args) == 1:
            if not isinstance(args[0], str):
                raise TypeError('Date must be str in format "YYYY.M[M].D[D]" or int <YYYY, M[M], D[D]>')
            value = args[0].split('.')
            if len(value) != 3:
                raise TypeError('Date must be str in format "YYYY.M[M].D[D]" or int <YYYY, M[M], D[D]>')

            try:
                year = int(value[0])
                month = int(value[1])
                day = int(value[2])
            except:
                raise ValueError('Date must be str in format "YYYY.M[M].D[D]" or int <YYYY, M[M], D[D]>')

            try:
                Date.is_valid_date(year, month, day)
            except:
                raise ValueError('Not valid date')
            self.__day = day
            self.__month = month
            self.__year = year
        else:
            raise TypeError('Date must be str in format "YYYY.M[M].D[D]" or int <YYYY, M[M], D[D]>"')


    def __str__(self):
        return f'{self.__day:0>2}.{self.__month:0>2}.{self.__year}'

    def __repr__(self):
        return f'Date({self.__year!r}, {self.__month!r}, {self.__day!r})'

    @staticmethod
    def is_leap_year(year):
        if year % 4 == 0: # високосный год - кратен 4 или 400 и не кратен 100
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                return False
            return True
        else:
            return False

    @classmethod
    def get_max_day(cls, year, month):
        leap_year = 1 if cls.is_leap_year(year) else 0
        return cls.DAY_OF_MONTH[leap_year][month-1]

    @property
    def date(self):
        return self.__str__

    @classmethod
    def is_valid_date(cls, year, month, day):
        if not isinstance(year, int):
            raise TypeError('year must be int')
        if not isinstance(month, int):
            raise TypeError('month must be int')
        if not isinstance(day, int):
            raise TypeError('day must be int')

        if not 0 <= year:
            raise ValueError("year should be positive")

        if not 0 < month <= 12:
            raise ValueError('month must be 0 < month <= 12')

        if not 0 < day <= cls.get_max_day(year, month):
            raise ValueError('invalid day for this month and year')

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise TypeError('Date must be str')
        value = value.split('.')
        if len(value) != 3:
            raise ValueError('Invalid date format')

        try:
            year = int(value[0])
            month = int(value[1])
            day = int(value[2])
            self.is_valid_date(year, month, day)
        except:
            raise ValueError('Invalid date format')

        self.__day = day
        self.__month = month
        self.__year = year

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        if isinstance(day, int):
            self.is_valid_date(self.__year, self.__month, day)
            self.__day = day
        else:
            raise ValueError("Invalid day")

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month):
        if isinstance(month, int):
            self.is_valid_date(self.__year, month, self.__day)
            self.__month = month
        else:
            raise ValueError("Invalid month")

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if isinstance(year, int):
            self.is_valid_date(year, self.__month, self.__day)
            self.__year = year
        else:
            raise ValueError("Year must be positive")

    def add_day(self, day):
        if isinstance(day, int):
            if day + self.__day <= self.get_max_day(self.__year, self.__month): # если нет переполнения в текущем месяце
                self.__day = self.__day + day
            else:
                to_next_month = self.get_max_day(self.__year, self.__month) - self.__day
                day = day - to_next_month - 1
                self.__day = 1
                self.add_month(1)
                while day >= self.get_max_day(self.__year, self.__month):
                    day = day - self.get_max_day(self.__year, self.__month)
                    self.add_month(1)
                self.__day = self.__day + day
        else:
            raise ValueError("День должен быть int")

    def add_month(self, month):
        if isinstance(month, int):
            month_to_add = month % 12
            years_to_add = month // 12
            if month_to_add + self.__month > 12:
                self.__year = self.__year + years_to_add + 1
                self.__month = self.__month + month_to_add - 12
            else:
                self.__year = self.__year + years_to_add
                self.__month = self.__month + month_to_add

        else:
            raise ValueError("Месяц должен быть int")

    def add_year(self, year):
        if isinstance(year, int):
            self.__year = self.__year + year
        else:
            raise ValueError("Год должен быть int")

    def sub_day(self, day):
        if isinstance(day, int):
            if self.__day - day >= 1: # если нет переполнения в текущем месяце
                self.__day = self.__day - day
            else:
                to_next_month = self.__day
                day = day - to_next_month
                self.sub_month(1)
                self.__day = self.get_max_day(self.__year, self.__month)
                while day >= self.get_max_day(self.__year, self.__month):
                    day = day - self.get_max_day(self.__year, self.__month)
                    self.sub_month(1)
                self.__day = self.get_max_day(self.__year, self.__month) - day
        else:
            raise ValueError("День должен быть int")


    def sub_month(self, month):
        if isinstance(month, int):
            month_to_sub = month % 12
            years_to_sub = month // 12
            if self.__month - month_to_sub < 1:
                self.__year = self.__year - years_to_sub - 1
                self.__month = 12 + (self.__month - month_to_sub)
            else:
                self.__month = self.__month - month_to_sub

        else:
            raise ValueError("Месяц должен быть int")

    def sub_year(self, year):
        if isinstance(year, int):
            self.__year = self.__year - year
        else:
            raise ValueError("Год должен быть int")

    @staticmethod
    def date2_date1(date2, date1): # разница в днях между двумя датами
        return date2.date_to_days() - date1.date_to_days()

    def date_to_days(self):
        return self.__year * 365 + self.__month * 30 + self.__day

    def __eq__(self, other):
        #self - то, что слева от операнда, а other - то, что справа
        if (self.__day == other.__day) and (self.__month == other.__month) and (self.__year == other.__year):
            return True
        else:
            return False

    def __ne__(self, other):
        #self - то, что слева от операнда, а other - то, что справа
        if (self.__day == other.__day) and (self.__month == other.__month) and (self.__year == other.__year):
            return False
        else:
            return True

    def __lt__(self, other):
        if self.__year < other.__year:
            return True
        elif self.__year > other.__year:
            return False
        else:
            if self.__month < other.__month:
                return True
            elif self.__month > other.__month:
                return False
            else:
                if self.__day < other.__day:
                    return True
                elif self.__day > other.__day:
                    return False
                else:
                    return False

    def __le__(self, other):
        if self.__year < other.__year:
            return True
        elif self.__year > other.__year:
            return False
        else:
            if self.__month < other.__month:
                return True
            elif self.__month > other.__month:
                return False
            else:
                if self.__day < other.__day:
                    return True
                elif self.__day > other.__day:
                    return False
                else:
                    return True

    def __gt__(self, other):
        if self.__year < other.__year:
            return False
        elif self.__year > other.__year:
            return True
        else:
            if self.__month < other.__month:
                return False
            elif self.__month > other.__month:
                return True
            else:
                if self.__day < other.__day:
                    return False
                elif self.__day > other.__day:
                    return True
                else:
                    return False

    def __ge__(self, other):
        if self.__year < other.__year:
            return False
        elif self.__year > other.__year:
            return True
        else:
            if self.__month < other.__month:
                return False
            elif self.__month > other.__month:
                return True
            else:
                if self.__day < other.__day:
                    return False
                elif self.__day > other.__day:
                    return True
                else:
                    return True

    def __add__(self, other):
        if not isinstance(other, int):
            raise ValueError
        else:
            self.add_day(other)


    def __radd__(self, other):
        if not isinstance(other, int):
            raise ValueError
        else:
            self.add_day(other)

    def __sub__(self, other):
        if not isinstance(other, int):
            raise ValueError
        else:
            pass
            self.sub_day(other)

    def __int__(self):
        return self.date_to_days()

if __name__ == "__main__":
    date1 = Date(2008, 1, 15)
    date2 = Date("2018.11.1")
    print(date1)
    date1.add_day(411)
    print(date1)
    print(Date.date2_date1(date2, date1))


    print("++++++++++++")

    print(date1.date)
    print(date1.date_to_days())

    print("++++++++++")
    d1 = Date(2019, 2, 10)
    d1_1 = Date(2020, 2, 7)
    d2 = Date(2020, 1, 11)
    #print(d1.date_to_days() - d2.date_to_days())
    print(d1 == d1_1)
    print(d1 == d2)
    print("++++++++++")
    print(d1 < d2)
    print(d1 > d2)
    d1 + 5
    print(d1)
    25 + d1
    print(d1)
    print("++++++++++")
    d1.sub_year(28)
    print(d1)
    d1.sub_month(15)
    print(d1)
    d1.sub_day(42)
    print(d1)
    d1 - 15
    print(d1)
    print(int(d1))

