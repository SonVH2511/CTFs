def SNT(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    i = 2
    while (i * i <= n):
        if (primes[i] == True):
            for j in range(i*i, n+1, i):
                primes[j] = False
        i += 1
    return [i for i in range(2,n+1) if primes[i] == True]

n = int(input("Nhap n: "))
primes = SNT(n)
dem = len(primes)
print(">> Cap so thoa man la: ")
for i in range(dem):
    for j in range(i+1,dem):
        tong = primes[i] + primes[j]
        hieu = primes[j] - primes[i]
        if tong in primes and hieu in primes:
            print("[{} va {}]".format(primes[i], primes[j]))