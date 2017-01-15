# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_ui.ui'
#
# Created: Sun Jan 15 17:43:46 2017
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_dlgShape(object):
    def setupUi(self, dlgShape):
        dlgShape.setObjectName(_fromUtf8("dlgShape"))
        dlgShape.resize(951, 760)
        dlgShape.setAutoFillBackground(False)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(dlgShape)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.grid = QtGui.QGridLayout()
        self.grid.setObjectName(_fromUtf8("grid"))
        self.horizontalLayout_4.addLayout(self.grid)
        self.table = QtGui.QTableView(dlgShape)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy)
        self.table.setObjectName(_fromUtf8("table"))
        self.horizontalLayout_4.addWidget(self.table)
        self.horizontalLayout_4.setStretch(0, 100)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.OpenFile = QtGui.QPushButton(dlgShape)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OpenFile.sizePolicy().hasHeightForWidth())
        self.OpenFile.setSizePolicy(sizePolicy)
        self.OpenFile.setObjectName(_fromUtf8("OpenFile"))
        self.horizontalLayout.addWidget(self.OpenFile)
        self.label = QtGui.QLabel(dlgShape)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.prompt = QtGui.QLabel(dlgShape)
        self.prompt.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prompt.sizePolicy().hasHeightForWidth())
        self.prompt.setSizePolicy(sizePolicy)
        self.prompt.setObjectName(_fromUtf8("prompt"))
        self.horizontalLayout_3.addWidget(self.prompt)
        self.progressBar_2 = QtGui.QProgressBar(dlgShape)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar_2.sizePolicy().hasHeightForWidth())
        self.progressBar_2.setSizePolicy(sizePolicy)
        self.progressBar_2.setMaximumSize(QtCore.QSize(0, 16777215))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName(_fromUtf8("progressBar_2"))
        self.horizontalLayout_3.addWidget(self.progressBar_2)
        self.progressBar = QtGui.QProgressBar(dlgShape)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.horizontalLayout_3.addWidget(self.progressBar)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(dlgShape)
        QtCore.QObject.connect(self.OpenFile, QtCore.SIGNAL(_fromUtf8("clicked()")), dlgShape.openFile)
        QtCore.QMetaObject.connectSlotsByName(dlgShape)

    def retranslateUi(self, dlgShape):
        dlgShape.setWindowTitle(_translate("dlgShape", "Road - 201411172039", None))
        self.OpenFile.setText(_translate("dlgShape", "Open File", None))
        self.prompt.setText(_translate("dlgShape", "TextLabel", None))
        self.progressBar.setFormat(_translate("dlgShape", "%p%", None))

