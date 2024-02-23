def fact(n1: int):
    i = 1
    count = 0
    while i <= n1:
        if n1 % i == 0:
            count += 1
        i += 1
    return count


def isPrime(n: int) -> bool:
    if fact(n) != 2:
        return False
    return True


number = 5
if isPrime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
