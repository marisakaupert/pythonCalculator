import sys
import math
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
        self.expression = []
        self.error = False
        self.makeConnections()

    def makeConnections(self):
        self.clearPushButton.clicked.connect(self.clearLine)
        self.undoPushButton.clicked.connect(self.undoLastAction)
        self.buttonsGroup.buttonClicked.connect(self.printDigits)
        self.buttonsGroup.buttonClicked.connect(self.makeDecimal)
        self.buttonsGroup.buttonClicked.connect(self.negateNumbers)
        self.buttonsGroup.buttonClicked.connect(self.setMathmaticalExpression)
        self.enterPushButton.clicked.connect(self.getAnswer)
        self.toggleNegative()
        self.buttonsGroup.buttonClicked.connect(self.squareRoot)
        self.buttonsGroup.buttonClicked.connect(self.powerOfTwo)
        self.buttonsGroup.buttonClicked.connect(self.cube)
        self.buttonsGroup.buttonClicked.connect(self.inverse)

    def clearLine(self):
        self.calculationsLineEdit.clear()
        self.calculationsLineEdit.setText("0")
        self.resetError()
        self.toggleNegative()

    def undoLastAction(self):
        line = self.calculationsLineEdit.text()
        self.calculationsLineEdit.setText(line[:-1])
        if len(line) < 2:
            self.calculationsLineEdit.setText("0")
        self.toggleNegative()

    def handleError(self):
        self.calculationsLineEdit.setText("Invalid Input")
        self.error = True
        self.toggleNonDigitButtons()
        self.enterPushButton.setEnabled(False)
        self.undoPushButton.setEnabled(False)

    def resetError(self):
        if self.error is True:
            self.calculationsLineEdit.clear()
            self.calculationsLineEdit.setText("0")
            self.expression = []
            self.error = False
            self.enterPushButton.setEnabled(True)
            self.undoPushButton.setEnabled(True)
            self.toggleNonDigitButtons()

    def printDigits(self, button):
        self.resetError()
        currentLine = self.calculationsLineEdit.text()
        limit = len(self.calculationsLineEdit.text())
        if button.text().isdigit() and limit < 15:
            if currentLine == "0":
                self.calculationsLineEdit.setText(button.text())
            else:
                self.calculationsLineEdit.setText(currentLine + button.text())
        self.toggleNegative()

    def toggleNegative(self):
        validNegative = self.calculationsLineEdit.text()
        for button in self.buttonsGroup.buttons():
            if button.text() == "(-)":
                if validNegative == "0" or self.error is True:
                    button.setEnabled(False)
                else:
                    button.setEnabled(True)

    def makeDecimal(self, button):
        convertToFloat = self.calculationsLineEdit.text()
        if button.text() == "." and "." not in convertToFloat:
            self.calculationsLineEdit.setText(convertToFloat + ".")

    def negateNumbers(self, button):
        currentNum = self.calculationsLineEdit.text()
        if button.text() == "(-)" and currentNum != "0":
            if "-" in currentNum:
                positiveNum = currentNum.replace("-", "")
                self.calculationsLineEdit.setText(positiveNum)
            else:
                self.calculationsLineEdit.setText("-" + currentNum)

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
        self.toggleNegative()

    def getAnswer(self):
        if len(self.expression) > 1:
            self.expression.append(self.calculationsLineEdit.text())
            combinedExpr = "".join(self.expression)
            try:
                self.result = str(eval(combinedExpr))
                self.calculationsLineEdit.setText(self.result)
                self.addHistory()
            except ZeroDivisionError:
                self.handleError()
        self.toggleNegative()

    def toggleNonDigitButtons(self):
        for button in self.buttonsGroup.buttons():
            if not button.text().isdigit():
                if self.error is True:
                    button.setEnabled(False)
                else:
                    button.setEnabled(True)

    def addHistory(self):
        formattedExpr = " ".join(self.expression)
        formattedExpr = formattedExpr.replace("*", "x")
        item = QtWidgets.QListWidgetItem(formattedExpr + " = " + self.result)
        item.setTextAlignment(QtCore.Qt.AlignRight)
        self.historyListWidget.addItem(item)
        self.resetHistoryAfterAdding()

    def resetHistoryAfterAdding(self):
        self.expression = []
        self.calculationsLineEdit.setText("0")

    def squareRoot(self, button):
        currentNum = self.calculationsLineEdit.text()
        if button.text() == u'\u221a':
            sqrtResult = math.sqrt(float(currentNum))
            self.calculationsLineEdit.setText(str(sqrtResult))

    def powerOfTwo(self, button):
        currentNum = self.calculationsLineEdit.text()
        if button.text() == u'x\xb2':
            powerOfTwoResult = math.pow(float(currentNum), 2)
            self.calculationsLineEdit.setText(str(powerOfTwoResult))

    def cube(self, button):
        currentNum = self.calculationsLineEdit.text()
        if button.text() == u'x\xb3':
            cubeResult = math.pow(float(currentNum), 3)
            self.calculationsLineEdit.setText(str(cubeResult))

    def inverse(self, button):
        currentNum = self.calculationsLineEdit.text()
        if button.text() == "1/x":
            try:
                inverseResult = 1 / float(currentNum)
                self.calculationsLineEdit.setText(str(inverseResult))
            except ZeroDivisionError:
                self.handleError()



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
