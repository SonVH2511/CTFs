import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

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

def nghichdao(a, p):
    u, v = a, p
    x1, x2 = 1, 0
    while u != 1:
        q = v // u
        r = v - q * u
        x = x2 - q * x1
        v = u
        u = r
        x2 = x1
        x1 = x
    if x1 >= 0:
        return x1 % p
    else:
        return x1 + p
    
SBD = int(input("SBD = "))
while True:
    p = random.randint(101,499)
    q = random.randint(101,499)
    if checkPrime(p,3) and checkPrime(q,3) and p != q:
        break
print (f"p = {p}")
print (f"q = {q}")

n = p * q
print(f"n = {p} * {q} = {n}")
a = (p - 1) * (q - 1)
print (f"a = {p - 1} * {q - 1} = {a}")

while True:
    e = random.randint(2,a-1)
    if gcd(e,a) == 1:
        break
print(f"e = {e}")
d = nghichdao(e,a)
print(f"d = {e}^(-1) mod {a} = {d}")

m = SBD + 123
print(f"m = {m}")
c = powermod(m,e,n)
print(f"Ban ma c cua thong diep m la: {c}")

m1 = powermod(c,d,n)
print("Thong diep la:", m1)