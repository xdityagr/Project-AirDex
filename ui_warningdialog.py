
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(364, 164)
        Dialog.setModal(False)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 371, 161))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.warning = QLabel(self.frame)
        self.warning.setObjectName(u"warning")
        self.warning.setGeometry(QRect(10, 10, 191, 31))
        font = QFont()
        font.setFamily(u"Bahnschrift Light")
        font.setPointSize(14)
        self.warning.setFont(font)
        self.warning.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.buttonBox = QDialogButtonBox(self.frame)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 130, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close|QDialogButtonBox.Yes)
        self.description = QLabel(self.frame)
        self.description.setObjectName(u"description")
        self.description.setGeometry(QRect(10, 50, 331, 71))
        self.description.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.description.setWordWrap(True)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Warning", None))
        self.warning.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600;\">AirDex </span>Warning</p></body></html>", None))
        self.description.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt;\">It seems Like you do not have an Internet Connection or it is not Stable.Try Connecting to a Stable Internet Connection or Restart Application.Do you want to continue Startup?</span></p></body></html>", None))
    # retranslateUi

