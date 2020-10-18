"""
Kerj be egy egesz szamot (feltetelezheto, hoy pozitiv), es ird, ki, hogy 7-es szamrendszerben felirva mennyi a szamjegyeinek az osszege (decimalis formaban)
 
Pl.: 
 1   (1)  -->  1
 2   (2)  -->  2
 3   (3)  -->  3
 4   (4)  -->  4
 5   (5)  -->  5
 6   (6)  -->  6
 7  (10)  -->  1
 8  (11)  -->  2
 9  (12)  -->  3
10  (13)  -->  4
11  (14)  -->  5
12  (15)  -->  6
13  (16)  -->  7
48  (66)  -->  12
49 (100)  -->  1
"""
a = int(input())
osszeg = 0

# legnagyobb hatványa hétnek ami kell
hatvany = 0
legNagyobbHatvany = 0
while True:
    epp = (7 ** hatvany) * 7
    if epp > a:
        legNagyobbHatvany = hatvany
        break
    hatvany += 1

while legNagyobbHatvany >= 0:
    n = 7
    while ((7 ** legNagyobbHatvany) * n) > a:
        n -= 1
    osszeg += n
    a -= (7 ** legNagyobbHatvany) * n
    legNagyobbHatvany -= 1

print(osszeg)


