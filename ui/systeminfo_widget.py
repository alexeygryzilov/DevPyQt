# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'systeminfo_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_CPUloadRAMload(object):
    def setupUi(self, CPUloadRAMload):
        if not CPUloadRAMload.objectName():
            CPUloadRAMload.setObjectName(u"CPUloadRAMload")
        CPUloadRAMload.resize(444, 375)
        self.verticalLayout = QVBoxLayout(CPUloadRAMload)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(CPUloadRAMload)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.spinBox = QSpinBox(CPUloadRAMload)
        self.spinBox.setObjectName(u"spinBox")

        self.horizontalLayout.addWidget(self.spinBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(CPUloadRAMload)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit = QLineEdit(CPUloadRAMload)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(CPUloadRAMload)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit_2 = QLineEdit(CPUloadRAMload)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_3.addWidget(self.lineEdit_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(CPUloadRAMload)

        QMetaObject.connectSlotsByName(CPUloadRAMload)
    # setupUi

    def retranslateUi(self, CPUloadRAMload):
        CPUloadRAMload.setWindowTitle(QCoreApplication.translate("CPUloadRAMload", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("CPUloadRAMload", u"\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0434\u0435\u0440\u0436\u043a\u0438", None))
        self.label_2.setText(QCoreApplication.translate("CPUloadRAMload", u"CPU load", None))
        self.label_3.setText(QCoreApplication.translate("CPUloadRAMload", u"RAM load", None))
    # retranslateUi

