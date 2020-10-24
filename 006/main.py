"""
Kerj be egesz szamokat addig, amig 0-t nem kapsz.
A vegen irj ki minden bekert szamot, de mindgyiket csak egyszer, es abban a sorrendben, ahogy az elso elofordulas tortent.

pl:

Bemenet:
1
2
3
4
3
2
4
7
5
6
7
0
Kimenet:
1
2
3
4
7
5
6
"""
def Halmaz(lista):
    kimenet = []
    for i in range(len(lista)):
        j = 0
        van = False
        while j < len(kimenet):
            if kimenet[j] == lista[i]: van = True
            j += 1
        if van == False: kimenet.append(lista[i])
    return kimenet

szamok = []
while True:
    bekert = int(input())
    if bekert == 0:
        break
    szamok.append(bekert)
    
for i in Halmaz(szamok[:]): print(i)
