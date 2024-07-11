import math

def demUoc(n):
    dem = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n%i == 0:
            dem += 1
            j = n/i
            if j != i:
                dem += 1
    return dem

#main
n = int(input("Nhap n: "))
T_prime = []
for i in range(1,n+1):
    if demUoc(i) == 3:
        T_prime.append(i)
print("Cac so T-prime nho hon hoac bang {} la: {}".format(n, T_prime))