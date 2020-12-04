"""
Ebben a perogramban a celunk egy futasok adatait rogzito fajlok statisztikainak kiiratasa.

Az alap adatszerkezetunke gy ilyen dictionary:

{"position":(x,y), "timestamp":ts, "elavation:e}

ahol:
 - x es y meterben megadott koordinatak egy alap viszonyitasi ponthoz kepest
 - ts egy egesz timestamp, ami masodpercben mondja meg, mennyi ido telt el ejfel ota
 - e pedig egy folytonos, meterben mert ertek a tengerszint feletti magassagrol


egy gpx track nem mas, mint ilyen adatpontoknak egy listaja.

A feladatban tobb, esetenkent egymasra epulo fuggvenyt kell megirni, melyek errol a trackrol arulnak el informaciokat.

"""

# Ez a fugggveny adja meg ket position kozotti legvonalbeli tavolsagot meterben. 
# p1 es p2 is (x,y) tuple-ok
def position_distance(p1,p2):
    import math
    return math.sqrt(((p2[0] - p1[0]) ** 2) + ((p2[1] - p1[1]) ** 2))

# Ez a fuggveny egy gpx-et var, ami a fent leirt pontokbol allo lista.
# A fuggveny adja meg a track teljes hosszat, ami a pontok kozotti legvonalbeli tavolsagok osszege.
# Nem kell foglalkozni 3d tavolsaggal, csak a "felulnezeti tavolsaggal".
def total_distance(gpx):
    sum = 0
    for i in range(len(gpx) - 1):
        sum += position_distance(gpx[i]["position"], gpx[i+1]["position"])
    return sum

# Ez adja meg maasodpercben, milyen hosszan futottunk
def total_time(gpx):
    runtime = 0
    for i in range(len(gpx) - 1):
        runtime += (gpx[i+1]["timestamp"] - gpx[i]["timestamp"])
    return runtime

# Ez a fuggveny adja meg masodpercben, hogy a futas soran hany masodpercig alldogaltunk csak futas helyett.
# Alldogalasnak szamit, ha ket meresi pont kozott nem valtozik a pozicio
def idle_time(gpx):
    sum = 0
    for i in range(len(gpx) - 1):
        if (gpx[i]["position"][0] == gpx[i+1]["position"][0]) and (gpx[i]["position"][1] == gpx[i+1]["position"][1]): sum += (gpx[i+1]["timestamp"] - gpx[i]["timestamp"])
    return sum

# Ez a fuggveny adja vissza masodpercben, hogy mennyit mozogtunk
def moving_time(gpx):
    return total_time(gpx) - idle_time(gpx)

# Ez a fuggveny adjon vissza egy stringet, amiben "szepen" benne van egy eltelt ido, amit masodpercben kapunk meg
# Szep alat mm:ss formatumot ertjuk, ha nem volt legalabb egy ora, es hh:mm:ss formatumot, ha igen.
# Mindket esetben a legelso tag (mm vagy hh) eseteben nem szukseges a 2 szeles kiiras 0-val paddingolva, a tobbi pozicion viszont igen.
# Jo peldak: 3:14, 12:23:05, 1:00:01
# Rossz peldak: 03:14, 12:23:5, 1:0:1
def pretty_time(seconds):
    h = seconds // (60 * 60)
    m = (seconds // 60) - (h * 60)
    s = seconds - (h * (60 * 60) + m * 60)

    if s < 10: s = "0" + str(s)

    if seconds < (60 * 60): # nem volt egy ora
        return "{}:{}".format(m, s)
    else: 
        if m < 10: m = "0" + str(m)
        return "{}:{}:{}".format(h, m, s)

# Ez a fuggveny szamolja ki, hogy mennyi volt az osszes emelkedes, azaz hany metert mentunk felfele
def total_ascent(gpx):
    ascent = 0
    for i in range(len(gpx) - 1):
        if gpx[i]["elavation"] < gpx[i+1]["elavation"]: ascent += (gpx[i+1]["elavation"] - gpx[i]["elavation"])
    return ascent

# Ez a fuggveny keresse meg a gpx track elejen azt a legrovidebb reszt, ami mar atlepi a megadott tavolsagot, majd errol a reszrol adjon vissza egy masolatot.
# A fuggveny adjon vissza egy ures tracket, ha az egesz gpx track nincs olyan hosszu, mint a megadott tavolsag.
def chop_after_distance(gpx, distance):
    if total_distance(gpx) < distance:
        return []
    else:
        total = 0
        track = []
        for i in range(len(gpx) - 1):
            total += total_distance(gpx)
            track.append(gpx[i])
            if total >= distance:
                track.append(gpx[i+1])
                return track    

# Ez a fuggveny keresse meg a leggyorsabb, legalabb 1 km-es szakaszt a trackben, es adjon vissza rola egy masolatot
def fastest_1k(gpx):
    min = chop_after_distance(gpx, 1000)
    index = 0

    for i in range(len(gpx)):
        track = chop_after_distance(gpx[i:], 1000)
        trackTime = total_time(track)
        if trackTime < min and 0 > trackTime:
            min = trackTime
            index = i

    return chop_after_distance(gpx[index], 1000)    

# Az alabbi reszek betoltenek egy ilyen pickle fajlt, es kiirjak a statisztikakat megformazva
import pickle

infile=open(input(),"rb")
gpx=pickle.load(infile)
infile.close()

print("Run statistics:")
print(" - Total distance: {:.2f} km".format(total_distance(gpx)/1000))
print(" - Total time    : {}".format(pretty_time(total_time(gpx))))
print(" - Total time    : {}".format(pretty_time(moving_time(gpx))))
print(" - Total ascent  : {:.0f} m".format(total_ascent(gpx)))
print(" - Fastest 1k    : {}".format(pretty_time(total_time(fastest_1k(gpx)))))

