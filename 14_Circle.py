import math

radiusString = input("What is the radius of the circle? ")
r = float(radiusString)

# Bereken de oppervlakte
area = math.pi * r**2

# Bereken de omtrek
circumference = 2 * math.pi * r

print("The circle has a radius:", r)
print("The area of the circle is", area)
print("The circumference of the circle is:", circumference)

# Extra checks voor de types
# print("radiusString:", type(radiusString))
# print("r:", type(r))
# print("area:", type(area))
# print("circumference:", type(circumference))
