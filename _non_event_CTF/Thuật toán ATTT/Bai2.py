# Sử dụng Miller Ranbin để check SNT

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

# main
n = int(input(">> Nhap n: "))
while (n<2 or n > 10):
    print("n thuoc [2;10]")
    n = int(input(">> Nhap lai n: "))
t = int(input(">> Nhap t: "))
print("Cac so nguyen to co n chu so la: ")
a = 10**(n-1)
b = 10**n
for i in range(a, b):
    if (checkPrime(i,t)):
        print(i)