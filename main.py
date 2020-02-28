'''
делаем фабрику, кот. будет предоставлять возможность от пользователя выбрать builder
Мы вызываем у builderа соответствующий метод и он строит нам драйвер
Мы делаем список. Его заполняем. Передаем их в драйвер, который нам запишет всё в json

'''
from weakref import ref
from structure_driver import *


class LinkedList:

    class Node:
        def __init__(self, prev_node=None, next_node=None, data=None):

            if prev_node is not None and not isinstance(prev_node, type(self)):
                raise TypeError('prev_node must be Node or None')

            if next_node is not None and not isinstance(next_node, type(self)):
                raise TypeError('next_node must be Node or None')

            self.prev_node_ = ref(prev_node) if prev_node is not None else None
            self.next_node_ = next_node
            self.data = data

        @property
        def prev_node(self):
            return self.prev_node_() if self.prev_node_ is not None else None

        @prev_node.setter
        def prev_node(self, value):
            if value is not None and not isinstance(value, type(self)):
                raise TypeError('Value must be Node or None')
            self.prev_node_ = ref(value) if value is not None else None

        @property
        def next_node(self):
            return self.next_node_

        @next_node.setter
        def next_node(self, value):
            if value is not None and not isinstance(value, type(self)):
                raise TypeError('Value must be Node or None')
            self.next_node_ = value

        def __str__(self):
            return self.data

    def __init__(self, structure_driver=None):
        self.size = 0
        self.head = self.Node()
        self.tail = self.Node(self.head)
        self.head.next_node = self.head
        self.__structure_driver = structure_driver
        self.__structure_driver = None # то же самое, что и строчка сверху

    def insert_next_node(self, current_node, data):
        new_node = self.Node(current_node, current_node.next_node, data)
        current_node.next_node.prev_node = new_node
        current_node.next_node = new_node
        self.size += 1

    def insert_node(self, index, data):
        if not isinstance(index, int):
            raise TypeError('index must be int')

        if index >= 0:
            if not 0 <= index <= self.size:
                raise ValueError('Invalid index')
            current_node = self.head.next_node
            for _ in range(self.size):
                current_node = current_node.next_node

            self.insert_next_node(current_node, data)

    def to_dict(self):
        d = {}
        i = 0
        current_node = self.head.next_node
        while i < self.size:
            d[i] = current_node.data # первая нода будет нулевая.
            i += 1
            current_node = current_node.next_node
        return d

    def from_dict(self, d):
        for index, value in d.items():
            self.insert_node(index, value)
        print(self.to_dict())

    def load(self):
        self.from_dict(self.__structure_driver.read())
        # из Istructuredriver должен прочитать и перевести в питоновский словарь

    def save(self):
        self.__structure_driver.write(self.to_dict())
        # взять питоновский словарь и запихать его в Istructuredriver

    def set_structure_driver(self, driver):
        self.__structure_driver = driver


class SDBuilder:

    def build(self):
        return None

    def __str__(self):
        return self.__class__.__name__


class JSONFileBuilder(SDBuilder):

    def build(self):
        filename = input('Enter filename (.json)>')
        return JSONFileDriver(filename)


class JSONStrBuilder(SDBuilder):
    def build(self):
        return JSONStringDriver()


class PickleBuilder(SDBuilder):
    def build(self):
        filename = input('Enter filename (.bin)>')
        return PickleDriver(filename)

class SDFabric:
    def get_sd_driver(self, driver_name):
        builders = {'json': JSONFileBuilder, # создается ссылка на класс
                    'json_str': JSONStrBuilder,
                    'pickle': PickleBuilder}
        try:
            return builders[driver_name]() # построится объект билдера
        except:
            return SDBuilder()

if __name__ == "__main__":
    l1 = LinkedList()

    l1.insert_node(0, 'Привет')
    l1.insert_node(1, 'Python')
    l1.insert_node(2, 'Hello')

    driver_name = input("Введите название драйвера > ")
    driver_builder = SDFabric().get_sd_driver(driver_name)  # если мы запускаем через staticmethod, можно скобки в SDFabric убрать
    #print(l1.to_dict())
    #print(l1.from_dict(l1.to_dict()))
    #print(driver_builder)
    l1.set_structure_driver(driver_builder.build())
    l1.save()
    # l2 = LinkedList()
    # driver_name = input("Введите название драйвера > ")
    # driver_builder = SDFabric().get_sd_driver(driver_name)
    # l2.set_structure_driver(driver_builder.build())
    # l2.load()

    #ll.set_structure_driver(JSONFileDriver("test.json"))
    #ll.save()