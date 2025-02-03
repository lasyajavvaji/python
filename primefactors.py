def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter number: "))
prime_factors = []

for n in range(1, num + 1):
    if num % n == 0:
        if is_prime(n):
            prime_factors.append(n)

print("Prime factors:", prime_factors)
