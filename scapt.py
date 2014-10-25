#!/usr/bin/env python
from PyQt4 import QtGui, QtCore
import sys
import os
from capture import CaptureDialog


def main():
    app=QtGui.QApplication(sys.argv)
    QtCore.QCoreApplication.setOrganizationName("MLGSoft")
    QtCore.QCoreApplication.setOrganizationDomain("mlgsoft.com")
    QtCore.QCoreApplication.setApplicationName("Scapt")
    root=os.path.dirname(os.path.abspath(__file__))
    os.chdir(root)
    d=CaptureDialog()
    d.show()
    app.exec_()
    

if __name__=='__main__':
    main()