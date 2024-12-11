lengte = int(input("Geef een lengte: "))

for num in range(1,lengte+1):
    for i in range(num):
        print (num, end=" ") #print number
    print()
    # new line after each row to display pattern correctly