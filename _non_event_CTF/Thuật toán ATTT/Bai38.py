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
a = int(input("a = "))
while (a < 1) or (a > p-1):
    print("Gia tri khong hop le --> 1 <= a <= p-1")
    a = int(input("Nhap lai a: "))

k = nghichdao(a, p)
print(f"Nghich dao cua a = {a} tren truong Fp la: {k}")