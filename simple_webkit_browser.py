# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'webviewtest.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2.QtWebEngineWidgets import QWebEngineView

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(912, 730)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.urlEdit = QLineEdit(self.centralwidget)
        self.urlEdit.setObjectName(u"urlEdit")

        self.buttonLayout.addWidget(self.urlEdit)

        self.goButton = QPushButton(self.centralwidget)
        self.goButton.setObjectName(u"goButton")

        self.buttonLayout.addWidget(self.goButton)


        self.verticalLayout.addLayout(self.buttonLayout)

        self.navigatorLayout = QHBoxLayout()
        self.navigatorLayout.setObjectName(u"navigatorLayout")
        self.forwardButton = QPushButton(self.centralwidget)
        self.forwardButton.setObjectName(u"forwardButton")

        self.navigatorLayout.addWidget(self.forwardButton)

        self.refreshButton = QPushButton(self.centralwidget)
        self.refreshButton.setObjectName(u"refreshButton")

        self.navigatorLayout.addWidget(self.refreshButton)

        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setObjectName(u"backButton")

        self.navigatorLayout.addWidget(self.backButton)


        self.verticalLayout.addLayout(self.navigatorLayout)

        self.webView = QWebEngineView(self.centralwidget)
        self.webView.setObjectName(u"webView")
        self.webView.setUrl(QUrl(u"https://duckduckgo.com/"))

        self.verticalLayout.addWidget(self.webView)


        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 912, 28))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.webView, self.urlEdit)
        QWidget.setTabOrder(self.urlEdit, self.goButton)
        QWidget.setTabOrder(self.goButton, self.forwardButton)
        QWidget.setTabOrder(self.forwardButton, self.refreshButton)
        QWidget.setTabOrder(self.refreshButton, self.backButton)

        self.retranslateUi(MainWindow)
        self.urlEdit.returnPressed.connect(self.redirectUrl)
        self.backButton.clicked.connect(self.webView.back)
        self.forwardButton.clicked.connect(self.webView.forward)
        self.refreshButton.clicked.connect(self.webView.reload)
        self.goButton.clicked.connect(self.redirectUrl)
        self.webView.loadFinished.connect(self.webView.setFocus)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"WebView Test", None))
        self.urlEdit.setText(QCoreApplication.translate("MainWindow", u"https://duckduckgo.com", None))
        self.goButton.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.forwardButton.setText(QCoreApplication.translate("MainWindow", u"Forward", None))
        self.refreshButton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.backButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
    # retranslateUi

    def redirectUrl(self):
        self.webView.setUrl(QUrl(self.urlEdit.text()))
