# from decimal import Decimal as D

def drange(start, stop, step=1.0, endpoint=False):
    floatlist = []
    number = start
    while number < stop:
        floatlist.append(round(number,3))
        number += step
    if endpoint==True and number <= stop:
        floatlist.append(round(number,3))
    return floatlist

print(drange(1,10))

print(drange(1,13))

print(drange(2,13, 2,endpoint=True))

print((drange(2,13, 0.1,endpoint=True)))