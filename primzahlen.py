#
#   Copyright © 2023, SnowCoder404
#
liste = []
for i in range(1, 101):
    y = [h for h in range(1, i+1)]
    data = 0
    for z in y:
        ergebnis = i % z
        if ergebnis == 0:
            data = data + 1
    if data == 2:
        liste.append(i)
print(liste)
