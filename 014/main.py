"""
Ideje mozgatni a hosunket :-)

A bemenetek lekezeleset elintezi a foprogram, Nektek csak egy move fuggvenyt kell megirni, ami megprobalja a megadott iranyba mozgatni a hosunket. 

Ez az irany lehet "up", "down", "left", "right".

Hogy ne egy unalmas ures palyan mozogjunk, a foprogram most fixen az alabbi helyzetbol indit: 

████████████████████████████
██🧙░░░░░░░░░░██████████████
██░░░░░░░░‍░░░░██████░░░░░░██
██░░░░██████████████░░██░░██
██░░░░██░░░░░░░░░░██░░██░░██
██░░░░░░░░░░░░██░░██░░██░░██
██████████░░░░██░░██░░██░░██
██░░░░░░░░░░░░██░░░░░░██░░██
████████████████████████████

A szabaly a mozgasra nyilvan a kovetkezo: ha val van, nem tudunk oda menni. A palyarol feltetelezhetjuk, hogy zart, azaz nem lehet rola lemenni, ezt kulon nem kell vizsgalni.

"""

def pretty_map_print(map, character):
    # Ide masold be a multkorit, modositas nem szukseges
    x = character["position"]["x"]
    y = character["position"]["y"]
    width = len(map[1])
    height = len(map)

    if (x <= width - 1 and x >= 0) and (y <= height - 1 and y >= 0): map[y][x] = "🧙‍"

    for i in range(len(map)):
        for j in range(len(map[i])): 
            print(map[i][j], end="")
            if map[i][j] != "🧙": print(map[i][j], end="")
        print("")
    

def move(map,character,direction):
    # fentiek alapjan, direction lehet "up", "down", "left", "right"
    x = character["position"]["x"]
    y = character["position"]["y"]
    map[character["position"]["y"]][character["position"]["x"]] = "░"

    if (direction == "up") and (map[y-1][x] != "█"): character["position"]["y"] -= 1
    elif (direction == "down") and (map[y+1][x] != "█"): character["position"]["y"] += 1
    elif (direction == "left") and (map[y][x-1] != "█"): character["position"]["x"] -= 1
    elif (direction == "right") and (map[y][x+1] != "█"): character["position"]["x"] += 1


###############################################################
###############################################################
####### Ez alatt nem modosithatsz #############################
###############################################################
###############################################################


character={"name":"The wizard", "position":{"x":1,"y":1}}
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
    move(map,character,command)
