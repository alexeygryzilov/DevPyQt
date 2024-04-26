# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ship_parameters.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(396, 248)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(13)
        self.groupBox.setFont(font)
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setFlat(False)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFrameShape(QFrame.Shape.Panel)
        self.label_6.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_6.setStyleSheet('color:orange')

        self.horizontalLayout.addWidget(self.label_6)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFrameShape(QFrame.Shape.Panel)
        self.label_7.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_7.setStyleSheet('color : "#19DE01"')

        self.horizontalLayout_2.addWidget(self.label_7)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFrameShape(QFrame.Shape.Panel)
        self.label_8.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_8.setStyleSheet('color : "#19DE01"')

        self.horizontalLayout_3.addWidget(self.label_8)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFrameShape(QFrame.Shape.Panel)
        self.label_9.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_9.setStyleSheet('color : "#19DE01"')

        self.horizontalLayout_4.addWidget(self.label_9)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFrameShape(QFrame.Shape.Panel)
        self.label_10.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_10.setStyleSheet('color : "#3DD41E"')



        self.horizontalLayout_5.addWidget(self.label_10)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.verticalLayout_2.addWidget(self.groupBox)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 396, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043a\u043e\u0440\u0430\u0431\u043b\u044f", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 \u043d\u0430 \u0431\u043e\u0440\u0442\u0443", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"22 \u0421", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0433\u0435\u0440\u043c\u0435\u0442\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u21161", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0440\u043c\u0430", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u21162", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0440\u043c\u0430", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043a \u21163", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0440\u043c\u0430", None))
    # retranslateUi

