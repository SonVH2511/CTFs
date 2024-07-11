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

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
m = int(input("m = "))
l = int(input("l = "))
Arr = []
if m > l:
    k = m
    m = l
    l = k
for i in range (m,l+1):
    y = A*i*i + B*i + C
    if checkPrime(y,5):
        Arr.append(y)
if not Arr:
    print("Khong co gia tri thoa man y = {}*i*i + {}*i + {} la SNT".format(A,B,C))
else:
    print("Cac gia tri thoa man y = {}*i*i + {}*i + {} la SNT la: {}".format(A,B,C,Arr))