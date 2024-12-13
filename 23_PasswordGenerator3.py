import random

capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
lowerletters = capitals.lower()
specialCharacters = "'!@#$%^&*()-+/><:\""
charFamilies = [capitals,numbers,lowerletters,specialCharacters]
characters = []

for chars in charFamilies:
    part = random.choices(chars, k=3)
    characters += part

random.shuffle(characters)

password = "".join(characters)

print(password)