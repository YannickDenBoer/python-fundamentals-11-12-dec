age = int(input("What is their age? "))

if age >= 0 and age < 2:
    print("It is a baby.")
elif age >= 2 and age < 4:
    print("It is a toddler.")
elif age >= 4 and age < 13:
    print("It is a kid.")
elif age >= 13 and age < 20:
    print("It is a teenager.")
elif age >= 20 and age < 65:
    print("It is an adult.")
elif age >= 65:
    print("It is an elder.")
else:
    print("It is something else.")
