def fibonacci_generator(limit):
    a, b = 1, 2
    while a <= limit:
        yield a
        a, b = b, a + b

# Voorbeeldgebruik:
limiet = 1000
fibonacci = fibonacci_generator(limiet)
print("Fibonacci-getallen tot aan de limiet van", limiet, ":")

for num in fibonacci:
    print(num, end=" ")