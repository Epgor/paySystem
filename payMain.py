from payEngine import *
from io import StringIO 
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from payPdf import *


class Ui_Wypata(object):
    karma = 0
    text = ""
    def engineUi(self):
        #zmienne   
        self.text = ""
        stanowisko = self.listWidget.currentItem().text()
        etat = self.listWidget_2.currentItem().text()
        latPracy = self.spinBox_3.value()
        nadGodziny = self.spinBox_5.value()
        delegacjaGodz = self.spinBox.value()
        delegacjaProc = self.spinBox_2.value()
        kosztyDodatkowe = self.spinBox_4.value()
        #godzPracy = self.spinBox_2.value()
        #stawka = self.spinBox_3.value()

        #print(latPracy, godzPracy, stawka)     
        engine = WyplataSilnik()
        engine.reset()
        engine.declare(Stanowisko(stan=stanowisko), Etat(wymiar=etat), LataPracy(lat=latPracy),\
             Nadgodziny(godz=nadGodziny), Pochwala(poch=self.karma), DelegacjaGodz(godz=delegacjaGodz),
             DelegacjaDod(dod=kosztyDodatkowe), DelegacjaProc(proc=delegacjaProc))
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        print("Wstępne Ustawienia")
        print("==================")
        self.print_setup()
        print("==================")
        engine.run()
        engine.ile_wyplaty()
        sys.stdout = old_stdout
        self.text += mystdout.getvalue()
        self.textBrowser.setText(self.text)

    def setupUi(self, Wypata):
        Wypata.setObjectName("Wypata")
        Wypata.resize(881, 621)
        self.pushButton = QtWidgets.QPushButton(Wypata)
        self.pushButton.setGeometry(QtCore.QRect(790, 100, 80, 29))
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(Wypata)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 761, 171))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.listWidget = QtWidgets.QListWidget(self.layoutWidget)
        self.listWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.listWidget.setStyleSheet("selection-color: rgb(170, 0, 0);\n"
"")
        self.listWidget.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.SelectedClicked)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.listWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.listWidget.setMovement(QtWidgets.QListView.Static)
        self.listWidget.setFlow(QtWidgets.QListView.TopToBottom)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.verticalLayout_4.addWidget(self.listWidget)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.listWidget_2 = QtWidgets.QListWidget(self.layoutWidget)
        self.listWidget_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.listWidget_2.setStyleSheet("selection-color: rgb(170, 0, 0);\n"
"")
        self.listWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.SelectedClicked)
        self.listWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listWidget_2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.listWidget_2.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.listWidget_2.setMovement(QtWidgets.QListView.Static)
        self.listWidget_2.setFlow(QtWidgets.QListView.TopToBottom)
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.verticalLayout_3.addWidget(self.listWidget_2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout_2.addWidget(self.spinBox)
        self.spinBox_2 = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_2.setMaximum(100)
        self.spinBox.setMaximum(999)
        self.spinBox_2.setObjectName("spinBox_2")
        self.verticalLayout_2.addWidget(self.spinBox_2)
        self.spinBox_4 = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_4.setMaximum(999999999)
        self.spinBox_4.setObjectName("spinBox_4")
        self.verticalLayout_2.addWidget(self.spinBox_4)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.spinBox_3 = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_3.setMaximum(9999999)
        self.spinBox_3.setObjectName("spinBox_3")
        self.verticalLayout_5.addWidget(self.spinBox_3)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.spinBox_5 = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_5.setMaximum(9999999)
        self.spinBox_5.setObjectName("spinBox_5")
        self.verticalLayout_6.addWidget(self.spinBox_5)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_8.addWidget(self.label_8)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_8.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_8.addWidget(self.pushButton_2)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.layoutWidget1 = QtWidgets.QWidget(Wypata)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 230, 861, 371))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.textBrowser = QtWidgets.QTextBrowser(self.layoutWidget1)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_9.addWidget(self.textBrowser)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_9.addWidget(self.pushButton_4)

        self.retranslateUi(Wypata)
        QtCore.QMetaObject.connectSlotsByName(Wypata)
        Wypata.setTabOrder(self.listWidget, self.pushButton)
        Wypata.setTabOrder(self.pushButton, self.spinBox)
        Wypata.setTabOrder(self.spinBox, self.spinBox_2)
        Wypata.setTabOrder(self.spinBox_2, self.spinBox_3)
        Wypata.setTabOrder(self.spinBox_3, self.textBrowser)

    def retranslateUi(self, Wypata):
        _translate = QtCore.QCoreApplication.translate
        Wypata.setWindowTitle(_translate("Wypata", "Wyplata - System Ekspercki"))
        self.pushButton.setText(_translate("Wypata", "Oblicz"))
        self.label_4.setText(_translate("Wypata", "Typ pracownika"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Wypata", "Stażysta"))
        item = self.listWidget.item(1)
        item.setText(_translate("Wypata", "Młodszy Specjalista"))
        item = self.listWidget.item(2)
        item.setText(_translate("Wypata", "Specjalista"))
        item = self.listWidget.item(3)
        item.setText(_translate("Wypata", "Starszy Specjalista"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("Wypata", "Wymiar Pracy"))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("Wypata", "Cały Etat"))
        item = self.listWidget_2.item(1)
        item.setText(_translate("Wypata", "3/4 Etatu"))
        item = self.listWidget_2.item(2)
        item.setText(_translate("Wypata", "1/2 Etatu"))
        item = self.listWidget_2.item(3)
        item.setText(_translate("Wypata", "1/4 Etatu"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("Wypata", " Godzin Delegacji"))
        self.label_5.setText(_translate("Wypata", " Płatność Diety (w %)"))
        self.label_6.setText(_translate("Wypata", "Dodatkowe Koszty"))
        self.label_3.setText(_translate("Wypata", "Lata Pracy"))
        self.label_7.setText(_translate("Wypata", "Nadgodziny"))
        self.label_8.setText(_translate("Wypata", "Uwagi"))
        self.pushButton_3.setText(_translate("Wypata", "+"))
        self.pushButton_2.setText(_translate("Wypata", "-"))
        self.pushButton_4.setText(_translate("Wypata", "Generuj Raport"))

        self.listWidget.setCurrentRow(0)
        self.listWidget_2.setCurrentRow(0)

        self.pushButton.clicked.connect(self.engineUi)
        self.pushButton_3.clicked.connect(self.pochwala)
        self.pushButton_2.clicked.connect(self.uwaga)
        self.pushButton_4.clicked.connect(self.generujRaport)

    #def itemActivated_event(item):
    #    print(item.text())

    def print_window(self):
        text = ""
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        self.print_setup()
        sys.stdout = old_stdout
        text = mystdout.getvalue()
        self.textBrowser.setText(text)

    def print_setup(self):
        print("Stanowisko: ",self.listWidget.currentItem().text()) #stanowisko
        print("Etat: ",self.listWidget_2.currentItem().text()) #etat
        print("Godzin Delegacji: ",self.spinBox.value()) #godz delegacji
        print("Płatność diety w %: ",self.spinBox_2.value()) #platnosc diety
        print("Dodatkowe koszty poniesione przez pracnownika: ",self.spinBox_4.value()) #dodatkowe koszty
        print("Lata pracy: ",self.spinBox_3.value()) #lata pracy
        print("Liczba nadgodzin: ", self.spinBox_5.value()) #nadgodziny
        print("Bilans uwag/pochwał: ", self.karma)

    def pochwala(self):
        print("Pochwala")
        self.karma += 1
        self.print_window()
    
    def uwaga(self):
        print("Uwaga")
        self.karma -= 1
        self.print_window()

    def generujRaport(self):
        printer = PayPdfGenerator()
        printer.konfiguracja(self.listWidget.currentItem().text(),\
            self.listWidget_2.currentItem().text(), self.spinBox_3.value(), \
            self.spinBox_5.value(), self.spinBox.value(), \
            self.spinBox_4.value(), self.karma, self.spinBox_2.value())
        if (self.text != ""):
            printer.wynik(self.text)
        printer.printPdf()


    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Wypata = QtWidgets.QDialog()
    ui = Ui_Wypata()
    ui.setupUi(Wypata)
    Wypata.show()
    sys.exit(app.exec_())



"""Stanowiska np tester młodszy programista starszy programista
Senior iles na godzinę junior iles tester iles

Etat pol etatu cześć etatu zamiast liczby przepracowanych godzin

Stawka na godzinę związać ze stanowiskiem

Fakty gdzie są stanowiska premia doliczać delegacje 

Może być liczba lat pracy

Uwag i pochwał może być nieokreślona liczba

Przeliczyć czego więcej i policzyć albo bonus albo potrącenie

Generowane zestawienie raport wypisane wszystkie informacje zniżki zwyżki i kwota do wypłaty 

Podatki składka zdrowotna może"""