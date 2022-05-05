from payFacts import *

class WyplataSilnik(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.wyplata=1
        self.godz=1
        self.pln=1
        self.dodatek=1

    @Rule(AS.ileGodz << GodzinPracy(godz=P(lambda x: x > 0)))
    def zlicz_godziny(self, ileGodz):
        self.setGodz(ileGodz['godz'])
        print("są godziny", ileGodz['godz'])

    @Rule(AS.zaGodz << PensjaNaGodzine(zl=P(lambda x: x > 0)))
    def przelicz_pensje(self, zaGodz):
        self.setStawka(zaGodz['zl'])
        print("za godzine: ", zaGodz['zl'])
        
    @Rule(LataPracy(lat=P(lambda x: x > 15)))
    def premia_za_bd_lata(self):
        self.wyplata *= 1.15
        print("bardzo długo pracuje")
        self.ile_wyplaty()

    @Rule(LataPracy(lat=P(lambda x: x >= 10) & P(lambda x: x <= 15)))
    def premia_za_d_lata(self):
        self.wyplata *= 1.10
        print("długo pracuje")
        self.ile_wyplaty()

    @Rule(LataPracy(lat=P(lambda x: x >= 5) & P(lambda x: x < 10)))
    def premia_za_sd_lata(self):
        self.wyplata *= 1.05
        print("średnio długo pracuje")
        self.ile_wyplaty()

    @Rule(LataPracy(lat=P(lambda x: x >= 2) & P(lambda x: x < 5)))
    def premia_za_s_lata(self):
        self.wyplata *= 1.02
        print("średnio pracuje : mid")
        self.ile_wyplaty()

    @Rule(LataPracy(lat=P(lambda x: x >= 1) & P(lambda x: x < 2)))
    def premia_za_k_lata(self):
        self.wyplata *= 1.01
        print("krótko pracuje")
        self.ile_wyplaty()

    @Rule(Pochwala(poch=1) | Pochwala(poch=2))
    def dodaj_premie_1(self):
        self.dodatek +=200
        print("jest dodatek")

    def setGodz(self, godz):
        self.godz = godz
    def setStawka(self, pln):
        self.pln = pln
    def setWyplata(self):
        self.wyplata *= self.godz * self.pln
    def ile_wyplaty(self):
        self.setWyplata()
        print(self.wyplata)