import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class AnaPencere(QMainWindow):
    def __init__(self,p=None):
        super (AnaPencere,self).__init__(p)
        self.setWindowTitle("logo muhasebe uygulamaları")
        self.setGeometry(200,200,800,400)
        self.menuEkleme()
        self.form_widget=FromWidget(self)
        self.setCentralWidget(self.form_widget)
        
    def menuEkleme(self):
        menubar=self.menuBar()
        menubar=self.menuBar()
        stokMenu=menubar.addMenu("&stok")
        stokEkle=stokMenu.addAction("&stok ekle")
        stokCikar=stokMenu.addAction("&stok çıkar")
        stokGoster=stokMenu.addAction("&stok göster")
        siparisMenu=menubar.addMenu("&sipariş")
        faturaMenu=menubar.addMenu("&fatura")
        cariMenu=menubar.addMenu("&cari hesap")
        kasaMenu=menubar.addMenu("kasa")
        bankaMenu=menubar.addMenu("&banka")
        cekMenu=menubar.addMenu("&çek/senet")
        topluMenu=menubar.addMenu("&toplu işlemler")
        sistemMenu=menubar.addMenu("&sistem işlemler")

class FormWidget(QWidget):
    def __init__(self,p=None):
        super(FromWidget,self).__init(p)
        frame=QFrame()
        frame.setFrameStyle(QFrame.Panel)
        frame2=QFrame()
        frame2.setFrameStyle(QFrame.Panel)

        fisWidgwet=QWidget()
        fisNo=QLineEdit()
        fisTarih=QLineEdit()
        fisGetir=QPushButton()
        fromLayout=QFromLayout()
        fromLayout.addRow("fiş no:",fisNo)
        fromLayout.addRow("fiş tarihi:",fisTarih)
        fisWidget.setLayout(fromLayout)
        fisWidget.show()

        dockWidget=QDockWidget("fiş no ya göre göster",self)
        dockWidget.setFeatures(dockWidget.NoDockWidgetFeatures)
        dockWidget.setWidget(fisWidget)

        izgara=QGridLayout()
        izgara.addWidget(dockWidget)
        frame.setLayout(izgara)

        yatay=QGridLayout()
        yatay.addWidget(izgara)
        yatay.setAlignment(Qt.AlignLeft)

        ozelKodWidget=QWidget()
        ozelKod=QLineEdit()
        yetkiKod=QLineEdit()
        ozelKodGoster=QPushButton("göster")
        fromLayout2=QFromLayout()
        fromLayout2.addRow("özel kod:",ozelKod)
        fromLayout2.addRow("yetki kod",yetkiKod)
        fromLayout2.addRow(ozelKodGoster)
        ozelKodWidget.setLayout(fromLayout2)
        ozelKodWidget.show()
        
uyg=QApplication(sys.argv)
pencere=AnaPencere()
pencere.show()
uyg.exec_
