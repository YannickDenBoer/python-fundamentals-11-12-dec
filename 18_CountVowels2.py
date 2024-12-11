text = input("Write some text: ")
totaalKarakters = len(text)
vowels = "aeiouy"

totaalKlinkers = 0
for vowel in vowels:
    aantalKlinkers = text.count(vowel)

    print("Found the vowel ", vowel, " ", aantalKlinkers, " time(s).")
    totaalKlinkers = totaalKlinkers + aantalKlinkers

print("The complete text contains ", totaalKarakters, " character(s).")
print("The text contains ", totaalKlinkers, " vowel(s).")