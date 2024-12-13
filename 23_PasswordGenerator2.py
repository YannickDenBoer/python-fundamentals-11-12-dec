import random

capitals = print("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = "0123456789"
lowerletters = capitals.lower()
specialCharacters = "'!@#$%^&*()-+/><:\""

part1 = random.choices(capitals, k=3)
print(part1)
part2 = random.choices(numbers, k=3)
print(part2)
part3 = random.choices(lowerletters, k=3)
print(part3)
part4 = random.choices(specialCharacters, k=3)
print(part4)

characters = part1 + part2 + part3 + part4
#print(characters)

random.shuffle(characters)

password = "".join(characters)

print(password)