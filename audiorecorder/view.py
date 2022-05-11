# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'audiorecorder.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QFormLayout, QLabel,
                               QLineEdit, QProgressBar, QPushButton, QSizePolicy,
                               QSpinBox, QWidget)


class Ui_main_widget(object):
    def setupUi(self, main_widget):
        if not main_widget.objectName():
            main_widget.setObjectName(u"main_widget")
        main_widget.resize(370, 274)
        self.formLayoutWidget = QWidget(main_widget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 351, 171))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.url_label = QLabel(self.formLayoutWidget)
        self.url_label.setObjectName(u"url_label")
        font = QFont()
        font.setPointSize(14)
        self.url_label.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.url_label)

        self.url_line_edit = QLineEdit(self.formLayoutWidget)
        self.url_line_edit.setObjectName(u"url_line_edit")
        self.url_line_edit.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.url_line_edit)

        self.length_label = QLabel(self.formLayoutWidget)
        self.length_label.setObjectName(u"length_label")
        self.length_label.setFont(font)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.length_label)

        self.length_field = QSpinBox(self.formLayoutWidget)
        self.length_field.setObjectName(u"length_field")
        self.length_field.setFont(font)
        self.length_field.setMinimum(1)
        self.length_field.setMaximum(200)
        self.length_field.setValue(10)
        self.length_field.setDisplayIntegerBase(10)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.length_field)

        self.size_label = QLabel(self.formLayoutWidget)
        self.size_label.setObjectName(u"size_label")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.size_label)

        self.size_spin_box = QSpinBox(self.formLayoutWidget)
        self.size_spin_box.setObjectName(u"size_spin_box")
        self.size_spin_box.setMinimum(32)
        self.size_spin_box.setMaximum(320)
        self.size_spin_box.setSingleStep(8)
        self.size_spin_box.setStepType(QAbstractSpinBox.DefaultStepType)
        self.size_spin_box.setDisplayIntegerBase(10)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.size_spin_box)

        self.file_name_label = QLabel(self.formLayoutWidget)
        self.file_name_label.setObjectName(u"file_name_label")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.file_name_label)

        self.file_name_line_edit = QLineEdit(self.formLayoutWidget)
        self.file_name_line_edit.setObjectName(u"file_name_line_edit")
        self.file_name_line_edit.setMaxLength(40)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.file_name_line_edit)

        self.progress_bar = QProgressBar(main_widget)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setGeometry(QRect(10, 220, 351, 23))
        self.progress_bar.setValue(0)
        self.progress_label = QLabel(main_widget)
        self.progress_label.setObjectName(u"progress_label")
        self.progress_label.setGeometry(QRect(10, 250, 58, 16))
        self.start_button = QPushButton(main_widget)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setGeometry(QRect(99, 190, 171, 32))

        self.retranslateUi(main_widget)

        QMetaObject.connectSlotsByName(main_widget)

    # setupUi

    def retranslateUi(self, main_widget):
        main_widget.setWindowTitle(QCoreApplication.translate("main_widget", u"Strickers Audiorecorder", None))
        self.url_label.setText(QCoreApplication.translate("main_widget", u"URL-Quelle:", None))
        self.url_line_edit.setPlaceholderText(
            QCoreApplication.translate("main_widget", u"https://mp3.example.com/example.mp3", None))
        self.length_label.setText(QCoreApplication.translate("main_widget", u"L\u00e4nge der Aufnahme (sek):", None))
        self.size_label.setText(QCoreApplication.translate("main_widget", u"Blockgr\u00f6\u00dfe:", None))
        self.file_name_label.setText(QCoreApplication.translate("main_widget", u"Dateiname:", None))
        self.file_name_line_edit.setPlaceholderText(QCoreApplication.translate("main_widget", u"my-audio.mp3", None))
        self.progress_label.setText("")
        self.start_button.setText(QCoreApplication.translate("main_widget", u"STARTEN", None))
    # retranslateUi
