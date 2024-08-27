# -*- coding: utf-8 -*-
from random import randrange,sample

def contraseñas(longitud):
    lista = []
    while len(lista) < longitud * 2:
        lista.append(chr(randrange(64,91)))
        lista.append(chr(randrange(97,123)))
        lista.append(chr(randrange(48,58)))
    return "".join(sample(lista,longitud))
    
try:
    log = int(input("Longitud contraseña: "))
    print(contraseñas(log))
except ValueError:
    print("Introcude un numero valido")