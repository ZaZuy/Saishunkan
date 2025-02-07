# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(761, 771)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 0, 761, 411))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 480, 81, 16))
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setTabletTracking(False)
        self.phonenumberText = QLineEdit(self.centralwidget)
        self.phonenumberText.setObjectName(u"phonenumberText")
        self.phonenumberText.setGeometry(QRect(210, 480, 161, 22))
        self.addressText = QLineEdit(self.centralwidget)
        self.addressText.setObjectName(u"addressText")
        self.addressText.setGeometry(QRect(210, 520, 161, 22))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 520, 49, 16))
        self.label_2.setFont(font)
        self.emailText = QLineEdit(self.centralwidget)
        self.emailText.setObjectName(u"emailText")
        self.emailText.setGeometry(QRect(210, 600, 231, 22))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 600, 49, 16))
        self.label_3.setFont(font)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(110, 560, 91, 16))
        self.label_4.setFont(font)
        self.fullnameText = QLineEdit(self.centralwidget)
        self.fullnameText.setObjectName(u"fullnameText")
        self.fullnameText.setGeometry(QRect(470, 480, 161, 22))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(390, 480, 49, 16))
        self.label_5.setFont(font)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(390, 560, 49, 16))
        self.label_6.setFont(font)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(390, 520, 61, 16))
        self.label_7.setFont(font)
        self.deleteButton = QPushButton(self.centralwidget)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setGeometry(QRect(670, 420, 75, 24))
        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(620, 640, 75, 24))
        self.quitButton = QPushButton(self.centralwidget)
        self.quitButton.setObjectName(u"quitButton")
        self.quitButton.setGeometry(QRect(670, 700, 75, 24))
        self.completeButton = QPushButton(self.centralwidget)
        self.completeButton.setObjectName(u"completeButton")
        self.completeButton.setGeometry(QRect(580, 700, 75, 24))
        self.refeshButton = QPushButton(self.centralwidget)
        self.refeshButton.setObjectName(u"refeshButton")
        self.refeshButton.setGeometry(QRect(580, 420, 75, 24))
        self.frameForm = QFrame(self.centralwidget)
        self.frameForm.setObjectName(u"frameForm")
        self.frameForm.setGeometry(QRect(60, 460, 651, 221))
        self.frameForm.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameForm.setFrameShadow(QFrame.Shadow.Raised)
        self.birthDateEdit = QDateEdit(self.centralwidget)
        self.birthDateEdit.setObjectName(u"birthDateEdit")
        self.birthDateEdit.setGeometry(QRect(470, 520, 110, 22))
        self.statusOnlineButton = QRadioButton(self.centralwidget)
        self.statusOnlineButton.setObjectName(u"statusOnlineButton")
        self.statusOnlineButton.setGeometry(QRect(210, 560, 89, 20))
        self.statusOfflineButton = QRadioButton(self.centralwidget)
        self.statusOfflineButton.setObjectName(u"statusOfflineButton")
        self.statusOfflineButton.setGeometry(QRect(280, 560, 89, 20))
        self.genderMaleButton = QRadioButton(self.centralwidget)
        self.genderMaleButton.setObjectName(u"genderMaleButton")
        self.genderMaleButton.setGeometry(QRect(470, 560, 89, 20))
        self.genderFemaleButton = QRadioButton(self.centralwidget)
        self.genderFemaleButton.setObjectName(u"genderFemaleButton")
        self.genderFemaleButton.setGeometry(QRect(540, 560, 89, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 761, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"S\u1ed1 \u0111i\u1ec7n tho\u1ea1i", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ecba ch\u1ec9", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Tr\u1ea1ng th\u00e1i", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"H\u1ecd t\u00ean", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Gi\u1edbi t\u00ednh", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y sinh", None))
        self.deleteButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.quitButton.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.completeButton.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.refeshButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.statusOnlineButton.setText(QCoreApplication.translate("MainWindow", u"Online", None))
        self.statusOfflineButton.setText(QCoreApplication.translate("MainWindow", u"Offline", None))
        self.genderMaleButton.setText(QCoreApplication.translate("MainWindow", u"Male", None))
        self.genderFemaleButton.setText(QCoreApplication.translate("MainWindow", u"Female", None))
    # retranslateUi

