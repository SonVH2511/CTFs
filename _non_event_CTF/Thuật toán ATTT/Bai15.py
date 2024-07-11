def SangSNT(n):
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
primes = SangSNT(n)
check = []
print(">> Cap SNT sinh doi la: ")
for i in range(len(primes)):
    x = primes[i] + 2
    y = primes[i] - 2
    if x in primes:
        if [primes[i],x] and [x,primes[i]] not in check:
            print ("[{},{}]".format(primes[i],x))
            check.append([primes[i],x])
    if y in primes:
        if [primes[i],y] and [y,primes[i]] not in check:
            print ("[{},{}]".format(primes[i],y))
            check.append([primes[i],y])