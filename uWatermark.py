__author__ = 'waterstrider.vin'

from PySide.QtGui import *

from uCentralWidget import UCentralWidget


class UWatermark(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.actionExit = QAction(self)
        self.centralwidget = UCentralWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(self)

        self.menuFile = QMenu(self.menubar)

        self.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(self)

        self.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionExit)