"""
Kerj be ket egesz szamot (feltetelezhetjuk, hogy pozitivak), es ird ki a legnagyobb kozos osztojukat, majd a legkisebb kozos tobbszorosuket.

pl:
Bemenet:
6
27
Kimenet:
3
54
"""
sz1 = int(input())
sz2 = int(input())
nagyobb = max([sz1,sz2])
kisebb = min([sz1,sz2])

# Legnagyobb közös osztó
legnagyKozOszt = kisebb
while True:
    if(kisebb % legnagyKozOszt == 0 and nagyobb % legnagyKozOszt == 0):
        print(legnagyKozOszt)
        break
    legnagyKozOszt -= 1

# Legkisebb közös többszörös
i = 0
while True:
    i += 1
    legkisKozTobb = nagyobb * i
    if (legkisKozTobb % kisebb == 0):
        print(legkisKozTobb)
        break
