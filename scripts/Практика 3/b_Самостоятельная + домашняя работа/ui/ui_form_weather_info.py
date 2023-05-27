# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_form_weather_info.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(350, 350)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(350, 350))
        MainWindow.setMaximumSize(QSize(350, 350))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit_latitude = QLineEdit(self.centralwidget)
        self.lineEdit_latitude.setObjectName(u"lineEdit_latitude")
        self.lineEdit_latitude.setPlaceholderText("Пример: 59.57")

        self.horizontalLayout_2.addWidget(self.lineEdit_latitude)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit_longitude = QLineEdit(self.centralwidget)
        self.lineEdit_longitude.setObjectName(u"lineEdit_longitude")
        self.lineEdit_longitude.setPlaceholderText("Пример: 30.19")

        self.horizontalLayout.addWidget(self.lineEdit_longitude)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(12)
        font.setKerning(False)
        self.label_4.setFont(font)
        self.label_4.setTabletTracking(False)
        self.label_4.setTextFormat(Qt.AutoText)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.plainTextEdit_Inform = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_Inform.setObjectName(u"plainTextEdit_Inform")

        self.verticalLayout.addWidget(self.plainTextEdit_Inform)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.spinBox_delay = QSpinBox(self.centralwidget)
        self.spinBox_delay.setObjectName(u"spinBox_delay")

        self.horizontalLayout_3.addWidget(self.spinBox_delay)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_start = QPushButton(self.centralwidget)
        self.pushButton_start.setObjectName(u"pushButton_start")

        self.horizontalLayout_4.addWidget(self.pushButton_start)

        self.pushButton_finish = QPushButton(self.centralwidget)
        self.pushButton_finish.setObjectName(u"pushButton_finish")

        self.horizontalLayout_4.addWidget(self.pushButton_finish)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.label_5_status = QLabel(self.centralwidget)
        self.label_5_status.setObjectName(u"label_5_status")

        self.verticalLayout.addWidget(self.label_5_status)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 350, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Данные о погоде", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0448\u0438\u0440\u043e\u0442\u0443", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0434\u043e\u043b\u0433\u043e\u0442\u0443", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043f\u043e\u0433\u043e\u0434\u0435", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0432\u0440\u0435\u043c\u044f \u0437\u0430\u0434\u0435\u0440\u0436\u043a\u0438 ", None))
        self.pushButton_start.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u043f\u043e\u0442\u043e\u043a", None))
        self.pushButton_finish.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u043f\u043e\u0442\u043e\u043a", None))
        self.label_5_status.setText("")
    # retranslateUi

