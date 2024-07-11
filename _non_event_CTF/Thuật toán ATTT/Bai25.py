def SNT(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    i = 2
    while (i * i <= n):
        if (primes[i] == True):
            for j in range(i*i, n+1, i):
                primes[j] = False
        i += 1
    return [i for i in range(2, n+1) if primes[i] == True]


def findSum(primes, M, N, start, path, result):
    if M == 0 and N == 0:
        result.append(path)
        return
    if M == 0 or N < 0:
        return
    for i in range(start, len(primes)):
        findSum(primes, M - 1, N - primes[i],
                i + 1, path + [primes[i]], result)


M = 3
# M = int(input("M = "))
N = int(input("N = "))
result = []
if M > N:
    print(f"{N} khong the phan tich duoc thanh tong {M} SNT")
else:
    if 2 < M <= 100 and 1 <= N <= 10000:
        primes = SNT(N)
        print(primes)
        findSum(primes, M, N, 0, [], result)
        if not result:
            print(f"{N} khong the phan tich duoc thanh tong {M} SNT")
        else:
            print(f"{N} co the phan tich duoc thanh tong {M} SNT la: ")
            for i in result:
                print(i)
    else:
        print("Gia tri nhap vao khong hop le")
