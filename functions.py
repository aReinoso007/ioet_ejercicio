
# Here the file is read line by line
# as well as a bit of cleaning


def readFile(path):
    lines, nl = [], []
    with open(path, encoding='utf8') as f:
        lines = f.readlines()
    for l in lines:
        ln = l.replace("=", ",")
        ln = ln.replace(" ", "")
        ln = ln.strip()
        # here is to split all the values separated by commas
        ln = ln.split(',')[0:]
        nl.append(ln)
    return nl


def dataToDictionary(lst):
    resDict = dict()
    for l in lst:
        resDict[l[0]] = l[1:]
    return resDict


fe = readFile('sample.txt')
dataDict = dataToDictionary(fe)

contador = 0
for i in range(0, len(fe)):
    for j in range(int(i+1), len(fe)):
        arrA = fe[i][1:]
        arrB = fe[j][1:]
        for e in arrA:
            for e2 in arrB:
                if (e[:2] == e2[:2]):
                    x = range(int(e[2:4]), int(e[8:10]))
                    y = range(int(e2[2:4]), int(e2[8:10]))
                    xs = set(x)
                    if xs.intersection(y):
                        contador += 1
        if contador > 0:
            print(fe[i][:1], '-', fe[j][:1], contador)
        contador = 0

""""
ASTRID-RENE: 2
*ASTRID-ANDRES: 3
*RENE-ANDRES: 2
"""""
