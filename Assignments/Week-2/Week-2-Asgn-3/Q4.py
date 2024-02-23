"""
Q4. Create a function named calSum which takes an 2 integer (n1 and n2) 
    as an argument. Calculate the sum of all the numbers divisible by 5 between n1 and n2 and return that sum. 
    (Make sure that n1 is less than n2).
"""


def calsum(n1: int, n2: int):
    if n1 > n2:
        print("n1 should be less than n2")
    i = n1
    sum: int = 0
    while i <= n2:
        if i % 5 == 0:
            sum += i
        i += 1
    print(sum)


calsum(43, 68)
