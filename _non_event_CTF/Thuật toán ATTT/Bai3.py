import random
import math

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

# main
N = int(input(">>Nhap so nguyen duong N: "))
t = int(input(">>Nhap tham so an toan t: "))
s,p,k,q = 0,0,0,0
for i in range(1,int(math.sqrt(N))+1):
    if N%i == 0:
        s += 1
        p += i
        if checkPrime(i,t):
            k += 1
            q += i
        j = N/i
        if (j != i):
            s += 1
            p += j
            if checkPrime(j,t):
                k += 1
                q += j
Tong =  N + p + s - q - k
print(" N + p + s - q - k = ", Tong)