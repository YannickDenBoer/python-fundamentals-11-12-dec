year = int(input("Put in a year: "))

# a year is a leapyear if the year can be divided by 4
# but (and) the year can not be divided by 100
# except (or) if the year can be divided by 400
leapyear = bool(((year % 4) == 0 and (year % 100) != 0) or (year % 400) == 0)

# Alternatieve oplossing
# div4 = year % 4 == 0
# div100 = year % 100 == 0
# div400 = year % 400 == 0
# leapyear = ((div4 and not div100) or div400)

print(leapyear)

# Optioneel: probeer de if-else statement
if leapyear:
    print(year, "is a leapyear")
else:
    print(year, "is not a leapyear")
