import random


def lottoziehung():

    zahlen = []
    for zahl in range(1, 46):
        zahlen.append(zahl)

    gezogen = []      
    letzter = 44     

    for durchgang in range(6):

        i = random.randint(0, letzter)


        gezogene_zahl = zahlen[i]
        gezogen.append(gezogene_zahl)



        zahlen[i] = zahlen[letzter]
        zahlen[letzter] = gezogene_zahl


        letzter = letzter - 1

    return gezogen


def statistik(gezogen, stat):
    for zahl in gezogen:
        stat[zahl] = stat[zahl] + 1



stat = {}
for zahl in range(1, 46):
    stat[zahl] = 0

anzahl = int(input("Wie viele Ziehungen? "))

for durchgang in range(anzahl):
    gezogen = lottoziehung()
    statistik(gezogen, stat)



for zahl in range(1, 46):
    print(zahl, ":", stat[zahl], "mal")