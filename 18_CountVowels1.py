# Oplossing met 'nested' for loop
text = input("Write some text: ")
totaalKarakters = len(text)
vowels = "aeiouy"
#vowels = ["a", "e", "i", "o", "u","y"]

totaalKlinkers = 0
# Loop over de klinkers
for vowel in vowels:
    aantalKlinkers = 0
    # Loop over de letters in de tekst
    for letter in text:
        #print("letter:", letter, "vowel:", vowel)
        if letter == vowel:
            aantalKlinkers += 1

    print("Found the vowel ", vowel, " ", aantalKlinkers, " time(s).")
    totaalKlinkers += aantalKlinkers

print("The complete text contains ", totaalKarakters, " character(s).")
print("The text contains ", totaalKlinkers, " vowel(s).")

