from PyQt4.QtGui import *
from PyQt4.QtCore import * 
class devirHızıHesaplama (QDialog):  
    def __init__(self,ebeveyn=None):
        super(devirHızıHesaplama,self).__init__(ebeveyn)
        grid=QGridLayout()   

        grid.addWidget(QLabel("dönembaşı çalışan sayısı:"),0,0)
        self.dbcs=QLineEdit()
        grid.addWidget(self.dbcs,0,1)

        grid.addWidget(QLabel("dönemsonu çalışan sayısı:"),1,0)
        self.dscs=QLineEdit()
        grid.addWidget(self.dscs,1,1)

        grid.addWidget(QLabel("işten çıkarılan çalışan sayısı:"),2,0)
        self.iccs=QLineEdit()
        grid.addWidget(self.iccs,2,1)

        grid.addWidget(QLabel("sonuç"),3,0)  
        self.sonuc=QLabel("")  
        grid.addWidget(self.sonuc,3,1)
        
        hesapla=QPushButton("hesapla")
        grid.addWidget(hesapla,4,1)
        self.connect(hesapla,SIGNAL("pressed()"),self.hesaplama)

        self.setLayout(grid)
        self.setWindowTitle("personel devir hızı hesaplama")

    def hesaplama(self):
        db=int(self.dbcs.text())
        ds=int(self.dscs.text())
        ic=int(self.iccs.text())
        pdh=ic/((db+ds)/2)*100
        self.sonuc.setText('<b>%0.lf</b>'%pdh)
uygulama=QApplication([])
pencere=devirHızıHesaplama()
pencere.show()

        

        

        
