from payFacts import *

class WyplataSilnik(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.wyplata=1
        self.dodatek=0
        print("Obliczanie pensji pracownika...")
    """
    @Rule(AS.ileGodz << GodzinPracy(godz=P(lambda x: x > 0)))
    def zlicz_godziny(self, ileGodz):
        self.setGodz(ileGodz['godz'])
        print("Pracownik przepracował: ", ileGodz['godz'], "godzin")

    @Rule(AS.zaGodz << PensjaNaGodzine(zl=P(lambda x: x > 0)))
    def przelicz_pensje(self, zaGodz):
        self.setStawka(zaGodz['zl'])
        print("Stawka za godzinę pracownika: ", zaGodz['zl'])
    """
    @Rule(LataPracy(lat=P(lambda x: x >= 10)))
    def premia_za_bd_lata(self):
        self.wyplata *= 1.15
        print("Pracownik ma bardzo duże doświadczenie")

    @Rule(LataPracy(lat=P(lambda x: x >= 5) & P(lambda x: x < 10)))
    def premia_za_sd_lata(self):
        self.wyplata *= 1.05
        print("Pracownik ma duże doświadczenie")

    @Rule(LataPracy(lat=P(lambda x: x >= 1) & P(lambda x: x < 5)))
    def premia_za_s_lata(self):
        self.wyplata *= 1.02
        print("Pracownik ma małe doświadczenie")

    @Rule(LataPracy(lat=P(lambda x: x < 1)))
    def premia_za_k_lata(self):
        print("Pracownik bez doświadczenia")

    @Rule(Stanowisko(stan="Stażysta") & Etat(wymiar="Cały Etat"))
    def podstawaStaz(self):
        wyplata =  Staz.stawka * Caly.godzin
        self.wyplata *= wyplata
        print("Podstawowa Wypłata: ", wyplata)

    @Rule(Stanowisko(stan="Stażysta") & Etat(wymiar="3/4 Etatu"))
    def podstawaStaz1(self):
        wyplata = Staz.stawka * TrzyCwierc.godzin
        self.wyplata *= wyplata
        print("Podstawowa Wypłata: ", wyplata)

    @Rule(Stanowisko(stan="Stażysta") & Etat(wymiar="1/2 Etatu"))
    def podstawaStaz2(self):
        wyplata =  Staz.stawka * Polowa.godzin
        self.wyplata *= wyplata
        print("Podstawowa Wypłata: ", wyplata)

    @Rule(Stanowisko(stan="Stażysta") & Etat(wymiar="1/4 Etatu"))
    def podstawaStaz3(self):
        wyplata =  Staz.stawka * Cwierc.godzin
        self.wyplata *= wyplata
        print("Podstawowa Wypłata: ", wyplata)

    @Rule(Stanowisko(stan="Młodszy Specjalista") & Etat(wymiar="Cały Etat"))
    def podstawaJunior(self):
        wyplata =  Junior.stawka * Caly.godzin
        self.wyplata *= wyplata
        print("Podstawowa Wypłata: ", wyplata)

    @Rule(Stanowisko(stan="Młodszy Specjalista") & Etat(wymiar="3/4 Etatu"))
    def podstawaJunior1(self):
        wyplata =  Junior.stawka * TrzyCwierc.godzin
        self.wyplata *= wyplata
        print("Podstawowa Wypłata: ", wyplata)

    @Rule(Stanowisko(stan="Młodszy Specjalista") & Etat(wymiar="1/2 Etatu"))
    def podstawaJunior2(self):
        wyplata =  Junior.stawka * Polowa.godzin
        self.wyplata *= wyplata
        print("Podstawowa Wypłata: ", wyplata)

    @Rule(Stanowisko(stan="Młodszy Specjalista") & Etat(wymiar="1/4 Etatu"))
    def podstawaJunior3(self):
        wyplata =  Junior.stawka * Cwierc.godzin
        self.wyplata *= wyplata
        print("Podstawowa Wypłata: ", wyplata)


    @Rule(Stanowisko(stan="Specjalista") & Etat(wymiar="Cały Etat"))
    def podstawaMid(self):
        wyplata =  Mid.stawka * Caly.godzin
        self.wyplata *= wyplata
        print("Podstawowa Wypłata: ", wyplata)

    @Rule(Stanowisko(stan="Specjalista") & Etat(wymiar="3/4 Etatu"))
    def podstawaMid1(self):
        wyplata =  Mid.stawka * TrzyCwierc.godzin
        self.wyplata *= wyplata
        print("Podstawowa Wypłata: ", wyplata)

    @Rule(Stanowisko(stan="Specjalista") & Etat(wymiar="1/2 Etatu"))
    def podstawaMid2(self):
        wyplata =  Mid.stawka * Polowa.godzin
        self.wyplata *= wyplata
        print("Podstawowa Wypłata: ", wyplata)

    @Rule(Stanowisko(stan="Specjalista") & Etat(wymiar="1/4 Etatu"))
    def podstawaMid3(self):
        wyplata =  Mid.stawka * Cwierc.godzin
        self.wyplata *= wyplata
        print("Podstawowa Wypłata: ", wyplata)



    @Rule(Stanowisko(stan="Starszy Specjalista") & Etat(wymiar="Cały Etat"))
    def podstawaSenior(self):
        wyplata =  Senior.stawka * Caly.godzin
        self.wyplata *= wyplata
        print("Podstawowa Wypłata: ", wyplata)

    @Rule(Stanowisko(stan="Starszy Specjalista") & Etat(wymiar="3/4 Etatu"))
    def podstawaSenior1(self):
        wyplata =  Senior.stawka * TrzyCwierc.godzin
        self.wyplata *= wyplata
        print("Podstawowa Wypłata: ", wyplata)

    @Rule(Stanowisko(stan="Starszy Specjalista") & Etat(wymiar="1/2 Etatu"))
    def podstawaSenior2(self):
        wyplata =  Senior.stawka * Polowa.godzin
        self.wyplata *= wyplata
        print("Podstawowa Wypłata: ", wyplata)

    @Rule(Stanowisko(stan="Starszy Specjalista") & Etat(wymiar="1/4 Etatu"))
    def podstawaSenior3(self):
        wyplata =  Senior.stawka * Cwierc.godzin
        self.wyplata *= wyplata
        print("Podstawowa Wypłata: ", wyplata)
    ####################################################################

    @Rule(AS.ileGodz << Nadgodziny(godz=P(lambda x: x > 0)) & Stanowisko(stan="Starszy Specjalista"))
    def nadgodzSenior(self, ileGodz):
        dodatek = ileGodz['godz'] * Senior.nadgodzina
        self.dodatek += dodatek
        print("Dodatek za nadgodziny: ", dodatek)

    @Rule(AS.ileGodz << Nadgodziny(godz=P(lambda x: x > 0)) & Stanowisko(stan="Specjalista"))
    def nadgodzMid(self, ileGodz):
        dodatek = ileGodz['godz'] * Mid.nadgodzina
        self.dodatek += dodatek
        print("Dodatek za nadgodziny: ", dodatek)

    @Rule(AS.ileGodz << Nadgodziny(godz=P(lambda x: x > 0)) & Stanowisko(stan="Młodszy Specjalista"))
    def nadgodzJunior(self, ileGodz):
        dodatek = ileGodz['godz'] * Junior.nadgodzina
        self.dodatek += dodatek
        print("Dodatek za nadgodziny: ", dodatek)

    @Rule(AS.ileGodz << Nadgodziny(godz=P(lambda x: x > 0)) & Stanowisko(stan="Stażysta"))
    def nadgodzStaz(self, ileGodz):
        dodatek = ileGodz['godz'] * Staz.nadgodzina
        self.dodatek += dodatek
        print("Dodatek za nadgodziny: ", dodatek)
    ################################################################################
    @Rule(AS.ilePoch << Pochwala(poch=P(lambda x: x > 0)) & Stanowisko(stan="Stażysta"))
    def pochwala(self, ilePoch):
        dodatek = ilePoch['poch'] * Staz.stawka * 3
        self.dodatek += dodatek
        print("Dodatek za pochwały: ", dodatek)

    @Rule(AS.ilePoch << Pochwala(poch=P(lambda x: x < 0)) & Stanowisko(stan="Stażysta"))
    def uwaga(self, ilePoch):
        dodatek = ilePoch['poch'] * Staz.stawka * 3
        self.dodatek += dodatek
        print("Potrącenie za uwagi: ", dodatek)


    @Rule(AS.ilePoch << Pochwala(poch=P(lambda x: x > 0)) & Stanowisko(stan="Młodszy Specjalista"))
    def pochwala1(self, ilePoch):
        dodatek = ilePoch['poch'] * Junior.stawka * 3
        self.dodatek += dodatek
        print("Dodatek za pochwały: ", dodatek)

    @Rule(AS.ilePoch << Pochwala(poch=P(lambda x: x < 0)) & Stanowisko(stan="Młodszy Specjalista"))
    def uwaga1(self, ilePoch):
        dodatek = ilePoch['poch'] * Junior.stawka * 3
        self.dodatek += dodatek
        print("Potrącenie za uwagi: ", dodatek)


    @Rule(AS.ilePoch << Pochwala(poch=P(lambda x: x > 0)) & Stanowisko(stan="Specjalista"))
    def pochwala2(self, ilePoch):
        dodatek = ilePoch['poch'] * Mid.stawka * 3
        self.dodatek += dodatek
        print("Dodatek za pochwały: ", dodatek)

    @Rule(AS.ilePoch << Pochwala(poch=P(lambda x: x < 0)) & Stanowisko(stan="Specjalista"))
    def uwaga2(self, ilePoch):
        dodatek = ilePoch['poch'] * Mid.stawka * 3
        self.dodatek += dodatek
        print("Potrącenie za uwagi: ", dodatek)


    @Rule(AS.ilePoch << Pochwala(poch=P(lambda x: x > 0)) & Stanowisko(stan="Starszy Specjalista"))
    def pochwala3(self, ilePoch):
        dodatek = ilePoch['poch'] * Senior.stawka * 3
        self.dodatek += dodatek
        print("Dodatek za pochwały: ", dodatek)

    @Rule(AS.ilePoch << Pochwala(poch=P(lambda x: x < 0)) & Stanowisko(stan="Starszy Specjalista"))
    def uwaga3(self, ilePoch):
        dodatek = ilePoch['poch'] * Senior.stawka * 3
        self.dodatek += dodatek
        print("Potrącenie za uwagi: ", dodatek)

    @Rule(AS.ileGodz << DelegacjaGodz(godz=P(lambda x : x > 0)) & AS.ileProc << DelegacjaProc(proc=P(lambda x : x > 0)))
    def deleg(self, ileGodz, ileProc):
        dodatek = 100 * (ileGodz['godz']/24) * (ileProc['proc']/100)
        dodatek = round(dodatek, 2)
        self.dodatek += dodatek
        print("Dieta za delegację: ", dodatek)

    @Rule(AS.ileDod << DelegacjaDod(dod=P(lambda x :  x > 0)))
    def dodatek(self, ileDod):
        dodatek = ileDod['dod']
        self.dodatek += dodatek
        print("Dodatek za poniesione koszty: ", dodatek)       

    def ile_wyplaty(self):
        print("Sugerowana wypłata pracownika to: ", self.wyplata + self.dodatek)

"""
engine = WyplataSilnik()
engine.reset()
engine.declare(Pochwala(poch=1), Stanowisko(stan="Stażysta"), Etat(wymiar="Cały Etat"))

engine.run()
engine.ile_wyplaty()
"""