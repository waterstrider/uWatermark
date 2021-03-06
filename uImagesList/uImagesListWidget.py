__author__ = 'waterstrider.vin'

from PySide.QtGui import *
from PySide.QtCore import *

from uPushButton.uPushButtonWidget import UPushButtonWidget
from uImagesList.uThumbnailDetailDelegate import UThumbnailDetailDelegate
from uImagesList.uThumbnailDetailItem import UThumbnailDetailItem
from uImagesList.uThumbnailDetailModel import UThumbnailDetailModel


class UImagesListWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.gridLayout = QGridLayout(self)
        self.addButton = UPushButtonWidget(self, "add", "+")
        self.gridLayout.addWidget(self.addButton, 1, 0, 1, 1)

        self.removeButton = UPushButtonWidget(self, "remove", "-")

        self.gridLayout.addWidget(self.removeButton, 1, 1, 1, 1)

        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)

        self.uImageList = QListWidget()

        self.scrollArea.setWidget(self.uImageList)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 2)

        self.addImage("Resources/Sample Image/sample01.jpg")
        self.addImage("Resources/Sample Image/sample02.jpg")
        self.addImage("Resources/Sample Image/sample03.jpg")
        self.addImage("Resources/Sample Image/sample02.jpg")
        self.addImage("Resources/Sample Image/sample03.jpg")
        self.addImage("Resources/Sample Image/sample01.jpg")

        QObject.connect(self.addButton.pushButton, SIGNAL("clicked()"), self.addButtonActionListener)
        QObject.connect(self.removeButton.pushButton, SIGNAL("clicked()"), self.removeButtonActionListener)


    def addButtonActionListener(self):
        filepath = QFileDialog.getOpenFileName(self)[0]
        if filepath != '':
            self.addImage(filepath)


    def removeButtonActionListener(self):
        self.removeImage()


    def addImage(self, filepath):
        item = UThumbnailDetailItem(filepath)
        self.uImageList.addItem(item)
        self.uImageList.setItemWidget(item, item.thumbnailWidget)

    def removeImage(self):
        items = self.uImageList.selectedItems()
        for item in items:
            self.uImageList.takeItem(self.uImageList.row(item))

    def updateScreen(self):
        pass