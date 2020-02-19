# -*- coding: utf-8

# 
# Курс DEV-PY200. Объектно-ориентированное программирование на языке Python
# Тема 1.1 Основы ООП. Понятие класса, объекта. Создание экземпляра класса

# Лабораторная работа № 1.1 (4 ак.ч.)

# Слушатель (ФИО): Коваленко Е.Н.

# ---------------------------------------------------------------------------------------------
# Понятие класса, объекта (стр. 1-22)

# 1. Создайте класс Glass с атрибутами capacity_volume и occupied_volume
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)

class Glass:
    def __init__(self, capacity_volume, occupied_volume):
        if isinstance(capacity_volume, (int, float)): # проверка сразу на int и на float
            if capacity_volume > 0: # проверка на неотрицательность
                self.capacity_volume = capacity_volume
            else:
                raise ValueError
        else:
            raise TypeError
        if isinstance(occupied_volume, (int, float)):
            if occupied_volume >= 0:
                if occupied_volume > capacity_volume:
                    raise ValueError("В стакан не может поместиться столько воды")
                self.occupied_volume = occupied_volume
            else:
                raise ValueError
        else:
            raise TypeError

    def get_self_id(self):
        """

        :return: возвращает 16-ричное представление id объекта
        """
        return hex(id(self)) # переводит в читабельный вид в 16-ричной системе


# 2. Создайте два и более объектов типа Glass
#    Измените и добавьте в любой стакан любое кол-во воды (через атрибуты)
#    Убедитесь, что у других объектов Glass атрибуты экземпляра класса не изменились.

print("+++++++++++++++++++ № 2 +++++++++++++++")

glass_2_1 = Glass(200, 100)
print(glass_2_1.capacity_volume) # экземпляр класса
print(glass_2_1.occupied_volume)

glass_2_2 = Glass(500, 50) # self - glass_2_2
print(glass_2_2.capacity_volume)
print(glass_2_2.occupied_volume)

#glass_2_3 = Glass(500, 700)
#print(glass_2_3.capacity_volume)
#print(glass_2_3.occupied_volume)

# 3. Создайте класс GlassDefaultArg (нужен только __init__) c аргументом occupied_volume
#    По умолчанию occupied_volume равен нулю. Создайте два объекта с 0 и 200
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)


class GlassDefaultArg:
    def __init__(self, capacity_volume, occupied_volume = 0):
        if isinstance(capacity_volume, (int, float)): # проверка сразу на int и на float
            if capacity_volume > 0: # проверка на неотрицательность
                self.capacity_volume = capacity_volume
            else:
                raise ValueError
        else:
            raise TypeError
        if isinstance(occupied_volume, (int, float)):
            if occupied_volume >= 0:
                if occupied_volume > capacity_volume:
                    raise ValueError("В стакан не может поместиться столько воды")
                self.occupied_volume = occupied_volume
            else:
                raise ValueError
        else:
            raise TypeError

print("+++++++++++++++++++ № 3 +++++++++++++++")

glass_3_1 = GlassDefaultArg(200)
print(glass_3_1.capacity_volume)
print(glass_3_1.occupied_volume)

glass_3_2 = GlassDefaultArg(200, 100)
print(glass_3_2.capacity_volume)
print(glass_3_2.occupied_volume)

# 4. Создайте класс GlassDefaultListArg (нужен только __init__) 
#    c аргументами capacity_volume, occupied_volume.
#    Пусть аргументом по умолчанию для __init__ occupied_volume = []. Будет список.
#    Попробуйте создать 3 объекта, которые изменяют occupied_volume.append(2) внутри __init__.
#    Создавайте объект GlassDefaultListArg только с одним аргументом capacity_volume.
#    Опишите результат.
#    Подсказка: можно ли использовать для аргументов по умолчанию изменяемые типы?
  
print("+++++++++++++++++++ № 4 +++++++++++++++")
'''
class GlassDefaultListArg:
    def __init__(self, capacity_volume, occupied_volume): # если там список - то это адрес. То попадет на одну и ту же ячейку памяти
        occupied_volume = []
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume
        self.occupied_volume.append(2)
'''
'''
В текущей реализации проблема в том, что передавая через аргумент occupied_volume  какое-либо значение, мы тут же
переменную occupied_volume перезаписываем на пустой список, который пройдя инициализацию получит значение [2].
И так каждый раз, что бы мы в occupied_volume не записывали
'''
'''
glass_4_1 = GlassDefaultListArg(200, 100)
print(glass_4_1.capacity_volume)
print(glass_4_1.occupied_volume)

glass_4_2 = GlassDefaultListArg(300, 100)
print(glass_4_2.occupied_volume)

glass_4_3 = GlassDefaultListArg(200, 200)
print(glass_4_3.occupied_volume)
'''

#Вариант, выдающий ошибку (в аргументе значение по умолчанию - изменяемый объект (список))

class GlassDefaultListArg:
    def __init__(self, capacity_volume, occupied_volume = [5,8,4]): # если там список - то это адрес. То попадет на одну и ту же ячейку памяти
        # в качестве параметров по умолчанию не стоит передавать изменяемые параметры.
        # если нужно использовать - то не в конструкторе
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume
        self.occupied_volume.append(2)

'''
В такой реализации occupied_volume список [5,8,4] находится в определенной ячейке памяти (адресе). При этом, интерпретатор
видит только значение 5 и ссылку на следующее значение. После инициализации и выполнения команды изменения значения по
умолчанию, в изначальный список по этому адресу будет добавлена [2]. Итого список поменялся и теперь он такой: [5,8,4,2].
Когда мы будем создавать очередной экземпляр объекта, то мы не создадим новый объект (не попадем в новую ячейку памяти),
а обратимся к уже имеющемуся по конкретному адресу [5,8,4,2] и после инициализации объекта добавим в конец списка еще [2].
И так будет каждый раз при создании экземпляра класса.

Собственно, подсказка из PyCharm:
Default argument values are evaluated only once at function definition time, which means that modifying the 
default value of the argument will affect all subsequent calls of the function
'''

glass_4_1 = GlassDefaultListArg(200)
print(glass_4_1.occupied_volume)

glass_4_2 = GlassDefaultListArg(300, [88, 105])
print(glass_4_2.occupied_volume)

glass_4_3 = GlassDefaultListArg(200)
print(glass_4_3.occupied_volume)

glass_4_4 = GlassDefaultListArg(500, [44, 32])
print(glass_4_4.occupied_volume)

glass_4_5 = GlassDefaultListArg(500, [44, 32])
print(glass_4_5.occupied_volume)

glass_4_6 = GlassDefaultListArg(200)
print(glass_4_6.occupied_volume)

# 5. Создайте класс GlassAddRemove, добавьте методы add_water, remove_water
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)
#    Вызовите методы add_water и remove.
#    Убедитесь, что методы правильно изменяют атрибут occupied_volume.

print("+++++++++++++++++++ № 5 +++++++++++++++")

class GlassAddRemove:
    def __init__(self, capacity_volume, occupied_volume = 0):
        if isinstance(capacity_volume, (int, float)): # проверка сразу на int и на float
            if capacity_volume > 0: # проверка на неотрицательность
                self.capacity_volume = capacity_volume
            else:
                raise ValueError
        else:
            raise TypeError
        if isinstance(occupied_volume, (int, float)):
            if occupied_volume >= 0:
                if occupied_volume > capacity_volume:
                    raise ValueError("В стакан столько не поместится")
                self.occupied_volume = occupied_volume
            else:
                raise ValueError
        else:
            raise TypeError

    def add_water(self, adding_water):
        """

        :param adding_water: количество добавляемой воды в стакан
        :return: # например, можно щдесь вывести излишек воды
        """
        space = self.capacity_volume - self.occupied_volume # оставшийся объем пустого места в стакане
        print("Путой объем в стакане: ", space)
        if space > adding_water:
            self.occupied_volume += adding_water
        else:
            self.occupied_volume = self.capacity_volume
            left = adding_water - space
            print(f"К сожалению, мы не смогли долить {left}")

    def remove_water(self, removing_water):
        if (self.occupied_volume - removing_water) < 0:
            raise ValueError("Нельзя вылить больше воды, чем есть в стакане")
        else:
            self.occupied_volume = self.occupied_volume - removing_water


glass_5_1 = GlassAddRemove(200, 50)
print(glass_5_1.occupied_volume)
glass_5_1.remove_water(30)
print(glass_5_1.occupied_volume)
glass_5_1.add_water(200)
print(glass_5_1.occupied_volume)
glass_5_1.remove_water(80)
print(glass_5_1.occupied_volume)
#glass_5_1.remove_water(130)
#print(glass_5_1.occupied_volume)
glass_5_2 = GlassAddRemove(300, 100)
glass_5_2.add_water(2000)
print(glass_5_2.occupied_volume)

# 6. Создайте три объекта типа GlassAddRemove, 
#    вызовите функцию dir для трёх объектов и для класса GlassAddRemove.
#    а. Получите типы объектов и класса
#    б. Проверьте тип созданного объекта.

print("+++++++++++++++++++ № 6 +++++++++++++++")

glass_6_1 = GlassAddRemove(200, 100)
print('тип объекта glass_6_1 класса GlassAddRemove: ', type(glass_6_1))
glass_6_2 = GlassAddRemove(500, 50)
print('тип объекта glass_6_2 класса GlassAddRemove: ', type(glass_6_2))
glass_6_3 = GlassAddRemove(100, 0)
print('тип объекта glass_6_3 класса GlassAddRemove: ', type(glass_6_3))

print('Тип класса GlassAddRemove: ', type(GlassAddRemove))
print('dir класса GlassAddRemove: ', dir(GlassAddRemove))
print('dir объекта glass_6_1 класса GlassAddRemove: ', dir(glass_6_1)) # выводит список build-in методов и аттрибутов и список пользовательских методов и аттрибутов
print('dir объекта glass_6_2 класса GlassAddRemove: ', dir(glass_6_2))
print('dir объекта glass_6_3 класса GlassAddRemove: ', dir(glass_6_3))
print(glass_6_1.__dict__) # выводит список пользовательских аттрибутов.
# ---------------------------------------------------------------------------------------------
# Внутренние объекты класса (стр. 25-33)

# 7. Получите список атрибутов экземпляра класса в начале метода __init__, 
#    в середине __init__ и в конце __init__, (стр. 28-30)
#    а также после создания объекта.
#    Опишите результат.

print("+++++++++++++++++++ № 7 +++++++++++++++")

class GlassDir:
    def __init__(self, capacity_volume, occupied_volume):
        print(dir(self)) # распечатает объект, с которым мы будем работать
        print(self.__dict__)  # распечатает список пользовательских атрибутов экземпляра класса

        self.capacity_volume = capacity_volume # момент появления атрибута capacity_volume при создании экземпляра класса
        print(dir(self))
        print(self.__dict__)

        self.occupied_volume = occupied_volume # момент появления атрибута occupied_volume при создании экземпляра класса
        print(dir(self))
        print(self.__dict__)

glass_7_1 = GlassDir(200, 100)


# 8. Создайте три объекта Glass. (стр. 27)
#    Получите id для каждого объекта с соответсвующим id переменной self.

print("+++++++++++++++++++ № 8 +++++++++++++++")

glass_8_1 = Glass(200, 100)
print(hex(id(glass_8_1)))
print(dir(glass_8_1))
print(glass_8_1.get_self_id())

glass_8_2 = Glass(300, 200)
print(hex(id(glass_8_2))) # эта и следующая строка - одно и то же
print(glass_8_2.get_self_id()) # то же, что и сверху

glass_8_3 = Glass(200, 100)
print(hex(id(glass_8_3)))
print(glass_8_3.get_self_id())

# 9. Корректно ли следующее объявление класса с точки зрения:
#     - интерпретатора Python;
#     - соглашения о стиле кодирования
#    Запустите код.

'''
С точки зрения интерпретатора - все в порядке
Нарушено соглашение о стиле. Название класса, должно быть с большой буквы, вместо f нужно self
'''

print("+++++++++++++++++++ № 9 +++++++++++++++")

class d:
    def __init__(f, a=2):
        f.a = a

    def print_me(p):
        print(p.a)
		
d.print_me(d())		

# 10. Исправьте
print("+++++++++++++++++++ № 10 +++++++++++++++")
class A:
    def __init__(self, a):
        if 10 < a < 50:
            #return #- было изначально
            raise ValueError("Значение атрибута должно быть либо меньше или равно 10, либо больше или равно 50")
        self.a = a

# a1 - выведет ошибку и не создаст экземпляр класса
#a1 = A(15)
#print(dir(a1))
a2 = A(55)
print(dir(a2))
# Объясните так реализовывать __init__ нельзя?
'''
Если мы поставим return в середине __init__, то если код дойдет до return - он создаст экземпляр класса и дальше по 
__init__ не пойдет. 
return можно использовать, если мы уверены, что экземпляр был правильно создан.
В текущем случае при указании атрибута от 10 до 50 будет создан экземпляр класса, однако атрибута 'a' у него не будет
'''

        
# 11. Циклическая зависимость (стр. 39-44)

print("+++++++++++++++++++ № 11 +++++++++++++++")

class Node:
    def __init__(self, prev=None, next_=None):
        self.__prev = prev
        self.__next = next_
        #TODO
        self.value = None
    def set_next(self, next_):
        self.__next = next_

    def set_prev(self, prev):
        self.__prev = prev

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.__value = value

    def __str__(self):
        return f"Node: {self.value}, Next node: {self.__next}, Previ"self.__next, self.value
        
    def __repr__(self):
        ...


class LinkedList:
    def __init__(self, nodes=None):
        if nodes is None:
            self.head = None
            self.tail = None
        elif isinstance(nodes, Node): # Один нод - можно не только типы проверять. Это будет значить, что тут один нод был передан
            self.head = nodes # указываем, что это тот же нод
            self.tail = nodes # указываем, что это тот же нод
        elif isinstance(nodes, list):
            self.head = nodes[0] # нужно обязательно проверять на вводимое значение (если там будут не только ноды - то должна быть ошибка)
            self.tail = nodes[-1]
            self.linked_nodes(nodes) # вязываем пользовательские ноды в порядке их подачи в списке

    # TODO нужно проверить, если будет список из одного элемента или из двух

    def linked_nodes(self, nodes):
        # установили ссылки для первого нода
        nodes[0].set_prev(nodes[-1])
        nodes[0].set_next(nodes[1])


        for i in range(1, len(nodes) - 1): # установили ссылки для остальных, кроме последнего
            nodes[i].set_prev(nodes[i - 1])
            nodes[i].set_next(nodes[i + 1])

        nodes[-1].set_prev(nodes[-2]) # установили ссылки для последнего нода
        nodes[-1].set_next(nodes[0])



    def insert(self, node, index=0):
        '''
        Insert Node to any place of LinkedList
        node - Node
        index - position of node
        '''
        ...
        
       
    def append(self, node):
        '''
        Append Node to tail of LinkedList
        node - Node
        '''
        self.tail.set_next(node)
        # сохраняем и запоминаем прошлый хвост
        #prev_tail = self.tail
        node.set_prev(self.tail)
        self.tail = node
        self.tail.set_next(self.head)
        self.head.set_prev(self.tail)


    def append_left(self, node):
        '''
        Append Node to tail of LinkedList
        node - Node
        '''
        # TODO - переделать
        self.head.set_prev(node)
        self.head = node
        self.head.set_next(self.head)

    def clear(self):
        '''
        Clear LinkedList
        '''
        ...

    def find(self, node):
        ...


    def remove(self, node):
        ...
        
    def delete(self, index):
        ...
























