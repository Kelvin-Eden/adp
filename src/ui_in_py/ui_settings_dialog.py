# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settins_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 10pt \"Lucida Sans Unicode\";")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.exportFolderLabel = QLabel(Dialog)
        self.exportFolderLabel.setObjectName(u"exportFolderLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exportFolderLabel.sizePolicy().hasHeightForWidth())
        self.exportFolderLabel.setSizePolicy(sizePolicy)
        self.exportFolderLabel.setMaximumSize(QSize(86, 20))

        self.horizontalLayout.addWidget(self.exportFolderLabel)

        self.folderPathLineEdit = QLineEdit(Dialog)
        self.folderPathLineEdit.setObjectName(u"folderPathLineEdit")
        self.folderPathLineEdit.setMinimumSize(QSize(160, 26))

        self.horizontalLayout.addWidget(self.folderPathLineEdit)

        self.chooseFolderBtn = QPushButton(Dialog)
        self.chooseFolderBtn.setObjectName(u"chooseFolderBtn")
        sizePolicy.setHeightForWidth(self.chooseFolderBtn.sizePolicy().hasHeightForWidth())
        self.chooseFolderBtn.setSizePolicy(sizePolicy)
        self.chooseFolderBtn.setMaximumSize(QSize(75, 28))
        self.chooseFolderBtn.setStyleSheet(u"background-color: rgb(86, 86, 86);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.chooseFolderBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.exportFolderLabel.setText(QCoreApplication.translate("Dialog", u"Export folder:", None))
        self.chooseFolderBtn.setText(QCoreApplication.translate("Dialog", u"...", None))
    # retranslateUi

