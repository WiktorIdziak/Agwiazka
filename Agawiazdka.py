def RobotFpoz(pozX, pozY, step):
    Fpoz = RobotGpoz(step) + RobotHpoz(pozX, pozY)
    return Fpoz

def RobotHpoz(pozX, pozY):
    Hpoz = (((pozX - finishX) ** 2) + (pozY - finishY) ** 2) ** (1 / 2)
    return Hpoz

def RobotGpoz(Gpoz):
    return Gpoz

def Testament(pozX, pozY):
    if pozX == startX and pozY == startY:
        return 1
    else:
        for i in range(0, len(listaZamknieta)):
            if listaZamknieta[i][0] == pozX and listaZamknieta[i][1] == pozY:
                return listaZamknieta[i][4] + 1

def RobotRuch(mapa, pozX, pozY):
    print("Robot znajduje się na pozycji X: ", pozX, "Y: ", pozY)
    print("Robot rozgląda się.")
    RuchUP(mapa, pozX, pozY)
    RuchDOWN(mapa, pozX, pozY)
    RuchLEFT(mapa, pozX, pozY)
    RuchRIGHT(mapa, pozX, pozY)

def RuchUP(mapa, pozX, pozY):
    if pozY + 1 < length:
        if mapa[pozX][pozY + 1] == '5':
            print("przeszkoda X: ", pozX, "Y: ", pozY + 1)
        elif szukaj(listaZamknieta, pozX, pozY + 1):
            print("już tu byłem")
        elif sprawdzOtwarta(listaOtwarta, pozX, pozY + 1):
            listaOtwarta.append([pozX, pozY + 1, pozX, pozY, Testament(pozX, pozY)])

def RuchLEFT(mapa, pozX, pozY):
    if pozX - 1 > 0:
        if mapa[pozX - 1][pozY] == '5':
            print("przeszkoda X: ", pozX - 1, "Y: ", pozY)
        elif szukaj(listaZamknieta, pozX - 1, pozY):
            print("już tu byłem")
        elif sprawdzOtwarta(listaOtwarta, pozX - 1, pozY):
            listaOtwarta.append([pozX - 1, pozY, pozX, pozY, Testament(pozX, pozY)])

def RuchDOWN(mapa, pozX, pozY):
    if mapa[pozX][pozY - 1] == '5':
        print("przeszkoda X: ", pozX, "Y: ", pozY - 1)
    elif szukaj(listaZamknieta, pozX, pozY - 1):
        print("już tu byłem")
    elif pozY - 1 > 0 and sprawdzOtwarta(listaOtwarta, pozX, pozY - 1):
        listaOtwarta.append([pozX, pozY - 1, pozX, pozY, Testament(pozX, pozY)])

def RuchRIGHT(mapa, pozX, pozY):
    if pozX + 1 < length:
        if mapa[pozX + 1][pozY] == '5':
            print("przeszkoda X: ", pozX + 1, "Y: ", pozY)
        elif szukaj(listaZamknieta, pozX + 1, pozY):
            print("już tu byłem")
        elif pozX + 1 < length and sprawdzOtwarta(listaOtwarta, pozX + 1, pozY):
            listaOtwarta.append([pozX + 1, pozY, pozX, pozY, Testament(pozX, pozY)])

def RobotIdz(listaOtwarta):
    punkt = 10000
    helpdesk = 0
    for i in range(0, len(listaOtwarta)):
        if RobotFpoz(listaOtwarta[i][0], listaOtwarta[i][1], listaOtwarta[i][4]) <= punkt:
            punkt = RobotFpoz(listaOtwarta[i][0], listaOtwarta[i][1], listaOtwarta[i][4])
            helpdesk = i
    punkt = listaOtwarta[helpdesk]
    listaOtwarta.remove(punkt)
    print("punkt to: ", punkt, "\n")
    return punkt

def szukaj(listaZamknieta, pozX, pozY):
    for i in range(0, len(listaZamknieta)):
        if listaZamknieta[i][0] == pozX and listaZamknieta[i][1] == pozY:
            return True
    return False

def sprawdzOtwarta(listaOtwarta, pozX, pozY):
    for i in range(0, len(listaOtwarta)):
        if listaOtwarta[i][0] == pozX and listaOtwarta[i][1] == pozY:
            return False
    return True

def makeFinalPath(listaZamknieta, punkt, path, finalPath):
    kroki= punkt[4]
    for x in range(0, kroki):
        for i in range(0, len(listaZamknieta)):
            if punkt[0] == listaZamknieta[i][0] and punkt[1] == listaZamknieta[i][1] and punkt[2] == listaZamknieta[i][2] and punkt[3] == listaZamknieta[i][3] and punkt[4] == listaZamknieta[i][4]:
                path.append(punkt)
        if punkt[2] == 0 and punkt[3] == 0:
            finalPath.append([0, 0])
        else:
            for j in range(0, len(listaZamknieta)):
                if punkt[2] == listaZamknieta[j][0] and punkt[3] == listaZamknieta[j][1]:
                    punkt = listaZamknieta[j]

    for j in range(0, kroki):
        finalPath.append(path.pop())
    print("TRASA:", finalPath)

#####################################################################################################
print("Start")
startX = 0
startY = 0
pozX = startX
pozY = startY
finishX = 19
finishY = 19
step = 0
mapa = []
finalPath = []
path = []
plik = open("grid3.txt", "r")
tekst = plik.read()
plik.close()

tablica = tekst.split("\n")
length = len(tablica)

for i in range(0, length):
    mapa.append(tablica[i].split(" "))
for i in range(0, len(mapa)):
    print(mapa[i])

listaOtwarta = []
listaZamknieta = [[startX, startY]]

while sprawdzOtwarta(listaZamknieta, finishX, finishY):
    RobotRuch(mapa, pozX, pozY)
    if listaOtwarta != []:
        listaZamknieta.append(RobotIdz(listaOtwarta))
    else:
        print("\n Nie można dotrzeć do celu")
        break
    pozX = listaZamknieta[-1][0]
    pozY = listaZamknieta[-1][1]
if listaOtwarta != []:
    makeFinalPath(listaZamknieta, listaZamknieta[-1], path, finalPath)