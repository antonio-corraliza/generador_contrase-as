# -*- coding: utf-8 -*-
from random import randrange,sample

def contraseñas(longitud):
    lista = []
    while len(lista) < longitud * 2:
        mayusculas = chr(randrange(64,91))
        lista.append(mayusculas)
        minusculas = chr(randrange(97,123))
        lista.append(minusculas)
        numeros = chr(randrange(48,58))
        lista.append(numeros)
    return "".join(sample(lista,longitud))
log = int(input("longitud contraseña: "))
print(contraseñas(log))