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

n = int(input("Nhap so phan tu cua mang n = "))
A = []
print("Nhap vao mang A")
for i in range(1,n+1):
    A.append(int(input(f"A[{i}] = ")))

dem = 0
B = []
for i in range(n):
    for j in range(i+1,n):
        if checkPrime(gcd(A[i],A[j]),2):
            dem += 1
            B.append([i,j])

if dem != 0:
    print("So cap so (i,j) thuoc A co UCLN la SNT la:",dem)
    print("Do la:", B)
else: 
    print("Khong co cap (i,j) thuoc A co UCLN la SNT")