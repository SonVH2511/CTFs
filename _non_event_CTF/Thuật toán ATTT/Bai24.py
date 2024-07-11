import math

def SNT(A,B):
    primes = [True] * (B+1)
    primes[0] = primes[1] = False
    for i in range(2, int(math.sqrt(B)) + 1):
        for j in range(max(i * i, (A + i - 1) // i * i), B + 1, i):
            primes[j] = False
    return [i for i in range(max(2, A), B + 1) if primes[(i)] == True]

A = int(input("A = "))
B = int(input("B = "))
primes = SNT(A,B)
arr = []
dem = 0
for i in range(len(primes)):
    for y in range(primes[i]):
        x = primes[i] - y
        if (math.sqrt(x) % 1 == 0) and (math.sqrt(y) % 1 == 0):
            if  primes[i] not in arr:
                dem += 1
                arr.append(primes[i])
print("So luong SNT thoa man la:", dem)
print("Do la:", arr)