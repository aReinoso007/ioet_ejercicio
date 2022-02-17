
# Here the file is read line by line
# as well as a bit of cleaning
import re
from datetime import datetime


def readFile(path):
    lines, nl = [], []
    with open(path, encoding='utf8') as f:
        lines = f.readlines()
    for l in lines:
        ln = l.replace("=", ",")
        # .strip to get rid of newline characters
        ln = ln.strip()
        # here is to split all the values separated by commas
        ln = ln.split(',')[0:]
        nl.append(ln)
    return nl


def dataToDictionary(lst):
    resDict = dict()
    for l in lst:
        # the first value is used as the key, and everything after is passed
        # as a list of values
        resDict[l[0]] = l[1:]
    return resDict


fe = readFile('sample.txt')
dataDict = dataToDictionary(fe)
iterador = iter(dataDict)


for i in range(0, len(fe)):
    contador = 0
    for j in range(i+1, len(fe)):
        arrA = fe[i][1:]
        arrB = fe[j][1:]
        for e in arrA:
            # obtener el intervalo de horas
            print(e[2:])
            # obtener el dia
            print(e[:2])
            for e2 in arrB:
                if e[:2] == e2[:2]:
                    print('same day')
    print(fe[i][:2], '-', fe[j][:1], contador)
    contador = 0
""""
RENE-ASTRID: 3
"""""

"""""
ideas verificar que los rangos de
entrada y salida o sean los mismos(en cuanto a horas)
o que uno se encuentre dentro del rango del otro
"""""
