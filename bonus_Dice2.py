import random

# Optioneel: gebruik een seed
# random.seed(10)

numberOfDice = 100
sumDices = 0

# Genereer een nummer tussen de 1 en de 6
for diceNo in range(numberOfDice):
    dice = random.randint(1, 6)
    print(f"Dice {diceNo}:", dice)
    # Voeg de dobbelsteen toe aan het totaal
    sumDices = sumDices + dice

print("Sum of dices:", sumDices)