# Sử dụng Sàng nguyên tố để check

from math import *

def Sang(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    i = 2
    while (i*i <= n):
        if (primes[i] == True):
            for j in range(i*i, n+1, i):
                primes[j] = False
        i += 1
    return [i for i in range(2,n+1) if primes[i] == True]

# main
n = int(input(">> Nhap n: "))
while (n<2 or n > 10):
    print("n thuoc [2;10]")
    n = int(input(">> Nhap lai n: "))
print("Cac so nguyen to co n chu so la: ")
for i in range(int(pow(10,(n-1))),int(pow(10,n))):
    if i in Sang(int(10**n)):
        print(i)