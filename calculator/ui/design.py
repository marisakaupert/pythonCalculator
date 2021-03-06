# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.6


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(722, 544)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.overallHorizontalLayout = QtWidgets.QHBoxLayout()
        self.overallHorizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.overallHorizontalLayout.setObjectName("overallHorizontalLayout")
        self.calculationsVerticalLayout = QtWidgets.QVBoxLayout()
        self.calculationsVerticalLayout.setContentsMargins(5, 5, 5, 5)
        self.calculationsVerticalLayout.setObjectName("calculationsVerticalLayout")
        self.previousInputLineEdit = QtWidgets.QLineEdit(Dialog)
        self.previousInputLineEdit.setObjectName("previousInputLineEdit")
        self.previousInputLineEdit.setEnabled(False)
        self.previousInputLineEdit.setAlignment(QtCore.Qt.AlignRight)
        self.calculationsVerticalLayout.addWidget(self.previousInputLineEdit)
        self.calculationsLineEdit = QtWidgets.QLineEdit(Dialog)
        self.calculationsLineEdit.setObjectName("calculationsLineEdit")
        self.calculationsLineEdit.setEnabled(False)
        self.calculationsLineEdit.setText("0")
        self.calculationsLineEdit.setAlignment(QtCore.Qt.AlignRight)
        self.calculationsVerticalLayout.addWidget(self.calculationsLineEdit)
        self.uiHorizontalLayout = QtWidgets.QHBoxLayout()
        self.uiHorizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.uiHorizontalLayout.setObjectName("uiHorizontalLayout")
        self.clearPushButton = QtWidgets.QPushButton("CLEAR")
        self.uiHorizontalLayout.addWidget(self.clearPushButton)
        self.undoPushButton = QtWidgets.QPushButton("UNDO")
        self.uiHorizontalLayout.addWidget(self.undoPushButton)
        self.calculationsVerticalLayout.addLayout(self.uiHorizontalLayout)
        self.buttonsGridLayout = QtWidgets.QGridLayout()
        self.buttonsGridLayout.setObjectName("buttonsGridLayout")

        # buttons
        self.buttonsGroup = QtWidgets.QButtonGroup()
        cube = u'x\xb3'
        square = u'x\xb2'
        sqrt = u'\u221a'
        buttonsTextDict = {
            (0, 0): sqrt.encode('utf-8'),
            (0, 1): "7",
            (0, 2): "8",
            (0, 3): "9",
            (0, 4): "/",
            (1, 0): square.encode('utf-8'),
            (1, 1): "4",
            (1, 2): "5",
            (1, 3): "6",
            (1, 4): "X",
            (2, 0): cube.encode('utf-8'),
            (2, 1): "1",
            (2, 2): "2",
            (2, 3): "3",
            (2, 4): "-",
            (3, 0): "1/x",
            (3, 1): "(-)",
            (3, 2): "0",
            (3, 3): ".",
            (3, 4): "+"
        }

        for i in range(4):
            for j in range(5):
                self.mathButtons = QtWidgets.QPushButton()
                if (i, j) in buttonsTextDict.keys():
                    self.mathButtons.setText(
                        "{0}".format(buttonsTextDict[(i, j)]))

                if self.mathButtons.text().isdigit():
                    self.mathButtons.setObjectName('digitButtons')

                self.buttonsGroup.addButton(self.mathButtons)
                self.buttonsGridLayout.addWidget(self.mathButtons, i, j)

        self.calculationsVerticalLayout.addLayout(self.buttonsGridLayout)
        self.enterPushButton = QtWidgets.QPushButton("ENTER")
        self.calculationsVerticalLayout.addWidget(self.enterPushButton)
        self.overallHorizontalLayout.addLayout(self.calculationsVerticalLayout)
        self.historyVerticalLayout = QtWidgets.QVBoxLayout()
        self.historyVerticalLayout.setContentsMargins(50, 5, 5, 5)
        self.historyVerticalLayout.setObjectName("historyVerticalLayout")
        self.historyLabel = QtWidgets.QLabel(Dialog)
        self.historyLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.historyLabel.setObjectName("historyLabel")
        self.historyVerticalLayout.addWidget(self.historyLabel)
        self.historyListWidget = QtWidgets.QListWidget(Dialog)
        self.historyListWidget.setObjectName("historyListWidget")
        self.historyVerticalLayout.addWidget(self.historyListWidget)
        self.overallHorizontalLayout.addLayout(self.historyVerticalLayout)
        self.gridLayout.addLayout(self.overallHorizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Calculator"))
        self.historyLabel.setText(_translate("Dialog", "History:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

