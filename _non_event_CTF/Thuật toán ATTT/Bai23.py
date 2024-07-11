import math
import random

def powermod(a,k,n):
    kq = 1
    a = a % n
    while k > 0:
        if k % 2 ==1:
            kq = (kq * a) % n
        a = (a * a) % n
        k //= 2
    return kq

def checkPrime(n,t):
    if n <= 1:
        return False
    if (n == 2 or n == 3):
        return True
    if n%2 == 0:
        return False
    s = 0
    r = n - 1
    while r%2 == 0:
        s += 1
        r //= 2
    for i in range(1,t+1):
        a = random.randint(2,n-2)
        y = powermod(a,r,n)
        if y != 1 and y != n-1 :
            j = 1
            while j <= s-1 and y != n-1 :
                y = powermod(y,2,n)
                if y == 1:
                    return False
                j += 1
            if y != n-1:
                return False    
    return True

def SNT(A,B):
    primes = [True] * (B+1)
    primes[0] = primes[1] = False
    for i in range(2, int(math.sqrt(B)) + 1):
        for j in range(max(i * i, (A + i - 1) // i * i), B + 1, i):
            primes[j] = False
    return [i for i in range(max(2, A), B + 1) if primes[(i)] == True]

A = int(input("A = "))
B = int(input("B = "))
tong = sum(SNT(A,B))
if checkPrime(tong,5):
    print("YES")
else:
    print("NO")