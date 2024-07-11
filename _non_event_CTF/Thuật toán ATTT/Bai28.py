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

def Carmichael(n):
    if checkPrime(n,3):
        return False
    for i in range(2,n):
        if gcd(i, n)==1 and powermod(i, n-1, n) != 1:
            return False
    return True

N = int(input("N = "))
if 0 <= N <= 10000:
    print(f">> Cac so Carmichael nho hon {N} la:")
    for i in range(2,N):
        if Carmichael(i):
            print(i, end = " ")
else:
    print("Gia tri khong hop le")