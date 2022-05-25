from experta import *
from threading import *

class LataPracy(Fact):
    """lata pracy w firmie"""
    pass

class Nadgodziny(Fact):
    pass

class Pochwala(Fact):
    pass

class DoswiadczenieWBranzy(Fact):
    pass

class Stanowisko(Fact):
    pass

class Etat(Fact):
    pass

class DelegacjaGodz(Fact):
    pass

class DelegacjaProc(Fact):
    pass

class DelegacjaDod(Fact):
    pass

class Staz(Fact):
    stawka = 20
    nadgodzina = stawka * 1.5
    delegacja = stawka * 8

class Junior(Fact):
    stawka = 50
    nadgodzina = stawka * 1.5
    delegacja = stawka * 8

class Mid(Fact):
    stawka = 75
    nadgodzina = stawka * 1.5
    delegacja = stawka * 8

class Senior(Fact):
    stawka = 125
    nadgodzina = stawka * 1.5
    delegacja = stawka * 8


class Caly(Fact):
    godzin = 160

class TrzyCwierc(Fact):
    godzin = 120

class Polowa(Fact):
    godzin = 80

class Cwierc(Fact):
    godzin = 40

