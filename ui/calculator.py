# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator.ui'
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
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font)

        self.horizontalLayout.addWidget(self.lineEdit)


        self.horizontalLayout_6.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.lineEdit_2 = QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.lineEdit_2)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton = QPushButton(self.groupBox_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font)

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.groupBox_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font)

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.groupBox_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font)

        self.horizontalLayout_3.addWidget(self.pushButton_4)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lineEdit_3 = QLineEdit(self.groupBox_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 150))
        font1 = QFont()
        font1.setPointSize(60)

        self.lineEdit_3.setFont(font1)
        self.lineEdit_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_3.setStyleSheet('color : "#0fc121"')

        self.horizontalLayout_7.addWidget(self.lineEdit_3)


        self.verticalLayout.addWidget(self.groupBox_4)

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
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0432\u043e\u0435 \u0447\u0438\u0441\u043b\u043e:", None))
#if QT_CONFIG(statustip)
        self.lineEdit.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0435\u0440\u0432\u043e\u0435 \u0447\u0438\u0441\u043b\u043e", None))
        self.groupBox_2.setTitle("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0442\u043e\u0440\u043e\u0435 \u0447\u0438\u0441\u043b\u043e:", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0442\u043e\u0440\u043e\u0435 \u0447\u0438\u0441\u043b\u043e", None))
        self.groupBox_3.setTitle("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.groupBox_4.setTitle("")
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
    # retranslateUi

