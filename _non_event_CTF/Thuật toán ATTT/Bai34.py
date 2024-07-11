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

# Thuật toán Fermat
def checkPrime(n,t):
    for i in range(1,t+1):
        a = random.randint(2,n-2)
        r = powermod(a,n-1,n)
        if r != 1:
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