import sys
from design import Ui_Dialog
from arithmaticFunctions import MainFunctions
from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        QtGui.QFontDatabase.addApplicationFont("fonts/Montserrat-Regular.ttf")
        QtGui.QFontDatabase.addApplicationFont("fonts/Montserrat-Bold.ttf")
        sshFile = "stylesheet.qss"
        with open(sshFile, "r") as fh:
            self.setStyleSheet(fh.read())
        self.makeConnections()

    def makeConnections(self):
        # digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # for num in digits:
        #     if self.
        # self.createGeometryPushButton.clicked.connect(self.printDigits)
        # self.createGeometryPushButton.clicked.connect(self.doMath)
        pass


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
