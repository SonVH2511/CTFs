# Chia đa thức
def div_gf2(a, b):
    q = []
    r = list(a)
    
    len_b = len(b)
    len_r = len(r)
    
    while len_r >= len_b:
        lead = r[0]
        q.append(lead)
        
        if lead == 1:
            for i in range(len_b):
                r[i] ^= b[i]
        
        r.pop(0)
        len_r -= 1
    
    while len(q) > 1 and q[0] == 0:
        q.pop(0)
    while len(r) > 1 and r[0] == 0:
        r.pop(0)
    
    return q, r

# Nhân đa thức
def mul_gf2(a, b):
    len_a = len(a)
    len_b = len(b)
    
    res = [0] * (len_a + len_b - 1)
    
    for i in range(len_a):
        for j in range(len_b):
            res[i + j] ^= a[i] & b[j]
    
    return res

# XOR
def sub_gf2(a, b):
    len_a = len(a)
    len_b = len(b)
    
    if len_a > len_b:
        b = [0] * (len_a - len_b) + b
    elif len_b > len_a:
        a = [0] * (len_b - len_a) + a
    
    return [x ^ y for x, y in zip(a, b)]

# Sử dụng Euclid mở động tìm GCD(a,b)
def gcd_gf2(a, b):
    if all(c == 0 for c in b):
        return a, [1], [0]
    else:
        x1, y1, x2, y2 = [0], [1], [1], [0]
        while not all(c == 0 for c in b):
            q, r = div_gf2(a, b)
            x = sub_gf2(x2, mul_gf2(q, x1))
            y = sub_gf2(y2, mul_gf2(q, y1))
            a, b = b, r
            x2, x1 = x1, x
            y2, y1 = y1, y
        return a, x2, y2

# Tìm nghịch đảo
def inv_gf2(a, b):
    d, x, _ = gcd_gf2(a, b)
    if d != [1]:
        return -1
    else:
        _, inv = div_gf2(x, b)
        return inv

n = int(input("Nhap so phan tu cua mang n = "))     # n = số mũ cao nhất của đa thức + 1
A = []
print("Nhap vao mang A")
for i in range(1,n+1):
    a = int(input(f"A[{i}] = "))
    while a!=0 and a!=1:
        print("Chỉ nhập giá trị 0 hoặc 1")
        a = int(input(f"A[{i}] = "))
    A.append(a)
g = [1,0,0,0,1,1,0,1,1]              # Đa thức bất khả quy 

print("\nĐa thức 1:", A)
print("Đa thức 2:", g)

inverse = inv_gf2(A, g)
print("\nNghịch đảo:", inverse)

# Kiểm tra kết quả nghịch đảo
test = mul_gf2(inverse, A)
quot, rem = div_gf2(test, g)
print("Kết quả phép chia:", (quot, rem))