from __future__ import division
from PyQt4.QtGui import *
from PyQt4.QtCore import *
 
 
class yakıtHesapla(QWidget):
    def __init__(self, parent=None):
        super(yakıtHesapla, self).__init__(parent)
 
        self.metin = "<center>tükeilen yakıt tutarı</center>"
 
        self.grid = QGridLayout()
        self.baslik = QLabel(self.metin)
        self.yol = QLabel('gideceğiniz yol')
        self.yakıt = QLabel('yakıt fiyatı ')
        self.km = QLabel('100 km de tüketilen yakıt ')
        self.yoldeger = QLineEdit()
        self.yakıtdeger = QLineEdit()
        self.kmDeger = QLineEdit()
        self.sonuc = QLabel('toplam tutar ')
        self.sonucDeger = QLabel('0.00')
        self.hesapla = QPushButton('Hesapla')
 
        self.grid.addWidget(self.baslik, 0, 0, 1, 2)
        self.grid.addWidget(self.yol, 1, 0)
        self.grid.addWidget(self.yoldeger, 1, 1)
        self.grid.addWidget(self.yakıt, 2, 0)
        self.grid.addWidget(self.yakıtdeger, 2, 1)
        self.grid.addWidget(self.km, 3, 0)
        self.grid.addWidget(self.kmDeger, 3, 1)
        self.grid.addWidget(self.sonuc, 4, 0)
        self.grid.addWidget(self.sonucDeger, 4, 1)
        self.grid.addWidget(self.hesapla, 5, 0, 1, 2)
 
        self.connect(self.hesapla, SIGNAL('pressed()'), self.hesapYap)
 
        self.setLayout(self.grid)
        self.setWindowTitle("akaryakıt hesaplama")
 
    def hesapYap(self):
        ortalama = 0
        try:
            gYol = int(self.yoldeger.text())
            yFiyat = int(self.yakıtdeger.text())
            tüketilen = int(self.kmDeger.text())
            ortalama = (yFiyat * gYol)/100
        except:
            self.sonucDeger.setText('<span style="color: red;">Tam sayi giriniz!</span>')
            return
        self.sonucDeger.setText('<b>%0.2f</b>' % ortalama)
 
 
uyg = QApplication([])
pencere=yakıtHesapla()
pencere.show()
