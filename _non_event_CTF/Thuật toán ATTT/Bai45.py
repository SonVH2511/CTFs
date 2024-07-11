import random
import math


def powermod(a, k, n):
    kq = 1
    a = a % n
    while k > 0:
        if k % 2 == 1:
            kq = (kq * a) % n
        a = (a * a) % n
        k //= 2
    return kq


def isPrime(n, t):  # Miller Rabin
    if n <= 1:
        return False
    if (n == 2 or n == 3):
        return True
    if n % 2 == 0:
        return False

    # Phân tích n-1 thành 2^s * r
    s = 0
    r = n - 1
    while r % 2 == 0:
        s += 1
        r //= 2

    for i in range(1, t+1):
        a = random.randint(2, n-2)
        y = powermod(a, r, n)
        if y != 1 and y != n-1:
            j = 1
            while j <= s-1 and y != n-1:
                y = powermod(y, 2, n)
                if y == 1:
                    return False
                j += 1
            if y != n-1:
                return False
    return True


def sinhSNT(n, a, b):
    while True:
        n = random.randint(a, b)
        if n % 2 == 0:
            continue
        if isPrime(n, 13):
            return n


n = int(input("n = "))
A = []
for i in range(1, n+1):
    A.append(sinhSNT(n, 1, 1000))
print("In mang A:", A)

_min = abs(A[0]-A[1])
for i in range(n):
    for j in range(i+1, n):
        k = abs(A[i]-A[j])
        if k < _min:
            _min = k
print("Khoang cach nho nhat giua 2 so bat ky trong A la:", _min)
