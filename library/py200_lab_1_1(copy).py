
# 11. Циклическая зависимость (стр. 39-44)

print("+++++++++++++++++++ № 11 +++++++++++++++")


from weakref import ref

class Node:
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
        return f"Node: {self.data}"


class LinkedList:
    def __init__(self, nodes=None):
        if nodes is None:
            self.head = None
            self.tail = None
        elif isinstance(nodes, Node):
            self.head = nodes # указываем, что это тот же нод
            self.tail = nodes # указываем, что это тот же нод
        elif isinstance(nodes, list):
            if len(nodes) == 0:
                self.head = None
                self.tail = None
            elif len(nodes) == 1:
                if not isinstance(nodes[0], Node):
                    raise TypeError("Передаваться должен Node или список из Node")
                self.head = nodes[0]
                self.tail = nodes[0]
            elif len(nodes) > 1:
                for i in nodes:
                    if not isinstance(i, Node):
                        raise TypeError("Передаваться должен Node или список из Node")
                self.head = nodes[0]
                self.tail = nodes[-1]
                self.linked_nodes(nodes) # связываем Node в порядке подачи в списке

        else:
            raise TypeError("Передаваться должен Node или список из Node")

    def __len__(self): # считаем количество Node в Linkedlist
        if self.head is None:
            return 0
        elif self.head == self.tail:
            return 1
        else:
            current_node = self.head
            current_node = current_node.next_
            index = 1 # счетчик
            while current_node != self.head:
                index += 1
                current_node = current_node.next_
            return index

    def __str__(self):
        l = []
        if self.head is None:
            return f"{l}"
        current_node = self.head
        for i in range(len(self)):
            l.append(current_node.data)
            current_node = current_node.next_
        return f"{l}"

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
        #находим нужный Node
        if not isinstance(node, Node):
            raise TypeError("В node был передан не Node")
        if index == 0:
            self.append_left(node)
        elif isinstance(index, int) and 0 < index < len(self): # проверяем, что в index записано число, и что это число не больше длины списка
            i = 0 # счетчик
            current_node = self.head
            while i != index:
                i += 1
                current_node = current_node.next_
            # устанавливаем связи, вставляя Node на нужное место
            current_node.prev().set_next(node)
            node.set_prev(current_node.prev())
            current_node.set_prev(node)
            node.set_next(current_node)
        else:
            raise ValueError("Такого количества Node нет в Linkedlist либо в index указано не число")

    def append(self, node):
        '''
        Добавляет node в конец Linked List
        :param node: Node
        :return:
        '''
        if not isinstance(node, Node):
            raise TypeError("В node был передан не Node")
        if self.head is None:
            self.head = node
            self.tail = node
        self.tail.set_next(node)
        node.set_prev(self.tail)
        self.tail = node
        self.tail.set_next(self.head)
        self.head.set_prev(self.tail)


    def append_left(self, node):
        '''
        Append Node to the beginning of LinkedList
        node - Node
        '''
        if not isinstance(node, Node):
            raise TypeError("В node был передан не Node")
        self.head.set_prev(node)
        node.set_next(self.head)
        self.head = node
        self.head.set_prev(self.tail)
        self.tail.set_next(self.head)

    def clear(self):
        '''
        Clear LinkedList
        '''
        # self.head.set_next(None)
        # self.head = None
        # self.tail = None

        del self.head.next_
        self.head = None


    def find(self, node):
        '''
        Поиск по Node
        :param node:
        :return: Если находит - возвращает индекс в списке, если не находит - None
        '''
        if not isinstance(node, Node):
            raise TypeError("В node был передан не Node")
        current_node = self.head
        for i in range(len(self)):
            if node == current_node:
                return i
            current_node = current_node.next_
        return None

    def remove(self, node):
        '''
        Удаление по Node
        :param node:
        :return:
        '''
        if not isinstance(node, Node):
            raise TypeError("В node был передан не Node")
        current_node = self.head
        for i in range(len(self)):
            if node == current_node:
                current_node.prev().set_next(current_node.next_)
                current_node.next_.set_prev(current_node.prev())
                return
            current_node = current_node.next_
        print(f"{node} не был найден в {self}")

        
    def delete(self, index):
        """
        Удаление node по индексу
        :param index: индекс нода
        :return:
        """
        if not isinstance(index, int):
            raise TypeError("Индекс должен быть числом")
        if 0 < index < len(self):
            current_node = self.head
            for i in range(len(self)):
                if index == i:
                    current_node.prev().set_next(current_node.next_)
                    current_node.next_.set_prev(current_node.prev())
                    return
                current_node = current_node.next_
        else:
            raise ValueError("Индекс за пределами возможных значений")


if __name__ == "__main__":
    # создадим 8 экземпляров Node
    a1 = Node(data=10)
    a2 = Node(data=35)
    a3 = Node(data=75)
    a4 = Node(data=115)
    a5 = Node(data=5)
    a6 = Node(data=125)
    a7 = Node(data=53)
    a8 = Node(data=143)

    # создадим 2 двусвязных списка
    l1 = LinkedList(a1)
    l2 = LinkedList([a1, a2, a3])

    l2.append(a4) # добавим в список а4
    l2.append_left(a5) # добавим а5 в начало списка
    l2.append(a6) # добавим в конец а6
    print(l2)
    print(len(l2))
    print(l2.tail.prev().data)
    l2.insert(a7, index=2) # вставим на место a2 (индекс 2) вставим a7. Теперь последовательность a5 - a1 - a7 - a2 - a3 - a4 - a6
    print(l2.head.next_.next_.data) # удостоверимся, что третьим с начала элементом будет a7
    print("Длина списка l2: ", len(l2)) # проверим работу __len__ - должно быть 7
    print(l2) # смотрим на область памяти списка l2
    l2.clear() # очищение списка
    print(l2) # проверяем, что это тот же список
    print(l2.head) # должно быть None
    print(l2.tail) # должно быть None
    print(len(l2)) # длина должна быть 0
    print("------------------------")
    l2.append(a1) # добавим новый элемент в пустой список
    print(l2.head) # head и tail должны быть одинаковыми
    print(l2.head.next_) # переходит сам на себя.
    print(len(l2)) # длина должна быть 1
    print("------------------------")

    l3 = LinkedList([a1, a2, a3, a4, a5, a6, a7]) # создаем новый список
    print("Индекс искомого элемента: ", l3.find(a5)) # проверяем работу метода find
    print("Индекс искомого элемента: ", l3.find(a8))  # проверяем работу метода find
    l3.remove(a8) # попытка удалить отсутствующий Node
    print("Длина списка до удаления: ", len(l3))
    l3.remove(a2)
    print("Длина списка после удаления: ", len(l3))
    print("Индекс Node a3: ", l3.find(a3))
    print("Индекс Node a2: ", l3.find(a2))
    print("Длина списка до удаления: ", len(l3))
    l3.delete(1)
    print("Длина списка после удаления: ", len(l3))
    print("Индекс Node a3: ", l3.find(a3))
    print("Индекс Node a6: ", l3.find(a6))














