import random

geheimGetal = random.randint(0,100)

gok = int(input("raad het getal: "))

while True:
    if gok < geheimGetal:
        gok = int(input('hoger, raad nog eens: '))
    elif gok > geheimGetal:
        gok = int(input('lager, raad nog eens: '))
    else:
        print("goed geraden!")
        break