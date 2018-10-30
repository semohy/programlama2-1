import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class AnaPencere(QMainWindow):
    def __init__(self,p=None):
        super (AnaPencere,self).__init__(p)
        self.setWindowTitle("logo muhasebe uygulamaları")
        self.setGeometry(200,200,800,400)
        self.menuEkleme()
        self.form_widget=FormWidget(self)
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
        super(FormWidget,self).__init__(p)
        frame=QFrame()
        frame.setFrameStyle(QFrame.Panel)
        frame2=QFrame()
        frame2.setFrameStyle(QFrame.Panel)

        fisWidget=QWidget()
        fisNo=QLineEdit()
        fisTarih=QLineEdit()
        fisGetir=QPushButton()
        formLayout=QFormLayout()
        formLayout.addRow("fiş no:",fisNo)
        formLayout.addRow("fiş tarihi:",fisTarih)
        fisWidget.setLayout(formLayout)
        fisWidget.show()

        dockWidget=QDockWidget("fiş no ya göre göster",self)
        dockWidget.setFeatures(dockWidget.NoDockWidgetFeatures)
        dockWidget.setWidget(fisWidget)

        izgara=QGridLayout()
        izgara.addWidget(dockWidget)
        frame.setLayout(izgara)

        yatay=QGridLayout()
        yatay.addWidget(frame)
        yatay.setAlignment(Qt.AlignLeft)

        ozelKodWidget=QWidget()
        ozelKod=QLineEdit()
        yetkiKod=QLineEdit()
        ozelKodGoster=QPushButton("göster")
        formLayout2=QFormLayout()
        formLayout2.addRow("özel kod:",ozelKod)
        formLayout2.addRow("yetki kod",yetkiKod)
        formLayout2.addRow(ozelKodGoster)
        ozelKodWidget.setLayout(formLayout2)
        ozelKodWidget.show()
        
uyg=QApplication(sys.argv)
pencere=AnaPencere()
pencere.show()
uyg.exec_
