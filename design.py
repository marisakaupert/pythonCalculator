# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(603, 544)
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
        self.calculationsVerticalLayout.addWidget(self.calculationsLineEdit)
        self.buttonsGridLayout = QtWidgets.QGridLayout()
        self.buttonsGridLayout.setObjectName("buttonsGridLayout")
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
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.historyLabel.setText(_translate("Dialog", "History:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

