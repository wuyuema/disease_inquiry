# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelInput = QtWidgets.QLabel(self.centralwidget)
        self.labelInput.setObjectName("labelInput")
        self.verticalLayout.addWidget(self.labelInput)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.pushButtonCommit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCommit.setObjectName("pushButtonCommit")
        self.verticalLayout.addWidget(self.pushButtonCommit)
        self.labelOutput = QtWidgets.QLabel(self.centralwidget)
        self.labelOutput.setObjectName("labelOutput")
        self.verticalLayout.addWidget(self.labelOutput)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButtonCommit.clicked.connect(MainWindow.commit)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelInput.setText(_translate("MainWindow", "输入病情描述"))
        self.pushButtonCommit.setText(_translate("MainWindow", "提交"))
        self.labelOutput.setText(_translate("MainWindow", "推荐诊室与医生"))
