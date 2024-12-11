import random

# Optioneel: gebruik een seed
# random.seed(10)

# Genereer een nummer tussen de 1 en de 6
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
dice3 = random.randint(1, 6)
dice4 = random.randint(1, 6)
dice5 = random.randint(1, 6)

print("Dice 1:", dice1)
print("Dice 2:", dice2)
print("Dice 3:", dice3)
print("Dice 4:", dice4)
print("Dice 5:", dice5)

# Voeg de dobbelstenen aan elkaar toe
sumDices = sum([dice1,dice2,dice3,dice4,dice5])

print("Sum of dices:", sumDices)

