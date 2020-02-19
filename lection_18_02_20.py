class Color:
    def __init__(self, *args):
        if len(args) > 3:
            raise TypeError()
        if len(args) == 0:
            r = 0
            g = 0
            b = 0
        if len(args) == 1 and isinstance(args[0], str):
            value = args[0].split("x")[1]
            r = int(value[0:2], 16)
            g = int(value[2:4], 16)
            b = int(value[4:8], 16)
        if len(args) == 3:
            for i in args:
                if not isinstance(i, int):
                    raise TypeError()
                if not 0 <= i < 256:
                    raise ValueError()
            r = args[0]
            g = args[1]
            b = args[2]


        self.__r = r
        self.__g = g
        self.__b = b

    def __add__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError()
        r = min((self.__r + other.__r), 255))
        return Color()


        print(r, g, b)

c = Color()
c1 = Color("0xFF0203")



'''    
        c1 = Color(100, 200, 50)
        c2 = Color(50, 10, 100)
        c3 = c1 + c2 #c3 - новый объект. Мы при сложении должны получить новый объект
        c3 = c1 - c2 #c3 - новый объект, r g b не меньше 0
'''