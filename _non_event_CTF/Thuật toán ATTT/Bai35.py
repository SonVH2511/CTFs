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

n = int(input("n = "))
while n < 3:
    print("Gia tri khong hop le --> n >= 3")
    n = int(input("Nhap lai n: "))
t = int(input("t = "))
while t < 1:
    print("Gia tri khong hop le --> t >= 1")
    t = int(input("Nhap lai t: "))

if checkPrime(n,t):
    print(f"n = {n} la SNT")
else:
    print(f"n = {n} la hop so")

p = 1 - (1/4) ** t
print("Xac suat de n la SNT la:", p)
