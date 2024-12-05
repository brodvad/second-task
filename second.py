import sys
import random
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor


class CircleWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.diameter = 0
        self.x = 0
        self.y = 0
        self.draw_circle = False
        self.pushButton.clicked.connect(self.wow)

    def paintEvent(self, event):
        if self.draw_circle:
            painter = QPainter(self)
            painter.setBrush(QColor(255, 255, 0))
            painter.drawEllipse(self.x, self.y, self.diameter, self.diameter)

    def wow(self):
        self.diameter = random.randint(40, 370)
        self.x = random.randint(0, 700 - self.diameter)
        self.y = random.randint(0, 500 - self.diameter)
        self.draw_circle = True
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = CircleWidget()
    main_window.show()
    sys.exit(app.exec())



