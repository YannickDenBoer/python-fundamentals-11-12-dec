import random
import string

capitals = string.ascii_uppercase
numbers = string.digits
lowerletters = string.ascii_lowercase
specialCharacters = string.punctuation

charFamilies = [capitals,numbers,lowerletters,specialCharacters]
characters = []

for chars in charFamilies:
    part = random.choices(chars, k=3)
    characters += part

random.shuffle(characters)

password = "".join(characters)

print(password)