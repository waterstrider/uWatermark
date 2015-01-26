__author__ = 'waterstrider.vin'

from PySide.QtGui import *


class UImageViewer(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.gridLayout = QGridLayout(self)

        self.label = QLabel(self)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 5)

        self.rotateLeftButton = QPushButton(self)
        self.gridLayout.addWidget(self.rotateLeftButton, 1, 0, 1, 1)

        self.rotateRightButton = QPushButton(self)
        self.gridLayout.addWidget(self.rotateRightButton, 1, 1, 1, 1)

        self.cropButton = QPushButton(self)
        self.gridLayout.addWidget(self.cropButton, 1, 2, 1, 1)

        self.effectsButton = QPushButton(self)
        self.gridLayout.addWidget(self.effectsButton, 1, 3, 1, 1)

        self.optionsButton = QPushButton(self)
        self.gridLayout.addWidget(self.optionsButton, 1, 4, 1, 1)

