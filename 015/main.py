"""
A hosunk nem lat el a vegtelensegig. X-Ray vision megvan, mint Supermannek, amiatt nem kell aggodni, de van mostantol egy "vision" tulajdonsaga, ami megmondja, hogy mekkora "korben" (negyzet valojaban) lat. Ha mondjuk a vision 3, akkor egy 7x7-es negyzetet lat, mert 3-nyit lat el balra jobbra, fel le. Tehat mondjuk a korabbi peldanal maradva a kezdoallapot:

██████████
██🧙░░░░░░
██░░░░░░░░
██░░░░████
██░░░░██░░

Balra itt nem lat el 3-at, meg felfele, mert nincs annyi a palyabol ugye. Egy jobbra lepes utan:
████████████
██░░🧙░░░░░░
██░░░░░░░░░░
██░░░░██████
██░░░░██░░░░
majd lefele:
████████████
██░░░░░░░░░░
██░░🧙░░░░░░
██░░░░██████
██░░░░██░░░░
██░░░░░░░░░░
meg 3x le, aztan jobbra:
██░░░░░░░░░░░░
██░░░░████████
██░░░░██░░░░░░
██░░░░🧙░░░░░░
██████████░░░░
██░░░░░░░░░░░░
██████████████
Es akkor itt most mar "teljesen kihasznalja" a latasat. 


A bemenetek lekezeleset elintezi a foprogram, eloszor beker egy ilyen "vision" erteket, majd utana a mozgasokat ugy, ahogy mult heten.

Terkepnek a korabbit hasznalja, es ugyanugy a bal felso ficakbol indulunk.

"""

def pretty_map_print(map, character):
    # A multkorit kell kicsit megpofozni
    x = character["position"]["x"]
    y = character["position"]["y"]
    width = len(map[1])
    height = len(map)
    v = character["vision"]

    if (x <= width - 1 and x >= 0) and (y <= height - 1 and y >= 0): map[y][x] = "🧙"

    for i in range(len(map)):
        if (y-i) <= v and (i-y) <= v:
            for j in range(len(map[i])): 
                if (x-j) <= v and (j-x) <= v: print(map[i][j], end="")
                if (map[i][j] != "🧙") :
                    if ((x-j) <= v and (j-x) <= v): print(map[i][j], end="")
            print("")

              

def move(map,character,direction):
    # ide csak masold be a multkorit, nem kell pofozni
    x = character["position"]["x"]
    y = character["position"]["y"]
    map[character["position"]["y"]][character["position"]["x"]] = "░"

    if (direction == "up") and (map[y-1][x] != "█"): 
        character["position"]["y"] -= 1
        return True
    elif (direction == "down") and (map[y+1][x] != "█"):
        character["position"]["y"] += 1
        return True
    elif (direction == "left") and (map[y][x-1] != "█"):
        character["position"]["x"] -= 1
        return True
    elif (direction == "right") and (map[y][x+1] != "█"):
        character["position"]["x"] += 1
        return True
    else:
        return False


###############################################################
###############################################################
####### Ez alatt nem modosithatsz #############################
###############################################################
###############################################################


vision=int(input())
character={"name":"The wizard", "position":{"x":1,"y":1},"vision":vision}
map = [
    ["█","█","█","█","█","█","█","█","█","█","█","█","█","█"],
    ["█","░","░","░","░","░","░","█","█","█","█","█","█","█"],
    ["█","░","░","░","░","░","░","█","█","█","░","░","░","█"],
    ["█","░","░","█","█","█","█","█","█","█","░","█","░","█"],
    ["█","░","░","█","░","░","░","░","░","█","░","█","░","█"],
    ["█","░","░","░","░","░","░","█","░","█","░","█","░","█"],
    ["█","█","█","█","█","░","░","█","░","█","░","█","░","█"],
    ["█","░","░","░","░","░","░","█","░","░","░","█","░","█"],
    ["█","█","█","█","█","█","█","█","█","█","█","█","█","█"]
]


while True:
    pretty_map_print(map,character)
    command = input()
    if command=="end": break
    print ("Moving "+command+" is "+ 
        ("successful" if move(map,character,command) else "impossibru")
    )
