import random


def powermod(a, k, n):
    kq = 1
    a = a % n
    while k > 0:
        if k % 2 == 1:
            kq = (kq * a) % n
        a = (a * a) % n
        k //= 2
    return kq


def isPrime(n, t):
    if n <= 1:
        return False
    if (n == 2 or n == 3):
        return True
    if n % 2 == 0:
        return False
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


def findPrime(_MSV):
    for i in range(0, _MSV, 2):
        if (isPrime(_MSV-i, 13)):
            return _MSV-i
        elif (isPrime(_MSV+i, 13)):
            return _MSV+i


MSV = 190547
tmp = MSV
if (MSV % 2 == 0):
    MSV -= 1
k = findPrime(MSV)
print(f">> SNT gan nhat voi {tmp} la: k = {k}")

n = 123456
a = 190547
pow = powermod(a, k, n)
print(f">> {a}^{k} mod {n} = {pow}")
