
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SplashActivity(object):
    def setupUi(self, SplashActivity):
        if not SplashActivity.objectName():
            SplashActivity.setObjectName(u"SplashActivity")
        SplashActivity.resize(642, 400)
        self.centralwidget = QWidget(SplashActivity)
        self.centralwidget.setObjectName(u"centralwidget")
        self.drop = QFrame(self.centralwidget)
        self.drop.setObjectName(u"drop")
        self.drop.setGeometry(QRect(9, 9, 621, 381))
        self.drop.setStyleSheet(u"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.045, x2:0.988636, y2:1, stop:0 rgba(93, 166, 255, 255), stop:1 rgba(30, 134, 219, 255));")
        self.drop.setFrameShape(QFrame.StyledPanel)
        self.drop.setFrameShadow(QFrame.Raised)
        self.head = QLabel(self.drop)
        self.head.setObjectName(u"head")
        self.head.setGeometry(QRect(180, 110, 231, 101))
        font = QFont()
        font.setPointSize(60)
        self.head.setFont(font)
        self.head.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.subhead = QLabel(self.drop)
        self.subhead.setObjectName(u"subhead")
        self.subhead.setGeometry(QRect(210, 200, 201, 31))
        font1 = QFont()
        font1.setPointSize(16)
        self.subhead.setFont(font1)
        self.subhead.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.img = QLabel(self.drop)
        self.img.setObjectName(u"img")
        self.img.setGeometry(QRect(410, 130, 71, 71))
        self.img.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.img.setPixmap(QPixmap(u"../assets/ic/ic.png"))
        self.img.setScaledContents(True)
        self.progress = QProgressBar(self.drop)
        self.progress.setObjectName(u"progress")
        self.progress.setGeometry(QRect(0, 340, 621, 23))
        self.progress.setStyleSheet(u"QProgressBar {\n"
"	border-radius:0px;\n"
"	background-color: rgb(255, 255, 255,100);\n"
"}\n"
"QProgressBar::chunk{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0.1875 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.progress.setValue(0)
        self.progress.setTextVisible(False)
        self.atomic = QLabel(self.drop)
        self.atomic.setObjectName(u"atomic")
        self.atomic.setGeometry(QRect(10, 320, 121, 16))
        self.atomic.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255,255,255);")
        self.version = QLabel(self.drop)
        self.version.setObjectName(u"version")
        self.version.setGeometry(QRect(390, 200, 71, 31))
        self.version.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(0, 120, 219);")
        SplashActivity.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashActivity)

        QMetaObject.connectSlotsByName(SplashActivity)
    # setupUi

    def retranslateUi(self, SplashActivity):
        SplashActivity.setWindowTitle(QCoreApplication.translate("SplashActivity", u"AirDex Home - 1.0.09B", None))
        self.head.setText(QCoreApplication.translate("SplashActivity", u"AirDex", None))
        self.subhead.setText(QCoreApplication.translate("SplashActivity", u"<html><head/><body><p align=\"center\">Home Edition</p></body></html>", None))
        self.img.setText("")
        self.atomic.setText(QCoreApplication.translate("SplashActivity", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Atomic Systems Inc.</span></p></body></html>", None))
        self.version.setText(QCoreApplication.translate("SplashActivity", u"BETA 1.0.09B", None))
    # retranslateUi

