# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\N_modules_Window_2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NModulesWindow2(object):
    def setupUi(self, NModulesWindow2):
        NModulesWindow2.setObjectName("NModulesWindow2")
        NModulesWindow2.resize(397, 312)
        NModulesWindow2.setStyleSheet("background-color: white")
        self.frame = QtWidgets.QFrame(NModulesWindow2)
        self.frame.setGeometry(QtCore.QRect(0, 20, 401, 291))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color: white")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_input = QtWidgets.QLabel(self.frame)
        self.label_input.setGeometry(QtCore.QRect(10, 10, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_input.setFont(font)
        self.label_input.setStyleSheet("")
        self.label_input.setAlignment(QtCore.Qt.AlignCenter)
        self.label_input.setObjectName("label_input")
        self.line_n1 = QtWidgets.QLineEdit(self.frame)
        self.line_n1.setGeometry(QtCore.QRect(20, 70, 161, 22))
        self.line_n1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.line_n1.setStyleSheet("background-color: #00D5FF;")
        self.line_n1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.line_n1.setObjectName("line_n1")
        self.line_n2 = QtWidgets.QLineEdit(self.frame)
        self.line_n2.setEnabled(False)
        self.line_n2.setGeometry(QtCore.QRect(240, 70, 141, 22))
        self.line_n2.setStyleSheet("background-color: #00D5FF;")
        self.line_n2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.line_n2.setObjectName("line_n2")
        self.operations = QtWidgets.QComboBox(self.frame)
        self.operations.setGeometry(QtCore.QRect(60, 160, 281, 31))
        self.operations.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.operations.setStyleSheet("background-color: #00D5FF;")
        self.operations.setObjectName("operations")
        self.operations.addItem("")
        self.operations.addItem("")
        self.operations.addItem("")
        self.operations.addItem("")
        self.operations.addItem("")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 110, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 200, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.result = QtWidgets.QLabel(self.frame)
        self.result.setGeometry(QtCore.QRect(10, 240, 371, 31))
        self.result.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.result.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.result.setStyleSheet("background-color: #00D5FF;")
        self.result.setFrameShape(QtWidgets.QFrame.Box)
        self.result.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.result.setObjectName("result")
        self.combo_d = QtWidgets.QComboBox(self.frame)
        self.combo_d.setEnabled(False)
        self.combo_d.setGeometry(QtCore.QRect(190, 70, 41, 22))
        self.combo_d.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.combo_d.setStyleSheet("background-color: #00D5FF;")
        self.combo_d.setObjectName("combo_d")
        self.combo_d.addItem("")
        self.combo_d.addItem("")
        self.combo_d.addItem("")
        self.combo_d.addItem("")
        self.combo_d.addItem("")
        self.combo_d.addItem("")
        self.combo_d.addItem("")
        self.combo_d.addItem("")
        self.combo_d.addItem("")
        self.combo_d.addItem("")
        self.pushButton_return = QtWidgets.QToolButton(NModulesWindow2)
        self.pushButton_return.setGeometry(QtCore.QRect(0, 0, 51, 22))
        self.pushButton_return.setStyleSheet("color: #00D5FF")
        self.pushButton_return.setObjectName("pushButton_return")

        self.retranslateUi(NModulesWindow2)
        QtCore.QMetaObject.connectSlotsByName(NModulesWindow2)

    def retranslateUi(self, NModulesWindow2):
        _translate = QtCore.QCoreApplication.translate
        NModulesWindow2.setWindowTitle(_translate("NModulesWindow2", "Прочие действия"))
        self.label_input.setText(_translate("NModulesWindow2", "Введите натуральное число:"))
        self.line_n1.setText(_translate("NModulesWindow2", "0"))
        self.line_n2.setText(_translate("NModulesWindow2", "0"))
        self.operations.setItemText(0, _translate("NModulesWindow2", "Проверка на 0"))
        self.operations.setItemText(1, _translate("NModulesWindow2", "Добавление 1"))
        self.operations.setItemText(2, _translate("NModulesWindow2", "Умножение числа на цифру"))
        self.operations.setItemText(3, _translate("NModulesWindow2", "Умножение на 10^k"))
        self.operations.setItemText(4, _translate("NModulesWindow2", "Вычитание из одного числа k других чисел (n1 - k*n2) "))
        self.label.setText(_translate("NModulesWindow2", "Выберите действие:"))
        self.label_2.setText(_translate("NModulesWindow2", "Результат:"))
        self.result.setText(_translate("NModulesWindow2", "0"))
        self.combo_d.setItemText(0, _translate("NModulesWindow2", "0"))
        self.combo_d.setItemText(1, _translate("NModulesWindow2", "1"))
        self.combo_d.setItemText(2, _translate("NModulesWindow2", "2"))
        self.combo_d.setItemText(3, _translate("NModulesWindow2", "3"))
        self.combo_d.setItemText(4, _translate("NModulesWindow2", "4"))
        self.combo_d.setItemText(5, _translate("NModulesWindow2", "5"))
        self.combo_d.setItemText(6, _translate("NModulesWindow2", "6"))
        self.combo_d.setItemText(7, _translate("NModulesWindow2", "7"))
        self.combo_d.setItemText(8, _translate("NModulesWindow2", "8"))
        self.combo_d.setItemText(9, _translate("NModulesWindow2", "9"))
        self.pushButton_return.setText(_translate("NModulesWindow2", "<-"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NModulesWindow2 = QtWidgets.QDialog()
    ui = Ui_NModulesWindow2()
    ui.setupUi(NModulesWindow2)
    NModulesWindow2.show()
    sys.exit(app.exec_())

