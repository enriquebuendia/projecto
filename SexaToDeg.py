from __future__ import print_function, division
from PyAstronomy import pyasl

def astro(coordenadas):
    ra, dec = pyasl.coordsSexaToDeg(coordenadas)
    print("*****************************************************************")
    print("*Las coordenadas del astro en grados son: %010.6f %+09.6f *" % (ra, dec))
    Pra, Pdec = pyasl.coordsSexaToDeg("02 31 50.59 +89 15 51.4")
    print("*Las coordenadas de Polaris en grados son: %010.6f %+09.6f*" % (Pra, Pdec))
    Dra = ra - Pra
    Ddec = Pdec - dec
    print("*Diferecia en DEG: %010.6f %+09.6f                       *" % (Dra, Ddec))
    return Dra, Ddec

def DegToPasos(coordenadas):
    TamPaso = float(360/200)
    ra, dec = astro(coordenadas)
    pasos1 = round(ra/TamPaso)
    pasos2 = round(dec/TamPaso)
    return pasos1, pasos2
    
