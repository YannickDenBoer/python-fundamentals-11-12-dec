text = input("Give some text: ")
if text == '':
    text = '''From fairest creatures we desire increase,
That thereby beauty's rose might never die,
But as the riper should by time decease,
His tender heir might bear his memory:
But thou contracted to thine own bright eyes,
Feed'st thy light's flame with self-substantial fuel,
Making a famine where abundance lies,
Thy self thy foe, to thy sweet self too cruel:
Thou that art now the world's fresh ornament,
And only herald to the gaudy spring,
Within thine own bud buriest thy content,
And tender churl mak'st waste in niggarding:
Pity the world, or else this glutton be,
To eat the world's due, by the grave and thee.'''

# Preprocessing
text = text.lower().replace(".", "").replace(",","")
lstText = text.split()
setUniqueWords = set(lstText)

dctUniqueWordCount = {}
#Oplossing zonder .count()
for uniqueWord in setUniqueWords:
    dctUniqueWordCount[uniqueWord] = 0
    for word in lstText:
        if uniqueWord == word:
            dctUniqueWordCount[uniqueWord] += 1

# print occurences
for word, n in dctUniqueWordCount.items():
    print(word, n)