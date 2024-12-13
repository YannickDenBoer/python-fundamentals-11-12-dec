def number_of_vowels(word):
    return sum([word.count(v) for v in 'aeiou'])

text = input("Give some text: ")

words = text.split()

lstVowelCount = sorted(words, key=number_of_vowels)

print(lstVowelCount)