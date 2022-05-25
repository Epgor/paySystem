from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import datetime

class PayPdfGenerator:
    def __init__(self):
        pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
        self.date = datetime.date.today()
        self.time = datetime.datetime.now()
        self.hour = str(self.time.hour)
        if len(self.hour)==1:
            self.hour = "0"+self.hour
        self.minutes = str(self.time.minute)
        if len(self.minutes)==1:
            self.minutes = "0"+self.minutes
        self.second = str(self.time.minute)
        if len(self.second)==1:
            self.second = "0"+self.second 
        self.hourP = f"{str(self.hour)}:{str(self.minutes)}:{str(self.second)}" 
        self.stanowisko = "Senior"
        self.wymiarPracy = "Cały Etat"
        self.lataPracy = "12"
        self.nadgodziny = "50"
        self.delegacjaGodz = "30"
        self.dodatkoweKoszty = "500"
        self.uwagi = "-34"
        self.wynikDziałania = ""
        self.platnoscDiety = ""
        
        
    def konfiguracja(self, stanowisko, wymiarPracy, lataPracy, nadgodziny,\
         delegacjaGodz, dodatkoweKoszty, uwagi, diety):
        self.stanowisko = str(stanowisko)
        self.wymiarPracy = str(wymiarPracy)
        self.lataPracy = str(lataPracy)
        self.nadgodziny = str(nadgodziny)
        self.delegacjaGodz = str(delegacjaGodz)
        self.dodatkoweKoszty = str(dodatkoweKoszty)
        self.uwagi = str(uwagi)
        self.platnoscDiety = str(diety)

    def wynik(self, text):
        self.wynikDziałania = text

    def printPdf(self):
        
        self.canvas = canvas.Canvas("raport.pdf", pagesize=letter)
        self.canvas.setLineWidth(.3)
        self.canvas.setFont('Helvetica', 20)

        self.canvas.drawString(275,730,'RAPORT')
        self.canvas.setFont('Helvetica', 16)
        self.canvas.drawString(150,700,'System estymowanych pensji pracowników')
        self.canvas.line(50,695,550,695)
        self.canvas.setFont('Vera', 12)
        self.canvas.drawString(500,750,str(self.date))
        self.canvas.drawString(510,738, self.hourP)
        self.canvas.line(480,735,580,735)
        self.canvas.line(480,763,580,763)
        self.canvas.drawString(90,670,"Stanowisko: ")
        self.canvas.drawString(400, 670, self.stanowisko)
        self.canvas.line(50,660,550,660)
        self.canvas.drawString(90,640,"Wymiar Pracy: ")
        self.canvas.drawString(400, 640, self.wymiarPracy)
        self.canvas.line(50,630,550,630)
        self.canvas.drawString(90,610,"Lata Pracy: ")
        self.canvas.drawString(400, 610, self.lataPracy)
        self.canvas.line(50,600,550,600)
        self.canvas.drawString(90,580,"Nadgodziny: ")
        self.canvas.drawString(400, 580, self.nadgodziny)
        self.canvas.line(50,570,550,570)
        self.canvas.drawString(90,550,"Delegacje: ")

        self.canvas.drawString(90,520,"Liczba godzin w delegacji: ")
        self.canvas.drawString(400, 520, self.delegacjaGodz)
        self.canvas.drawString(90,490,"Płatność diety: ")
        self.canvas.drawString(400, 490, self.platnoscDiety+"%")
        self.canvas.drawString(90,460,"Dodatkowe koszty poniesione przez pracownika: ")
        self.canvas.drawString(400, 460, self.dodatkoweKoszty)
        self.canvas.line(50,450,550,450)

        self.canvas.drawString(90,430,"Potrącenia i dodatki: ")
        self.canvas.drawString(90,400,"Bilans pochwał/uwag: ")
        self.canvas.drawString(400,400, self.uwagi)
        self.canvas.line(50,390,550,390)
        self.canvas.line(50,385,550,385)

        #################################
        if (self.wynikDziałania != ""):
            lista = self.wynikDziałania.split('\n')
            wysokosc = 360
            for linia in lista[11:]:
                if linia.endswith(".0"):
                    linia = linia [:-2]
                self.canvas.drawString(90, wysokosc, str(linia))
                wysokosc -= 30



        self.canvas.save()




