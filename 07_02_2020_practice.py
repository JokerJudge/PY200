class A:
    a = 1

    def __init__(self, a=None):
        self.a = a

    def print_a(self):
        print("Attr <a> from object <{}> = {}".format(self.__class__.__name__, self.a))

    @classmethod
    def other_print_a(cls):
        print("Attr <a> from object <{}> = {}".format(cls.__class__.__name__, cls.a))


a = A()

a.print_a()

a.other_print_a()

print("++++++++++++++++")

a = A(100)
a.print_a()

a.other_print_a()

print("++++++++++++++++")

A.a = 101
a.other_print_a()

print("++++++++++++++++")

# изменяем
#a.__class__.a = 1000
A.other_print_a()

print("++++++++++++++++")
A.print_a(a)


# self.a - смотрим сначала в своих аттрибутах, а


print("++++++++++++++++")


class A:
    a = 1

    def __init__(self, a=None):
        self.a = a

    def print_a(self):
        print("Attr <a> from object <{}> = {}".format(self.__class__.__name__, self.a))

    @classmethod
    def other_print_a(cls):
        print("Attr <a> from object <{}> = {}".format(cls.__class__.__name__, cls.a))


class B(A):
    def __init__(self, b):
        self.b = b


b = B(2)
b.print_a()

print("++++++++++++++++")

b.other_print_a()

print("++++++++++++++++")
b.a = 200
b.print_a()

print("++++++++++++++++")
b.other_print_a()

print("++++++++++++++++")
B.a = 2000
b.other_print_a()
print("++++++++++++++++")

print(A.a)
print("++++++++++++++++")
A.a = 1000
a.other_print_a()


print("++++++++++++++++")
print("++++++++++++++++")

'''
#A - класс
#А() - конструктор класса А (__init__)

class A:
    b_class_attr = 1
    def __init__(self):
        self.b_obj_attr = 2
        self.__b = 1
    def b_method(self):


    @property
    def b_property(self):
        return self.__b

a_obj = A()

A.b_class_attr # атрибут класса
a_obj.b_obj_attr # аттрибут объекта
a_obj.b_property # свойство

get_b()

set_b()

'''

class A_without_property:
    def __init__(self, a):
        self.__a = a

    def get_a(self):
        return self.__a

    def set_a(self, a):
        self.__a = a

a_without = A_without_property(1)
#a_without.a # выведет ошибку, т.к. а не видит из-за __а
a_from_a_without = a_without.get_a()# чтобы получить а, нужно через get
print(a_from_a_without)


print("++++++++++++++++")
print("++++++++++++++++")

class A_with_property:
    def __init__(self, a):
        self.__a = a

    @property
    def a(self):
        print("Call property")
        return self.__a

    @a.getter
    def a(self):
        print("Call property")
        return self.__a

    @a.setter
    def a(self, a):
        print("Call setter")
        self.__a = a

a_with = A_with_property(1)
a_with.a # вызовется @property

a_from_a_with = a_with.a # вызовется @a.getter
a_with.a = 5