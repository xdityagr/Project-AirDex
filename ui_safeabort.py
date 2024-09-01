
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(367, 164)
        self.abort = QDialogButtonBox(Dialog)
        self.abort.setObjectName(u"abort")
        self.abort.setGeometry(QRect(-10, 130, 361, 32))
        self.abort.setOrientation(Qt.Horizontal)
        self.abort.setStandardButtons(QDialogButtonBox.Abort)
        self.warning = QLabel(Dialog)
        self.warning.setObjectName(u"warning")
        self.warning.setGeometry(QRect(10, 10, 191, 31))
        font = QFont()
        font.setFamily(u"Bahnschrift Light")
        font.setPointSize(14)
        self.warning.setFont(font)
        self.warning.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.description = QLabel(Dialog)
        self.description.setObjectName(u"description")
        self.description.setGeometry(QRect(10, 50, 331, 71))
        self.description.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.description.setWordWrap(True)

        self.retranslateUi(Dialog)
        self.abort.accepted.connect(Dialog.accept)
        self.abort.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.warning.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:600;\">AirDex </span>Warning</p></body></html>", None))
        self.description.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt;\">It seems Like you do not have an Internet Connection or it is not Stable.Try Connecting to a Stable Internet Connection or Restart Application. You should safely abort now.</span></p></body></html>", None))
    # retranslateUi

