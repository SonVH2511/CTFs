from math import *


def demUoc(n):
    k = 0
    for i in range(1, int(sqrt(n)+1)):
        if (n % i == 0):
            k += 1
            j = n/i
            if (j != i):
                k += 1
        if k > 4:
            return -1
    return k


# main
n = int(input(">> Nhap n: "))
print("Cac so Q-Prime nho hon hoac bang n: ")
for i in range(1, n+1):
    if (demUoc(i) == 4):
        print(i)
