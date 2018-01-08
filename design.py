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
        self.calculationsLineEdit = QtWidgets.QLineEdit(Dialog)
        self.calculationsLineEdit.setObjectName("calculationsLineEdit")
        self.calculationsLineEdit.setEnabled(False)
        self.calculationsVerticalLayout.addWidget(self.calculationsLineEdit)
        self.buttonsGridLayout = QtWidgets.QGridLayout()
        self.buttonsGridLayout.setObjectName("buttonsGridLayout")

        # buttons
        self.buttonGroup = QtWidgets.QButtonGroup()
        buttonTextDict = {
            0: "+",
            1: "6",
            2: "9",
            3: "-",
            4: "x" + u'\xb3',
            5: "1",
            6: "5",
            7: "3",
            8: "8",
            9: "UNDO",
            10: "X",
            11: "/",
            12: "2",
            13: "%",
            14: "x" + u'\xb2',
            15: "CLEAR",
            16: "7",
            17: "4",
            18: u'\u221a',
            19: "0",
            10: "(-)",
            11: ".",
            12: "ENTER",
            13: "1/x"
        }

        for i in range(6):
            for j in range(4):
                self.pressableButtons = QtWidgets.QPushButton()

                self.buttonGroup.addButton(self.pressableButtons)
                self.buttonsGridLayout.addWidget(self.pressableButtons, i, j)

        # end of buttons
        self.calculationsVerticalLayout.addLayout(self.buttonsGridLayout)
        self.overallHorizontalLayout.addLayout(self.calculationsVerticalLayout)
        self.historyVerticalLayout = QtWidgets.QVBoxLayout()
        self.historyVerticalLayout.setContentsMargins(5, 5, 5, 5)
        self.historyVerticalLayout.setObjectName("historyVerticalLayout")
        self.historyLabel = QtWidgets.QLabel(Dialog)
        self.historyLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.historyLabel.setObjectName("historyLabel")
        self.historyVerticalLayout.addWidget(self.historyLabel)
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setObjectName("listWidget")
        self.historyVerticalLayout.addWidget(self.listWidget)
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

