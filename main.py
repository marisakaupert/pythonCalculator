import sys
import os
from design import Ui_Dialog
from arithmaticFunctions import MainFunctions
from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setStyleSheet("""
            QPushButton {
                border: none;
                background-color: #8f8f91;
                font-size: 16px;
            }

            QLineEdit {
                font-size: 35 px;
                margin: 10px;
            }

            QLabel {
                font-size: 11px;
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
