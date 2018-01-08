import sys
from design import Ui_Dialog
from arithmaticFunctions import MainFunctions
from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setStyleSheet("""
            QDialog {
                background-color: #b6b6b6;
            }
            QPushButton {
                border: none;
                background-color: #d3d3d3;
                font-size: 16px;
                min-width: 150px;
                min-height: 80px;
                font-family: monotype;
            }
            QPushButton#zeroPushButton, QPushButton#onePushButton,
            QPushButton#twoPushButton, QPushButton#threePushButton,
            QPushButton#fourPushButton, QPushButton#fivePushButton,
            QPushButton#sixPushButton, QPushButton#sevenPushButton,
            QPushButton#eightPushButton, QPushButton#ninePushButton {
                background-color: #f1f1f1;
                font-weight: bold;
            }
            QLineEdit {
                font-size: 35px;
                padding: 10px;
                border: none;
                background-color: #b6b6b6;
            }
            QLabel {
                font-size: 15px;
            }
            QListWidget {
                min-width: 300px;
                min-height: 100px;
                background-color: #b6b6b6;
                border: none;
            }
        """)
        self.makeConnections()

    def makeConnections(self):
        pass


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
