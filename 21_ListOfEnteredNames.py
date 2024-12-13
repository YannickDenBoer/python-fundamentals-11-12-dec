names = []

# Input
while True:
    name = input("Geef een naam: ")
    name = name.strip()
    if name == "":
        break

    names.append(name)

# Output
names.sort() # key=len, reverse=True
#sortedNames = sorted(names) or sorted(names, key=len, reverse=True)

for name in names:
    print(name)