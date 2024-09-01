"""
AirDex Home Edition Build: 
A weather app with minimal design which provides real-time weather information,
including temperature, pressure, humidity, and more, using data from the OpenWeatherMap API.
The app features a beautiful UI that changes according to the time of day.

----------------------------------------------------------------------
Created by Aditya Gaur
Credits to: PySide2, QtDesigner, OpenWeatherMap API

"""


# Imports 
import sys,platform
from PySide2 import QtCore,QtGui,QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui_splash import Ui_SplashActivity
from HomeDataInit import HomeActivity
from ui_warningdialog import Ui_Dialog

import socket,time,timeit

TIMEOUT = 0

# Splash screen activity 
class SplashActivity(QMainWindow):
    def __init__(self):
        # Initializing UI
        
        QMainWindow.__init__(self)
        self.ui = Ui_SplashActivity()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("assets/icons/ic.ico"))
        self.setIconSize(QtCore.QSize(64,64))
        
        # Adding Fonts

        QtGui.QFontDatabase.addApplicationFont("assets/faces/Comfortaa/Comfortaa-Light.ttf")
        QtGui.QFontDatabase.addApplicationFont("assets/faces/Comfortaa/Comfortaa-medium.ttf")
        QtGui.QFontDatabase.addApplicationFont("assets/faces/Comfortaa/Comfortaa-Regular.ttf")
        QtGui.QFontDatabase.addApplicationFont("assets/faces/Open_Sans/OpenSans-SemiBold.ttf")


        # Window customisation
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.fxShadow = QGraphicsDropShadowEffect(self)
        self.fxShadow.setBlurRadius(25)
        self.fxShadow.setXOffset(0)
        self.fxShadow.setYOffset(0)
        self.fxShadow.setColor(QColor(0,0,0,55))
        self.ui.drop.setGraphicsEffect(self.fxShadow)

        # Styling the app

        self.ui.img.setPixmap("assets/icons/icHome.png")

        self.ui.head.setStyleSheet("font-family: Comfortaa; font:Comfortaa-Medium; color:rgb(255,255,255); background-color: rgba(255,255,255,0); font-size:68px;")
        self.ui.subhead.setStyleSheet("font-family: Comfortaa; font:Comfortaa-Regular; color:rgb(255,255,255); background-color: rgba(255,255,255,0); font-size:20px;")
        self.ui.version.setStyleSheet("font-family: Comfortaa; font:Comfortaa-Light;color: rgb(0, 120, 219); background-color: rgba(255,255,255,0); font-size:8px;")
        self.ui.atomic.setStyleSheet("font-family: Open-Sans; font:OpenSans-SemiBold;color: rgb(255,255,255); background-color: rgba(255,255,255,0); font-size:10px;")


        self.loadt = QtCore.QTimer()
        self.loadt.timeout.connect(self.progress)
        self.loadt.start(50)


    # changing values of progress bar
    def progress(self):
        global TIMEOUT

        self.ui.progress.setValue(TIMEOUT)

        if TIMEOUT > 100 and self.chckConn():
            self.loadt.stop()
            self.home = HomeActivity()
            self.home.show()
            self.close()

        elif TIMEOUT > 100 and not self.chckConn():
            showWarning(self)


        TIMEOUT +=1

    # check internet connection by pinging a website
    def chckConn(self):
        try:
            socket.create_connection(('Google.com',80))
            return True
        except OSError:
            return False

# show warning if no connection is present.
def showWarning(self):
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    rsp = Dialog.exec_()

    if rsp == QtWidgets.QDialog.Accepted:
        self.loadt.stop()
        self.home = HomeActivity()
        self.home.show()
        self.close()
    else:
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashActivity()
    window.show()
    sys.exit(app.exec_())