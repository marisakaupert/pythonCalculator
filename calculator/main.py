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
        self.expression = []

    def makeConnections(self):
        self.clearPushButton.clicked.connect(self.clearLine)
        self.undoPushButton.clicked.connect(self.undoLastAction)
        self.buttonsGroup.buttonClicked.connect(self.printDigits)
        self.buttonsGroup.buttonClicked.connect(self.makeDecimal)
        self.buttonsGroup.buttonClicked.connect(self.negateNumbers)
        self.buttonsGroup.buttonClicked.connect(self.setMathmaticalExpression)
        self.enterPushButton.clicked.connect(self.getAnswer)

    def clearLine(self):
        self.calculationsLineEdit.clear()
        self.calculationsLineEdit.setText("0")

    def undoLastAction(self):
        line = self.calculationsLineEdit.text()
        self.calculationsLineEdit.setText(line[:-1])
        if len(line) < 2:
            self.calculationsLineEdit.setText("0")

    def printDigits(self, button):
        currentLine = self.calculationsLineEdit.text()
        limit = len(self.calculationsLineEdit.text())
        if button.text().isdigit() and limit < 15:
            if currentLine == "0":
                self.calculationsLineEdit.setText(button.text())
            else:
                self.calculationsLineEdit.setText(currentLine + button.text())

    def makeDecimal(self, button):
        convertToFloat = self.calculationsLineEdit.text()
        if button.text() == "." and "." not in convertToFloat:
            self.calculationsLineEdit.setText(convertToFloat + ".")

    def negateNumbers(self, button):
        currentNum = self.calculationsLineEdit.text()
        if button.text() == "(-)" and "-" not in currentNum:
            self.calculationsLineEdit.setText("-" + currentNum)

        if button.text() == "(-)" and "-" in currentNum:
            positiveNum = currentNum.replace("-", "")
            self.calculationsLineEdit.setText(positiveNum)

    def setMathmaticalExpression(self, button):
        mathFunctions = ["+", "-", "X", "/"]
        currentLine = self.calculationsLineEdit.text()
        if button.text() in mathFunctions:
            self.expression.append(currentLine)
            if button.text() == "X":
                self.expression.append("*")
            else:
                self.expression.append(button.text())
            self.calculationsLineEdit.setText("0")

    def getAnswer(self):
        self.expression.append(self.calculationsLineEdit.text())
        combinedExpr = "".join(self.expression)
        self.result = str(eval(combinedExpr))
        self.calculationsLineEdit.setText(self.result)
        self.addHistory()

    def addHistory(self):
        formattedExpr = " ".join(self.expression)
        formattedExpr = formattedExpr.replace("*", "x")
        item = QtWidgets.QListWidgetItem(formattedExpr + " = " + self.result)
        item.setTextAlignment(QtCore.Qt.AlignRight)
        if self.calculationsLineEdit.text() == "0":
            pass
        else:
            self.historyListWidget.addItem(item)
        self.clearHistory()

    def clearHistory(self):
        self.expression = []
        self.calculationsLineEdit.setText("0")


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
