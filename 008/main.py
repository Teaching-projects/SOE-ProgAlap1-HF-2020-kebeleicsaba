x=0.0
y=0.0

def KetPontTav(x1, y1):
    print(round(((0 - x1) ** 2 + (0 - y1) ** 2) ** 0.5, 2))

while True:
    irany = str(input())
    if irany == "stop": break
    egyseg = float(input())
    if irany == "forward": y += egyseg
    elif irany == "backward": y -= egyseg
    elif irany == "right": x += egyseg
    elif irany == "left": x -= egyseg

print(round(x,2))
print(round(y,2))
KetPontTav(x, y)
    