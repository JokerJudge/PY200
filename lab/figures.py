import os
import math
import sys
# Подключаем модули QApplication и QLabel
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtGui import QPainter, QBrush
from PySide2.QtCore import Qt, QPoint
from abc import abstractmethod

class Figure:
    def __init__(self, x=0, y=0): # 3 - затем здесь - см. ниже 1 и 2
        self._x = x
        self._y = y

    @abstractmethod # обязательно в наследнике придется переопределить этот метод, иначе будет ошибка. Потомок не может их не иметь
    def perimeter(self):
        pass

    @abstractmethod
    def square(self):
        pass

    @property
    def width(self):
        return 0

    @property
    def height(self):
        return 0

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError
        self._y = y


    
class Rectangle(Figure):
    def __init__(self, x=0, y=0, w=0, h=0): #1 от пользователя
        # self.__x = x
        # self.__y = y
        super().__init__(x, y) # 2 x и y попадают сюда
        self.width = w # если width - есть как свойство в родителе - то это будет именно свойство, а не атрибут
        self.height = h

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError
        self._height = height

    @property
    def perimeter(self):
       return 2*(self.width +self.height)

    @property
    def square(self):
        return self.width *self.height

class Ellipse(Figure):
    def __init__(self, x=0, y=0, w=0, h=0):
        super().__init__(x, y)  # 2 x и y попадают сюда
        self.width = w  # если width - есть как свойство в родителе - то это будет именно свойство, а не атрибут
        self.height = h

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError
        self._height = height

    @property
    def perimeter(self):
        return 4 * ((math.pi * self.width / 2 * self.height / 2 + (self.width / 2 - self.height / 2)) / self.width / 2 + self.height / 2)

    @property
    def square(self):
        return math.pi * self.width / 2 * self.height / 2

class CloseFigure(Figure):
    def __init__(self, *args):
        d = []
        for c_x, c_y in args:
            temp = {"x": c_x, "y": c_y}
            d.append(temp)
        self.d = d # список словарей - пример: [{'x': 1, 'y': 2}, {'x': 5, 'y': 6}, {'x': 7, 'y': 4}]
                                                     
if __name__ == '__main__':

    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = 'C:\\Users\\Евгений\\AppData\\Local\\Programs\\Python\\Python37-32\\Lib\\site-packages\\PySide2\\plugins\\platforms'
    '''
    было ./platforms
    '''
    app = QApplication(sys.argv)
    figure_widget = FigureWidget()



	# Создайте список фигур
    figures = [Rectangle(20, 30, 400, 200), Rectangle(100, 300, 300, 50)]
	
    figure_widget.set_figures(figures)
	
    figure_widget.show()
    sys.exit(app.exec_())
