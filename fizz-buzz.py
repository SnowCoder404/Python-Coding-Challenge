#
#   Copyright © 2023, SnowCoder404
#
zahl = 0
for i in range(100):
    zahl = zahl + 1
    fizz = zahl / 3
    buzz = zahl / 5
    if fizz.is_integer():
        print('Fizz')
    elif buzz.is_integer():
        print('Buzz')
    else:
        print(zahl)
