import math

def primes(n):
    prime = [True] * (n+1)
    prime[0] = prime[1] = False
    for i in range(2, int(math.sqrt(n))+1):
        if prime[i] == True:
            for j in range(i*i, n+1, i):
                prime[j] = False
    return [i for i in range(2, n+1) if prime[i] == True]

n = int(input("Nhap n: "))
prime = primes(n)
dem = len(prime)
if dem < 4:
    print("Co it hon 4 SNT nho hon hoac bang n ")
for i in range(dem-3):
    Tong = sum(prime[i:i+4])
    if Tong in prime:
        print(">> Day so thoa man la: {} {} {} {}".format(prime[i], prime[i+1], prime[i+2], prime[i+3]))