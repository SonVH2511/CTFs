import random

# Thuật toán nhân bình phương có lặp
def powermod(a,k,n):
    kq = 1
    a = a % n
    while k > 0:
        if k % 2 ==1:
            kq = (kq * a) % n
        a = (a * a) % n
        k //= 2
    return kq

# Thuật toán Miller Rabin
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

# Thuật toán Fermat
def check_Prime(n,t):
    for i in range(1,t+1):
        a = random.randint(2,n-2)
        r = powermod(a,n-1,n)
        if r != 1:
            return False
    return True

# Thuật toán Random - Search --> Sinh SNT
def check(n,b):
    for i in range(2,b):
            if checkPrime(i,2) and n % i == 0:
                return False
    return True

def sinhSNT(a, b, t):
    while True:
        n = random.randint(a,b)
        if check(n,b):
            continue
        if checkPrime(n,t):
            return n

# Thuật toán tính nghịch đảo
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


# main
n = int(input("Nhap n: "))
t = int(input("Nhap t: "))
print(checkPrime(n,t))