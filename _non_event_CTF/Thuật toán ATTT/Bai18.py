import math

def  Arr(a, W, t):
    A = [0] * t
    for i in range(t-1, -1, -1):
        k = pow(2, W*i)
        A[i] = a // k
        a = a % k
    return A

def Num(A, W, t):
    a = 0
    for i in range(t-1, -1, -1):
        a = a + A[i] * pow(2, W*i)
    return a

def CongSNL(A, B, W, t):
    C = [0] * t
    e = 0
    k = pow(2, W)
    for i in range(t):
        C[i] = A[i] + B[i] + e
        if C[i] >= k:
            e = 1
            C[i] = C[i] % k
        else: 
            e = 0
    return e, C

# main
a = int(input("a = "))
b = int(input("b = "))

p = 2147483647
W = 8
m = math.ceil(math.log(p,2))
t = math.ceil(m/W)

A = Arr(a, W, t)
B = Arr(b, W, t)
e, C = CongSNL(A, B, W, t)

print("(e,C) = ({}, [".format(e), end = "")
for i in range(t-1,-1,-1):
    print(C[i], end = " ")
print("])")

c = Num(C, W, t)
c = c%p
print ("C duoi dang so nguyen trong truong Fp la: ", c)

C = Arr(c, W, t)
print ("c duoi dang mang trong truong Fp la: [", end = "")
for i in range(t-1,-1,-1):
    print(C[i], end =" ")
print("]")