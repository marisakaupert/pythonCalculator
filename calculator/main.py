import sys
from ui.design import Ui_Dialog
from arithmaticFunctions import MainFunctions
from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        QtGui.QFontDatabase.addApplicationFont("fonts/Montserrat-Regular.ttf")
        QtGui.QFontDatabase.addApplicationFont("fonts/Montserrat-Bold.ttf")
        sshFile = "stylesheet/stylesheet.qss"
        with open(sshFile, "r") as fh:
            self.setStyleSheet(fh.read())
        self.makeConnections()

    def makeConnections(self):
        self.buttonsGroup.buttonClicked.connect(self.printDigits)

    def printDigits(self, button):
        currentLine = self.calculationsLineEdit.text()
        limit = len(self.calculationsLineEdit.text())
        if button.text().isdigit() and limit < 16:
            if currentLine == "0":
                self.calculationsLineEdit.setText(button.text())
            else:
                self.calculationsLineEdit.setText(currentLine + button.text())


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
