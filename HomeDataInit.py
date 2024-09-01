"""
AirDex Home Edition Build : init file ;
A weather app with minimal design which provides real-time weather information,
including temperature, pressure, humidity, and more, using data from the OpenWeatherMap API.
The app features a beautiful UI that changes according to the time of day.

----------------------------------------------------------------------
Created by Aditya Gaur
Credits to: PySide2, QtDesigner, OpenWeatherMap API

"""

# Imports
import sys, platform,pickle,os

from ui_main import Ui_Home
from ui_safeabort import Ui_Dialog
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore, QtGui, QtWidgets
    

import requests
import datetime
import time, json

# For temperature in Fahrenheit use units=imperial
# For temperature in Celsius use units=metric
# Temperature in Kelvin is used by default, no need to use units parameter in API call

#  Color Scheme Params
ColorSchemeBG = {
    "morning": "background-color: qlineargradient(spread:pad, x1:1, y1:0.074, x2:1, y2:1, stop:0 rgba(53, 211, 255, 255), stop:1 rgba(77, 131, 247, 255));border-radius:10px;",
    "after": "background-color: qlineargradient(spread:pad, x1:1, y1:0.102, x2:1, y2:1, stop:0 rgba(255, 255, 25, 255), stop:1 rgba(255, 191, 0, 255));border-radius:10px;",
    "eve": "background-color: qlineargradient(spread:pad, x1:1, y1:0.045, x2:1, y2:1, stop:0 rgba(255, 185, 80, 255), "
           "stop:1 rgba(255, 60, 60, 255));border-radius:10px;",
    "night": "background-color: qlineargradient(spread:pad, x1:1, y1:0.193, x2:1, y2:1, stop:0 rgba(0, 0, "
             "0, 255), stop:1 rgba(0, 18, 97, 255));border-radius:10px;"}

ColorSchemeWE = {"cse": "background-color: rgba(255, 255, 255, 0);color: rgb(255, 255, 255);"}
ColorSchemeTX = {"morning": "background-color: rgba(255, 255, 255, 0);color: rgb(40, 100, 231);", "after": "background"
                                                                                                           "-color: "
                                                                                                           "rgba(255, "
                                                                                                           "255, 255, "
                                                                                                           "0);color: "
                                                                                                           "rgb(255, "
                                                                                                           "147, 14);",
                 "eve": "background-color: rgba(255, 255, 255, 0);color: rgb(255, 51, 0);",
                 "night": "background-color: "
                          "rgba(255, 255, "
                          "255, "
                          "0);color: rgb(0, "
                          "30, 149);"}

#  Defined constants

MAX = None
MIN = None
PA = None
HUMI = None
CON = None

LAT = None
LON = None
TIMEZN = None

RCLK = 0

UNIT = "metric"
ff = "°C"

WAPI = "12182c2dfbc5c517ec45b92c91c90894"
lurl = "https://ipinfo.io/"


# aurl = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={LAT}&lon={LON}&appid={WAPI}"


# print(OVRALOC)
# print(weather)
# print(f"{MAX},{MIN},{PA},{HUMI},{CON},{VIS}")

# DATA SET : maxtemp,mintemp,pressure,humidity,visibility,timezone,lat,lon,time,date

# Home Page Activity 
class HomeActivity(QMainWindow):
    def __init__(self):
        # Initializing UI
        QMainWindow.__init__(self)
        self.ui = Ui_Home()
        self.ui.setupUi(self)
        self.requestWeather()
        self.changeCS()


        # Adding Fonts
        QtGui.QFontDatabase.addApplicationFont("assets/faces/Comfortaa/Comfortaa-Light.ttf")
        QtGui.QFontDatabase.addApplicationFont("assets/faces/Comfortaa/Comfortaa-medium.ttf")
        QtGui.QFontDatabase.addApplicationFont("assets/faces/Comfortaa/Comfortaa-Regular.ttf")
        QtGui.QFontDatabase.addApplicationFont("assets/faces/Open_Sans/OpenSans-SemiBold.ttf")

        # Styling the app

        self.ui.temp.setStyleSheet(
            "font-family: Comfortaa; font:Comfortaa-Medium; color:rgb(255,255,255); background-color: rgba(255,255,255,0); font-size:120px;")

        self.ui.title.setText("AirDex Home - 1.1.b0")
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui.minmax.clicked.connect(lambda: self.showMinimized())
        self.ui.icon.setPixmap(QPixmap("assets/icons/ic.ico"))
        self.setWindowIcon(QtGui.QIcon("assets/icons/ic.ico"))
        self.setIconSize(QtCore.QSize(64, 64))

        self.fxShadow = QGraphicsDropShadowEffect(self)
        self.fxShadow.setBlurRadius(25)
        self.fxShadow.setXOffset(0)
        self.fxShadow.setYOffset(0)
        self.fxShadow.setColor(QColor(0, 0, 0, 55))
        self.ui.drop.setGraphicsEffect(self.fxShadow)

        # CLOSE
        self.ui.exit.clicked.connect(lambda: self.closeOpen(self.exeOp.isChecked()))

        def moveWindow(event):
            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.drop.mouseMoveEvent = moveWindow


        self.ui.exit.setToolTip('Exit')
        self.ui.minmax.setToolTip('Minimise/Restore')
        self.ui.icon.setToolTip('AirDex Home Edition')
        
        # System Tray Icon Init
        self.CSTTask()
        
        # Loading settings to check info
        self.setCheck()

        self.show()

    # Show warning method 
    def showWarning(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        rsp = Dialog.exec_()

        if rsp == QtWidgets.QDialog.Accepted:
            self.close()
            quit()
        else:
            self.close()
            quit()

    # Requesting weather Info
    def requestWeather(self):
        global UNIT, WAPI
        try:

            # GET LOCATION
            self.locd = requests.get(lurl).json()
            self.LOC = str(self.locd["city"])
            self.COOR = str(self.locd["loc"])
            self.LAT = self.COOR.split(",")[0]
            self.LON = self.COOR.split(",")[1]
            self.COUN = str(self.locd["country"])
            self.TIMEZN = str(self.locd["timezone"])

            self.wurl = f"http://api.openweathermap.org/data/2.5/weather?q={self.LOC}&units={UNIT}&appid={WAPI}"

            self.GLOBAL_STATE = 0

            # GET WEATHER DATA
            self.weather = requests.get(self.wurl).json()

            self.TEMP = int(self.weather["main"]["temp"])
            self.FTEMP = str(self.TEMP)
            self.MAX = str(self.weather["main"]["temp_max"]) + ff
            self.MIN = str(self.weather["main"]["temp_min"]) + ff
            self.PA = str(self.weather["main"]["pressure"]) + "Pa"
            self.HUMI = str(self.weather["main"]["humidity"]) + "%"
            self.CON = str(self.weather["weather"][0]["main"])
            self.VIS = str(self.weather["visibility"]) + "m"
            self.OVRALOC = self.LOC + ", " + self.COUN

            self.DATTIME = datetime.datetime.now()
            self.DATE = self.DATTIME.strftime("%A, %B %d,%Y")

            self.setValues()
        except requests.exceptions.RequestException as e:
            self.showWarning()

    # Updating interface values
    def setValues(self):
        self.ui.title.setText("AirDex Home - 1.1.b0 - Loading...")
        self.ui.temp.setText(self.FTEMP)
        self.ui.degree.setText("°C")
        self.ui.city.setText(self.LOC)
        self.ui.condition.setText(self.CON)
        self.ui.maxtemp.setText(self.MAX)
        self.ui.mintemp.setText(self.MIN)
        self.ui.pressure.setText(self.PA)
        self.ui.humid.setText(self.HUMI)
        self.ui.visibility.setText(self.VIS)
        self.ui.timezone.setText(self.TIMEZN)
        self.ui.latitude.setText(self.LAT)
        self.ui.longitude.setText(self.LON)
        self.ui.location.setText(self.OVRALOC)
        self.ui.date.setText(self.DATE)
        self.ui.title.setText("AirDex - 1.1.b0")

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    
    # Color scheme change
    def changeCS(self):
        global ColorSchemeBG, ColorSchemeTX, ColorSchemeWE
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            self.ui.drop.setStyleSheet(ColorSchemeBG["morning"])
            self.ui.condition.setStyleSheet(ColorSchemeTX["morning"])
            self.ui.degree.setStyleSheet(ColorSchemeTX["morning"])
            self.ui.wish.setText("Morning!")
            self.ui.image.setPixmap(QPixmap("assets/icons/stateMorn.png"))


        elif hour >= 12 and hour < 18:
            self.ui.drop.setStyleSheet(ColorSchemeBG["after"])
            self.ui.condition.setStyleSheet(ColorSchemeTX["after"])
            self.ui.degree.setStyleSheet(ColorSchemeTX["after"])
            self.ui.wish.setText("Afternoon!")
            self.ui.image.setPixmap(QPixmap("assets/icons/stateAfter.png"))


        elif hour >= 18 and hour < 21:
            self.ui.drop.setStyleSheet(ColorSchemeBG["eve"])
            self.ui.condition.setStyleSheet(ColorSchemeTX["eve"])
            self.ui.degree.setStyleSheet(ColorSchemeTX["eve"])
            self.ui.wish.setText("Evening!")
            self.ui.image.setPixmap(QPixmap("assets/icons/stateEve.png"))


        else:
            if hour >= 21 and hour < 24:
                self.ui.drop.setStyleSheet(ColorSchemeBG["night"])
                self.ui.condition.setStyleSheet(ColorSchemeTX["night"])
                self.ui.degree.setStyleSheet(ColorSchemeTX["night"])
                self.ui.wish.setText("Night!")
                self.ui.image.setPixmap(QPixmap("assets/icons/stateNight.png"))

    # Initializing Custom System Tray Icon
    def CSTTask(self):
        self.systray = QSystemTrayIcon(QIcon("assets/icons/ic.ico"), parent=self)
        self.systray.setToolTip("AixDex Home Edition")
        self.setting = QSettings("AirDexHome", "Home")

        self.stm = QMenu()
        self.open = self.stm.addAction('Open')
        self.min = self.stm.addAction('Minimise')
        self.exeOp = self.stm.addAction('Keep app running in background')
        self.exeOp.setCheckable(True)
        self.stm.addSeparator()
        self.exitAct = self.stm.addAction('Exit')

        self.open.triggered.connect(lambda: self.showNormal())
        self.min.triggered.connect(lambda: self.showMinimized())
        self.exeOp.triggered.connect(lambda: self.closeOpen(self.exeOp.isChecked()))
        self.exitAct.triggered.connect(lambda: self.close())

        self.systray.setContextMenu(self.stm)

        self.systray.show()
        self.systray.activated.connect(self.systemIconActivation)
    
    # trigger app show on system tray icon click.
    def systemIconActivation(self, reason):
        if reason == self.systray.DoubleClick or reason == self.systray.Trigger:
            self.show()
            self.showNormal()
    
    # just hide if "keep app running in background" is checked, else not (just exit)
    def closeOpen(self, checked):
        self.checked = checked
        if self.checked:
            if self.checkData():
                self.changeData("True")
            else:
                self.saveState("True")
            self.setCheck()
            self.ui.exit.clicked.connect(lambda: self.hide())

        else:
            if self.checkData():
                self.changeData("False")
            else:
                self.saveState("False")
            self.setCheck()
            self.ui.exit.clicked.connect(lambda: self.close())

    # checking for "keep app running in background"
    def setCheck(self):
        self.state = self.loadData()
        if self.state == "True":
            self.exeOp.setChecked(True)
        elif self.state == "False":
            self.exeOp.setChecked(False)
    
    # checking if settings exists
    def checkData(self):
        return os.path.exists("data/settings.asd")

    # Keeping check of state
    def saveState(self,val):
        self.key = "State"
        self.val = val
        self.data = {self.key:self.val}
        pickle.dump(self.data,open("data/settings.asd","wb"))

    # Changing Settings data
    def changeData(self,newval):
        self.newval = newval
        self.saveState(self.newval)

    # Load settings from settings.asd file, (*.asd) -> atomic systems data file format (nothing special, just a pickled file)
    def loadData(self):
        self.loadKey = pickle.load(open("data/settings.asd","rb"))
        return self.loadKey["State"]