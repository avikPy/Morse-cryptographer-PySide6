from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

from logic_morze import *

class Ui_MorsePro(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(712, 315)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"    background-color: #2f2f2f;\n"
"}\n"
"QTextEdit {\n"
"    background-color: #565656;\n"
"    color: #0d0e0d;\n"
"}\n"
"QPushButton {\n"
"    color: #4d7fa3;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #5b5b5b;\n"
"}\n"
"QCheckBox {\n"
"    color: #6194b8\n"
"}\n"
"QLabel {\n"
"    color: #63a696\n"
"}")
        self.input_txte = QTextEdit(self.centralwidget)
        self.input_txte.setObjectName(u"input_txte")
        self.input_txte.setGeometry(QRect(20, 10, 671, 81))
        font = QFont()
        font.setFamilies([u"System"])
        font.setPointSize(14)
        font.setBold(True)
        self.input_txte.setFont(font)
        self.output_txte = QTextEdit(self.centralwidget)
        self.output_txte.setObjectName(u"output_txte")
        self.output_txte.setGeometry(QRect(20, 210, 671, 81))
        font1 = QFont()
        font1.setFamilies([u"System"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.output_txte.setFont(font1)
        self.output_txte.setReadOnly(True)
        self.fr_textcode = QCheckBox(self.centralwidget)
        self.fr_textcode.setObjectName(u"fr_textcode")
        self.fr_textcode.setGeometry(QRect(20, 100, 131, 21))
        font2 = QFont()
        font2.setFamilies([u"System"])
        font2.setPointSize(11)
        font2.setBold(True)
        self.fr_textcode.setFont(font2)
        self.fr_codeKir = QCheckBox(self.centralwidget)
        self.fr_codeKir.setObjectName(u"fr_codeKir")
        self.fr_codeKir.setGeometry(QRect(20, 130, 161, 21))
        self.fr_codeKir.setFont(font2)
        self.fr_codeLat = QCheckBox(self.centralwidget)
        self.fr_codeLat.setObjectName(u"fr_codeLat")
        self.fr_codeLat.setGeometry(QRect(20, 160, 161, 21))
        self.fr_codeLat.setFont(font2)
        self.start_btn = QPushButton(self.centralwidget)
        self.start_btn.setObjectName(u"start_btn")
        self.start_btn.setGeometry(QRect(444, 123, 181, 61))
        self.start_btn.setFont(font2)
        self.name_lbl = QLabel(self.centralwidget)
        self.name_lbl.setObjectName(u"name_lbl")
        self.name_lbl.setGeometry(QRect(230, 130, 191, 31))
        font3 = QFont()
        font3.setFamilies([u"Tahoma"])
        font3.setPointSize(17)
        font3.setBold(False)
        self.name_lbl.setFont(font3)
        self.watermark = QLabel(self.centralwidget)
        self.watermark.setObjectName(u"watermark")
        self.watermark.setGeometry(QRect(650, 291, 71, 20))
        self.watermark.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.start_btn.clicked.connect(self.do_cryp)
    
    def do_cryp(self):
        if not checked_duo(self.fr_codeKir, self.fr_codeLat, self.fr_textcode):
            if check(self.fr_textcode):
                self.text_to_code()
            elif check(self.fr_codeKir):
                self.code_to_kir()
            elif check(self.fr_codeLat):
                self.code_to_lat()
        else:
            self.output_txte.clear()
            self.output_txte.setText('Выберете фунцию корректно!')
            
            
    def text_to_code(self):
        text = self.input_txte.toPlainText()
        self.output_txte.clear()
        self.output_txte.setText(text2code(text=text))

    def code_to_kir(self):
        code = self.input_txte.toPlainText()
        self.output_txte.clear()
        self.output_txte.setText(code2kir(code=code))
        
    def code_to_lat(self):
        code = self.input_txte.toPlainText()
        self.output_txte.clear()
        self.output_txte.setText(code2lat(code=code))


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Morsepro byAvk", None))
        self.fr_textcode.setText(QCoreApplication.translate("MainWindow", u"From text to code", None))
        self.fr_codeKir.setText(QCoreApplication.translate("MainWindow", u"From code to Cyrillic", None))
        self.fr_codeLat.setText(QCoreApplication.translate("MainWindow", u"From the code to the Latin", None))
        self.start_btn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.name_lbl.setText(QCoreApplication.translate("MainWindow", u"MorsePro decoder", None))
        self.watermark.setText(QCoreApplication.translate("MainWindow", u"by Avik", None))


