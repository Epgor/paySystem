from payEngine import *


engine = WyplataSilnik()
engine.reset()
engine.declare(LataPracy(lat=10), GodzinPracy(godz=120), PensjaNaGodzine(zl=25), Pochwala(poch=1))
engine.run()
