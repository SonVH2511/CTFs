import random 

# Nhân bình phương có lặp
def powermod(a,k,n):
    kq = 1
    a = a % n
    while k > 0:
        if k % 2 ==1:
            kq = (kq * a) % n
        a = (a * a) % n
        k //= 2
    return kq

# Miller-Rabin
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
while n <= 0 or n > 1000:
    print("Gia tri khong hop le (0 < a,k < n < 1000)")
    n = int(input("n = "))

a = int(input("a = "))
while a <= 0 or a > n:
    print("Gia tri khong hop le (0 < a,k < n < 1000)")
    a = int(input("a = "))

k = int(input("k = "))
while k <= 0 or k > n:
    print("Gia tri khong hop le (0 < a,k < n < 1000)")
    k = int(input("k = "))

y = powermod(a,k,n)
if checkPrime(y,2):
    print(f"{a}^{k} mod {n} = {y} la SNT")
else:
    print(f"{a}^{k} mod {n} = {y} khong phai SNT")