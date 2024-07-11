def nghichdao(a, p):
    u, v = a, p
    x1, x2 = 1, 0
    while u != 1:
        q = v // u
        r = v - q * u
        x = x2 - q * x1
        v = u
        u = r
        x2 = x1
        x1 = x
    if x1 >= 0:
        return x1 % p
    else:
        return x1 + p

p = int(input("p = "))
n = int(input("Nhap so phan tu cua mang n = "))
A = []
print("Nhap vao mang A")
for i in range(1,n+1):
    a = int(input(f"A[{i}] = "))
    while a<0 or a >= p:
        print("a thuoc Fp --> 0 <= a < p")
        a = int(input(f"A[{i}] = "))
    A.append(a)

B = []
print("Mang B chua cac phan tu nghich dao cua mang A")
for i in range(1,n+1):
    k = nghichdao(i,p)
    print(f"B[{i}] = {k}")