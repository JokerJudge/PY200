'''
установить pyside2

1.Атрибут класса
1.1. Публичный атрибут класса
1.2. Приватный атрибут класса (2 подчеркивания)
1.3. Защищенный атрибут класса (1 подчеркивание)
2. Атрибут экземпляра
2.1. Публичный атрибут экземпляра
2.2. Приватный атрибут экземпляра (2 подчеркивания)
2.3. Защищенный атрибут экземпляра (1 подчеркивание)
3. Методы экземпляра
3.1. Публичный метод экземпляра
3.2. Приватный метод экземпляра (2 подчеркивания)
3.3. Защищенный метод экземпляра (1 подчеркивание)
4. Класс метод @classmethod
...
5. Статик метод @staticmethod
...
6. Свойство @property

Потом нужно наследоваться. И проверить все области видимости
'''

class A:
    public_class_attr_A = "public_class_attr_A"
    _protected_class_attr_A = "_protected_class_attr_A"
    __private_class_attr_A = "__private_class_attr_A"

    def __init__(self): #public_unit_attr_A, protected_unit_attr_A, private_unit_attr_A
        self.public_unit_attr_A = "public_unit_attr_A"
        self._protected_unit_attr_A = "_protected_unit_attr_A"
        self.__private_unit_attr_A = "__private_unit_attr_A"

    def public_unit_method_A(self):
        print("public_unit_method_A")

    def _protected_unit_method_A(self):
        print("_protected_unit_method_A")

    def __private_unit_method_A(self):
        print("__private_unit_method_A")

    @classmethod
    def public_class_method_A(self):
        print("public_class_method_A")

    @classmethod
    def _protected_class_method_A(self):
        print("_protected_class_method_A")

    @classmethod
    def __private_class_method_A(self):
        print("__private_class_method_A")

    @staticmethod
    def public_static_method_A(self):
        print("public_static_method_A")

    @staticmethod
    def _protected_static_method_A(self):
        print("_protected_static_method_A")

    @staticmethod
    def __private_static_method_A(self):
        print("__private_static_method_A")

    @property
    def public_property_A(self):
        print("public_property_A")
        return

    @property
    def _protected_property_A(self):
        print("_protected_property_A")
        return

    @property
    def __private_property_A(self):
        print("__private_property_A")
        return


class B(A):
    public_class_attr_B = "public_class_attr_B"
    _protected_class_attr_B = "_protected_class_attr_B"
    __private_class_attr_B = "__private_class_attr_B"



if __name__ == "__main__":
    a = A()
    print(a.public_class_attr_A)
    #print(a.__private_class_attr_A)
    print(a._protected_class_attr_A)
    print(a.public_unit_attr_A)
    print(a._protected_unit_attr_A)
    #print(a.__private_unit_attr_A)
    a.public_unit_method_A()
    a._protected_unit_method_A()
    # и т.д. проверить все