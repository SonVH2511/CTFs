def gcd(a, b):
    A = a
    B = b
    while (B > 0):
        R = A % B
        A = B
        B = R
    return A


M = int(input("M = "))
N = int(input("N = "))
D = int(input("D = "))
Arr = []
if M <= N:
    if M <= 0 or M >= 1000:
        print("0 < M < 1000")
        M = int(input("Nhap lai M = "))
    if N <= 0 or N >= 1000:
        print("0 < N < 1000")
        N = int(input("Nhap lai N = "))
    if D <= 0 or D >= 1000:
        print("0 < D < 1000")
        D = int(input("Nhap lai D = "))
    if M > N:
        k = M
        M = N
        N = k

    print(">> Cac cap so thoa man la: ")
    for i in range(M+1, N):
        for j in range(M+1, N):
            if [i, j] or [j, i] not in Arr:
                if gcd(i, j) == D:
                    Arr.append([i, j])
                    print("[{},{}]".format(i, j), end=" ")
                    if i != j:
                        Arr.append([j, i])
                        print("[{},{}]".format(j, i), end=" ")
else:
    print("Wrong input")
