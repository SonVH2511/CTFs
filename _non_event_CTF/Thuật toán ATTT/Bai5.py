import math

def SangSoNgTo(A, B):
    primes = [True] * (B - A + 1)
    for i in range(2, int(math.sqrt(B)) + 1):
        for j in range(max(i * i, (A + i - 1) // i * i), B + 1, i):
            primes[j - A] = False
    return [i for i in range(max(2, A), B + 1) if primes[(i-A)] == True]

# main
A = int(input('A ='))
B = int(input('B = '))
sum = sum(SangSoNgTo(A, B))
print("Tong cac so nguyen to trong khoang [A, B] la: ", sum)