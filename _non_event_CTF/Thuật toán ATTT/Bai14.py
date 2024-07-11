import math

def SNT(A, B):
    primes = [True] * (B - A + 1)
    for i in range(2, int(math.sqrt(B)) + 1):
        for j in range(max(i * i, (A + i - 1) // i * i), B + 1, i):
            primes[j - A] = False
    return [i for i in range(max(2, A), B + 1) if primes[(i-A)] == True]

primes = SNT(100,999)
dem = len(primes)
print(">> Cac so thoa man la:")
for i in range(dem):
    j = int(str(i)[::-1])
    can3 = pow(j,1/3)
    if can3 % 1 == 0:
        print(primes[i], end = " ")