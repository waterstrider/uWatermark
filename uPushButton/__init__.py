__author__ = 'waterstrider.vin'

from sys import argv

from PySide.QtGui import QApplication

from uPushButton.uPushButtonWidget import UPushButtonWidget


if __name__ == "__main__":
    app = QApplication(argv)
    uPushButtonWidget = UPushButtonWidget()
    uPushButtonWidget.show()
    app.exec_()