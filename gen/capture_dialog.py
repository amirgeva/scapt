# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/capture_dialog.ui'
#
#
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(640, 354)
        Dialog.closeButton = QtGui.QPushButton(Dialog)
        Dialog.closeButton.setGeometry(QtCore.QRect(512, 304, 119, 32))
        Dialog.closeButton.setObjectName(_fromUtf8("closeButton"))
        Dialog.winDescEdit = QtGui.QLineEdit(Dialog)
        Dialog.winDescEdit.setGeometry(QtCore.QRect(128, 16, 369, 32))
        Dialog.winDescEdit.setReadOnly(True)
        Dialog.winDescEdit.setObjectName(_fromUtf8("winDescEdit"))
        Dialog.label = QtGui.QLabel(Dialog)
        Dialog.label.setGeometry(QtCore.QRect(16, 16, 84, 22))
        Dialog.label.setObjectName(_fromUtf8("label"))
        Dialog.selectWinButton = QtGui.QPushButton(Dialog)
        Dialog.selectWinButton.setGeometry(QtCore.QRect(512, 16, 119, 32))
        Dialog.selectWinButton.setObjectName(_fromUtf8("selectWinButton"))
        Dialog.dirEdit = QtGui.QLineEdit(Dialog)
        Dialog.dirEdit.setGeometry(QtCore.QRect(128, 64, 369, 32))
        Dialog.dirEdit.setObjectName(_fromUtf8("dirEdit"))
        Dialog.label_2 = QtGui.QLabel(Dialog)
        Dialog.label_2.setGeometry(QtCore.QRect(16, 48, 84, 49))
        Dialog.label_2.setWordWrap(True)
        Dialog.label_2.setObjectName(_fromUtf8("label_2"))
        Dialog.selectDirButton = QtGui.QPushButton(Dialog)
        Dialog.selectDirButton.setGeometry(QtCore.QRect(512, 64, 119, 32))
        Dialog.selectDirButton.setObjectName(_fromUtf8("selectDirButton"))
        Dialog.captureButton = QtGui.QPushButton(Dialog)
        Dialog.captureButton.setGeometry(QtCore.QRect(128, 160, 369, 129))
        Dialog.captureButton.setObjectName(_fromUtf8("captureButton"))
        Dialog.frameCB = QtGui.QCheckBox(Dialog)
        Dialog.frameCB.setGeometry(QtCore.QRect(128, 112, 241, 27))
        Dialog.frameCB.setObjectName(_fromUtf8("frameCB"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Scapt", None))
        Dialog.closeButton.setText(_translate("Dialog", "Close", None))
        Dialog.label.setText(_translate("Dialog", "Window", None))
        Dialog.selectWinButton.setText(_translate("Dialog", "Select", None))
        Dialog.label_2.setText(_translate("Dialog", "Images Directory", None))
        Dialog.selectDirButton.setText(_translate("Dialog", "Select", None))
        Dialog.captureButton.setText(_translate("Dialog", "Capture", None))
        Dialog.frameCB.setText(_translate("Dialog", "Include Window Frame", None))

