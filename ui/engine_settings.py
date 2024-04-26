# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'engine_settings.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QSizePolicy, QSlider,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 20, 771, 261))
        font = QFont()
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)

        self.verticalSlider_5 = QSlider(self.groupBox_4)
        self.verticalSlider_5.setObjectName(u"verticalSlider_5")
        self.verticalSlider_5.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_5.addWidget(self.verticalSlider_5)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_10)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.groupBox_4)

        self.groupBox_8 = QGroupBox(self.groupBox)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_17)

        self.verticalSlider_9 = QSlider(self.groupBox_8)
        self.verticalSlider_9.setObjectName(u"verticalSlider_9")
        self.verticalSlider_9.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_9.addWidget(self.verticalSlider_9)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_18)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.label_6 = QLabel(self.groupBox_8)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_6.addWidget(self.label_6)


        self.horizontalLayout.addWidget(self.groupBox_8)

        self.groupBox_5 = QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_11)

        self.verticalSlider_6 = QSlider(self.groupBox_5)
        self.verticalSlider_6.setObjectName(u"verticalSlider_6")
        self.verticalSlider_6.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_6.addWidget(self.verticalSlider_6)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_12)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.label_3 = QLabel(self.groupBox_5)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)


        self.horizontalLayout.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.groupBox)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_13)

        self.verticalSlider_7 = QSlider(self.groupBox_6)
        self.verticalSlider_7.setObjectName(u"verticalSlider_7")
        self.verticalSlider_7.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_7.addWidget(self.verticalSlider_7)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_14)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.label_4 = QLabel(self.groupBox_6)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)


        self.horizontalLayout.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(self.groupBox)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_15)

        self.verticalSlider_8 = QSlider(self.groupBox_7)
        self.verticalSlider_8.setObjectName(u"verticalSlider_8")
        self.verticalSlider_8.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.verticalSlider_8)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_16)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.label_5 = QLabel(self.groupBox_7)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_5.addWidget(self.label_5)


        self.horizontalLayout.addWidget(self.groupBox_7)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043e\u0441\u043d\u043e\u0432\u043d\u044b\u043c\u0438 \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f\u043c\u0438", None))
        self.groupBox_4.setTitle("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21161", None))
        self.groupBox_8.setTitle("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21162", None))
        self.groupBox_5.setTitle("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21163", None))
        self.groupBox_6.setTitle("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u21164", None))
        self.groupBox_7.setTitle("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0430\u044f \u0442\u044f\u0433\u0430", None))
    # retranslateUi

