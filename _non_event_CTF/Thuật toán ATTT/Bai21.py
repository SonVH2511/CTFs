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

def SNT(n):
    primes = [True] * (n)
    primes[0] = primes[1] = False
    i = 2
    while (i * i < n):
        if (primes[i] == True):
            for j in range(i*i, n, i):
                primes[j] = False
        i += 1
    return [i for i in range(2,n) if primes[i] == True]


A = int(input("A = "))
B = int(input("B = "))
supperprime = []
dem = 0
for i in range(A,B+1):
    k = len(SNT(i))
    if checkPrime(k,5):
        dem += 1
        supperprime.append(i)
print("So sieu SNT trong khong [A,B] la: ", dem)
print("Cac so do la: ",supperprime)