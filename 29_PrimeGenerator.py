def is_prime(n):
    # n = 1 of 0 -> geen priem
    if n <= 1:
        return False
    # n = 2 of 3 -> priem
    elif n <= 3:
        return True
    # is deelbaar door 2 of 3 -> geen priem
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_generator(limit):
    num = 2
    while num <= limit:
        if is_prime(num):
            yield num
        num += 1

# Voorbeeldgebruik:
limiet = 50
print("Priemgetallen tot aan de limiet van", limiet, ":")
primes = prime_generator(limiet)
for prime in primes:
    print(prime, end=" ")