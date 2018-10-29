from PyQt4.QtGui import*
from PyQt4.QtCore import*
class tablo(QDialog):
    def __init__(self,ebeveyn=None):
        super(tablo,self).__init__(ebeveyn)
        self.initUI()
    def initUI(self):
        self.setWindowTitle("Tablo")
        grid=QGridLayout()
        self.setLayout(grid)
        sozluk={"Adı":["Can","Semih","Büşra"],"Bolum":["YBS","YBS","iktisat"],"Soyadı":["Aydın","Yarar","Demirgüreşçi"],}
        table=QTableWidget(self)
        table.setRowCount(3)
        table.setColumnCount(3)
        liste=[]
        for a, key in enumerate(sorted(sozluk.keys())):
            liste.append(key)
            for b, item in enumerate(sozluk[key]):
                yeniItem=QTableWidgetItem(item)
                table.setItem(a,b,yeniItem)
        table.setHorizontalHeaderLabels(liste)
        grid.addWidget(table,0,0)
        self.show()
uyg=QApplication([])
pencere=tablo()
pencere.show()
uyg.exec_()
