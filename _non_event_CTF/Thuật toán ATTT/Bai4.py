import math

def SangSoNgTo(A,B):
    primes = [True] * (B+1)
    primes[0] = primes[1] = False
    for i in range(2, int(math.sqrt(B)) + 1):
        for j in range(max(i * i, (A + i - 1) // i * i), B + 1, i):
            primes[j] = False
    return [i for i in range(max(2, A), B + 1) if primes[(i)] == True]

# main
A = int(input("A = "))
B = int(input("B = "))
dem = len(SangSoNgTo(A,B))
print("So so nguyen to trong khoang [A, B] la: ", dem)