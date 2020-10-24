bekertMozgas = []
def Penzmozgas():
    for i in range(12): bekertMozgas.append(int(input()))

def Bankszamla(mozgas):
    egyenleg = 0
    for i in range(len(mozgas)):
        if i != 0: egyenleg -= 2000 # januar kivetel
        egyenleg += mozgas[i]
        if egyenleg < 0: egyenleg = int(egyenleg * 1.1) # negativ
        elif egyenleg > 0: egyenleg = int(egyenleg * 1.05) # pozitiv
    return egyenleg

def SzamlaNelkul(mozgas):
    egyenleg = 0
    for i in mozgas: egyenleg += i
    return egyenleg

Penzmozgas()
print(Bankszamla(bekertMozgas[:]))
print(SzamlaNelkul(bekertMozgas[:]))
