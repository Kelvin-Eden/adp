# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'final_master.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 835)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1200, 835))
        MainWindow.setMaximumSize(QSize(16777215, 835))
        MainWindow.setStyleSheet(u"background-color: rgb(221, 221, 221);")
        self.load_stg_action = QAction(MainWindow)
        self.load_stg_action.setObjectName(u"load_stg_action")
        font = QFont()
        font.setFamilies([u"Maven Pro"])
        font.setPointSize(10)
        self.load_stg_action.setFont(font)
        self.settings_action = QAction(MainWindow)
        self.settings_action.setObjectName(u"settings_action")
        self.settings_action.setFont(font)
        self.about_action = QAction(MainWindow)
        self.about_action.setObjectName(u"about_action")
        self.about_action.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_6 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.left_frame = QFrame(self.centralwidget)
        self.left_frame.setObjectName(u"left_frame")
        self.left_frame.setMinimumSize(QSize(0, 41))
        self.left_frame.setMaximumSize(QSize(500, 772))
        self.left_frame.setToolTipDuration(7)
        self.left_frame.setStyleSheet(u"background-color: rgb(29, 160, 156);")
        self.left_frame.setFrameShape(QFrame.StyledPanel)
        self.left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit = QLineEdit(self.left_frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 41))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 300 11pt \"Noto Sans Regular\";")

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.listWidget = QListWidget(self.left_frame)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Noto Sans\";\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_2.addWidget(self.listWidget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, -1, 20, -1)
        self.clearBtn = QPushButton(self.left_frame)
        self.clearBtn.setObjectName(u"clearBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.clearBtn.sizePolicy().hasHeightForWidth())
        self.clearBtn.setSizePolicy(sizePolicy1)
        self.clearBtn.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Maven Pro\";")

        self.horizontalLayout.addWidget(self.clearBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.predictBtn = QPushButton(self.left_frame)
        self.predictBtn.setObjectName(u"predictBtn")
        sizePolicy1.setHeightForWidth(self.predictBtn.sizePolicy().hasHeightForWidth())
        self.predictBtn.setSizePolicy(sizePolicy1)
        self.predictBtn.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Maven Pro\";")

        self.horizontalLayout.addWidget(self.predictBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(84, -1, 50, -1)
        self.progressBar = QProgressBar(self.left_frame)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy2)
        self.progressBar.setMinimumSize(QSize(0, 16))
        self.progressBar.setMaximumSize(QSize(16777215, 21))
        self.progressBar.setStyleSheet(u"font: 500 11pt \"Maven Pro\";")
        self.progressBar.setValue(24)

        self.horizontalLayout_2.addWidget(self.progressBar)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.status_label = QLabel(self.left_frame)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setMaximumSize(QSize(61, 18))
        self.status_label.setStyleSheet(u"background-color: rgb(29, 160, 156);\n"
"color: rgb(255, 255, 255);\n"
"font: 500 11pt \"Maven Pro\";")
        self.status_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.status_label)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_6.addWidget(self.left_frame)

        self.middle_frame = QFrame(self.centralwidget)
        self.middle_frame.setObjectName(u"middle_frame")
        self.middle_frame.setStyleSheet(u"background-color: rgb(29, 160, 156);")
        self.middle_frame.setFrameShape(QFrame.StyledPanel)
        self.middle_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.middle_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.results_tabWidget = QTabWidget(self.middle_frame)
        self.results_tabWidget.setObjectName(u"results_tabWidget")
        self.results_tabWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";")
        self.possibles_tab = QWidget()
        self.possibles_tab.setObjectName(u"possibles_tab")
        self.results_tabWidget.addTab(self.possibles_tab, "")
        self.final_tab = QWidget()
        self.final_tab.setObjectName(u"final_tab")
        self.results_tabWidget.addTab(self.final_tab, "")

        self.verticalLayout_3.addWidget(self.results_tabWidget)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(50)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.exportBtn = QPushButton(self.middle_frame)
        self.exportBtn.setObjectName(u"exportBtn")
        sizePolicy1.setHeightForWidth(self.exportBtn.sizePolicy().hasHeightForWidth())
        self.exportBtn.setSizePolicy(sizePolicy1)
        self.exportBtn.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Maven Pro\";")

        self.horizontalLayout_4.addWidget(self.exportBtn)

        self.saveBtn = QPushButton(self.middle_frame)
        self.saveBtn.setObjectName(u"saveBtn")
        sizePolicy1.setHeightForWidth(self.saveBtn.sizePolicy().hasHeightForWidth())
        self.saveBtn.setSizePolicy(sizePolicy1)
        self.saveBtn.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Maven Pro\";")

        self.horizontalLayout_4.addWidget(self.saveBtn)

        self.stgBtn = QPushButton(self.middle_frame)
        self.stgBtn.setObjectName(u"stgBtn")
        sizePolicy1.setHeightForWidth(self.stgBtn.sizePolicy().hasHeightForWidth())
        self.stgBtn.setSizePolicy(sizePolicy1)
        self.stgBtn.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Maven Pro\";")

        self.horizontalLayout_4.addWidget(self.stgBtn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_6.addWidget(self.middle_frame)

        self.right_frame = QFrame(self.centralwidget)
        self.right_frame.setObjectName(u"right_frame")
        self.right_frame.setMaximumSize(QSize(315, 16777215))
        self.right_frame.setStyleSheet(u"background-color: rgb(29, 160, 156);")
        self.right_frame.setFrameShape(QFrame.StyledPanel)
        self.right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.right_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.supported_tabWidget = QTabWidget(self.right_frame)
        self.supported_tabWidget.setObjectName(u"supported_tabWidget")
        self.supported_tabWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.supported_tabWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Segoe UI\";")
        self.diseases_tab = QWidget()
        self.diseases_tab.setObjectName(u"diseases_tab")
        self.supported_tabWidget.addTab(self.diseases_tab, "")
        self.criteria_tab = QWidget()
        self.criteria_tab.setObjectName(u"criteria_tab")
        self.supported_tabWidget.addTab(self.criteria_tab, "")

        self.verticalLayout_4.addWidget(self.supported_tabWidget)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, -1, -1, -1)
        self.logoLabel = QLabel(self.right_frame)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setMinimumSize(QSize(51, 21))
        self.logoLabel.setMaximumSize(QSize(51, 21))
        self.logoLabel.setStyleSheet(u"background-color: rgb(29, 160, 156);\n"
"color: rgb(255, 255, 255);\n"
"font: 500 11pt \"Maven Pro\";")

        self.horizontalLayout_5.addWidget(self.logoLabel)

        self.email_label = QLabel(self.right_frame)
        self.email_label.setObjectName(u"email_label")
        self.email_label.setMaximumSize(QSize(141, 16))
        self.email_label.setStyleSheet(u"background-color: rgb(29, 160, 156);\n"
"color: rgb(255, 255, 255);\n"
"font: 500 11pt \"Maven Pro\";")

        self.horizontalLayout_5.addWidget(self.email_label)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_6.addWidget(self.right_frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 35))
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy3)
        self.menubar.setMinimumSize(QSize(0, 35))
        self.menubar.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Maven Pro Medium"])
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(False)
        self.menubar.setFont(font1)
        self.menubar.setCursor(QCursor(Qt.ArrowCursor))
        self.menubar.setFocusPolicy(Qt.NoFocus)
        self.menubar.setStyleSheet(u"font: 500 11pt \"Maven Pro Medium\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(100, 100, 100);")
        self.menu_MENU = QMenu(self.menubar)
        self.menu_MENU.setObjectName(u"menu_MENU")
        self.menu_MENU.setFont(font1)
        self.menu_MENU.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_MENU.setLayoutDirection(Qt.LeftToRight)
        self.menu_MENU.setStyleSheet(u"")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setToolTipDuration(-1)
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_MENU.menuAction())
        self.menu_MENU.addAction(self.load_stg_action)
        self.menu_MENU.addAction(self.settings_action)
        self.menu_MENU.addAction(self.about_action)

        self.retranslateUi(MainWindow)

        self.results_tabWidget.setCurrentIndex(1)
        self.supported_tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.load_stg_action.setText(QCoreApplication.translate("MainWindow", u"&Update STG", None))
        self.settings_action.setText(QCoreApplication.translate("MainWindow", u"&Settings", None))
        self.about_action.setText(QCoreApplication.translate("MainWindow", u"&About", None))
#if QT_CONFIG(tooltip)
        self.left_frame.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lineEdit.setText("")
        self.clearBtn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
#if QT_CONFIG(tooltip)
        self.predictBtn.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.predictBtn.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.predictBtn.setText(QCoreApplication.translate("MainWindow", u"Predict", None))
        self.status_label.setText(QCoreApplication.translate("MainWindow", u" Done!", None))
        self.results_tabWidget.setTabText(self.results_tabWidget.indexOf(self.possibles_tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.results_tabWidget.setTabText(self.results_tabWidget.indexOf(self.final_tab), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.exportBtn.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.saveBtn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.stgBtn.setText(QCoreApplication.translate("MainWindow", u"STG", None))
        self.supported_tabWidget.setTabText(self.supported_tabWidget.indexOf(self.diseases_tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.supported_tabWidget.setTabText(self.supported_tabWidget.indexOf(self.criteria_tab), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.logoLabel.setText(QCoreApplication.translate("MainWindow", u"  logo", None))
        self.email_label.setText(QCoreApplication.translate("MainWindow", u"eden.tz@yahoo.com", None))
        self.menu_MENU.setTitle(QCoreApplication.translate("MainWindow", u"&Menu", None))
#if QT_CONFIG(tooltip)
        self.statusbar.setToolTip("")
#endif // QT_CONFIG(tooltip)
    # retranslateUi

