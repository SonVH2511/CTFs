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

n = int(input("Nhap n: "))
A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
for i in range (1,n):
    y = A*i*i + B*i + C
    if (checkPrime(y,5)):
        print("x = {} la so nho nhat thoa man ({}*x^2 + {}*x + {} = {}) la SNT".format(i,A,B,C,y))
        break
else:
    print("Khong co gia tri nao thoa man yeu cau")