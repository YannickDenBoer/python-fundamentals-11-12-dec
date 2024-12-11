text = input("Put in some text: ")

print("Text in UPPERCASE: ", text.upper())
print("Text in lowercase: ", text.lower())
print("Text capitalized: ", text.capitalize())
print("Text in title: ", text.title())
print("First 3 characters of text: ", text[0:3])

# Check of de tekst eindigt met een vraagteken
# questionmark = text[-1] == '?'
questionmark = text.endswith("?")
if questionmark:
    print("Text ends with a question mark.")
else:
    print("Text does not end with a question mark.")

# print de text in lowercase en vervang spaties met _
text2 = text.lower().replace(" ", "_")
print("Before: ", text, " After: ", text2)