import os

import sys
# Подключаем модули QApplication и QLabel
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtGui import QPainter, QBrush
from PySide2.QtCore import Qt, QPoint

from figures import Figure, Rectangle, Ellipse, CloseFigure

class FigureWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # super - вызываем __init__ из QWidget(предок\родитель). Аналог self на класс предка
        self.setWindowTitle('Рисовалка фигур')
        self.__figures = []

    def set_figures(self, figures): # передаем фигуры
        self.__figures = figures # записываем в private переменную

    def paintEvent(self, event): # c нуля перезаписываем paintEvent, который есть в родителе

        painter = QPainter(self)
        reset_brush = painter.brush()

        for figure in self.__figures:
            if not isinstance(figure, Figure):
                continue

            if isinstance(figure, Rectangle):
                painter.setBrush(QBrush(Qt.red))
                painter.drawRect(figure.x, figure.y, figure.width, figure.height) # не нужны круглые скобки, так как это свойства (property)
                continue

            if isinstance(figure, Ellipse):
                painter.setBrush(QBrush(Qt.green))
                painter.drawEllipse(figure.x, figure.y, figure.width, figure.height)
                continue

            if isinstance(figure, CloseFigure):
                painter.setBrush(QBrush(Qt.blue))
                # моя кривая попытка на паре
                #for i in range(len(figure._args)//4):
                #    painter.drawLine(figure.x1, figure.y1, figure.x2, figure.x2)


                points = [] # точки, которые будем передавать в drawPolygon
                # d - это список. Каждый поинт - отдельный дикт
                for point in figure.d:
                    points.append(QPoint(point['x'], point['y']))
                painter.drawPolygon(points)
                continue


if __name__ == '__main__':
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = './platforms'
    app = QApplication(sys.argv)
    figure_widget = FigureWidget()

    # Создайте список фигур
    figures = [Rectangle(20, 30, 400, 200), Rectangle(100, 300, 300, 50),
               Ellipse(100, 400, 250, 80), CloseFigure(12, 21, 15, 76)]
    #figures = []

    figure_widget.set_figures(figures)

    figure_widget.show()
    sys.exit(app.exec_())