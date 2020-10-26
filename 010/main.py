total = 0
honap = 12
percek = []
smsek = []
szamla=[]

for i in range(honap):
    telPerc = int(input())
    smsDb = int(input())
    percek.append(telPerc)
    smsek.append(smsDb)

# Csomag árak
havidij = int(input())
percdij = int(input())
smsdij = int(input())

for i in range(honap):
    eppen = 0
    if (percdij * percek[i]) + (smsdij * smsek[i]) > havidij:
        eppen += (percdij * percek[i]) + (smsdij * smsek[i])
    else: eppen += havidij
    szamla.append(eppen)
    total += eppen

print(szamla)
print(total)


