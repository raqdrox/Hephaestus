# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledxGKwOl.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject,QThread, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import ScraperWorker
import time
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        ui = Ui_MainWindow(self)

class Ui_MainWindow(QMainWindow):
    def __init__(self,win):
        super().__init__()
        self.thread = QThread()
        self.worker = None
  
        # calling method
        self.setupUi(win)
  
        # showing all the widgets
        self.show()

    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setFixedSize(380, 247)
        font = QFont()
        
        font.setPointSize(9)
        MainWindow.setFont(font)

        self.spinBox = QSpinBox(self)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(250, 30, 101, 31))
        font1 = QFont()
        font1.setPointSize(14)
        self.spinBox.setFont(font1)
        self.pushButton = QPushButton("CLICK", self)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(120, 110, 141, 41))
        font2 = QFont()
        font2.setPointSize(17)
        self.pushButton.setFont(font2)
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 191, 51))
        font3 = QFont()
        font3.setPointSize(16)
        self.label.setFont(font3)
        self.progressBar = QProgressBar(self)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(30, 170, 311, 23))
        self.progressBar.setFont(font)
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.label_2 = QLabel(self)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 70, 191, 31))
        self.label_2.setFont(font3)

        self.label_3 = QLabel(self)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 180, 200, 60))
        self.label_3.setFont(font3)

        self.plainTextEdit = QPlainTextEdit(self)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(250, 70, 104, 31))
        font4 = QFont()
        font4.setPointSize(11)
        self.plainTextEdit.setFont(font4)

        MainWindow.setCentralWidget(self)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 380, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.threadstart)
        self.retranslateUi(MainWindow)
        
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Screenshot Scraper By Paradox", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Number of results", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Filename Prefix", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Status : Stopped", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"Image", None))
    # retranslateUi

    def threadstart(self):
        self.threadstop()
        self.worker = ScraperWorker.ScraperThread(self.spinBox.value(),self.plainTextEdit.toPlainText())
        self.worker.moveToThread(self.thread)
        self.worker.progress.connect(self.progbar)
        self.thread.started.connect(self.worker.loop)
        self.worker.finished.connect(self.threadstop)
        self.thread.start()
        self.label_3.setText("Status : Running")

    def threadstop(self):
        if self.worker is not None:
            self.worker.stop()
        self.thread.quit()
        self.thread.wait()
        self.progbar(0)
        self.worker = None
        self.label_3.setText("Status : Stopped")

    def progbar(self,i):
        self.progressBar.setValue(i)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())