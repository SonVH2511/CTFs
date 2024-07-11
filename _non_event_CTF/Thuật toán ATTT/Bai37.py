# j là vị trí mà ta đang xét của xâu P
# i là độ dài tiền tố và hậu tố ta đang kiểm tra

def so_sanh_chuoi(P, j, i):     # So sánh i ký tự của tiền tố P[0,j-1] với i ký tự của hậu tố P[1,j-1]
    k = 0
    for x in range(i):
        if P[x] == P[j - i + x]:       
            k += 1
    if k == i:
        return 1       
    return 0

def kiem_tra(P, j):     # Kiểm tra độ dài lớn nhất của tiền tố và hậu tố trùng nhau 
    for i in range(j - 1, -1, -1):      
        if so_sanh_chuoi(P, j, i) == 1:
            return i
    return 0

def failure_function(P):
    F = [-1] * len(P)
    for j in range(1, len(P)):
        F[j] = kiem_tra(P, j)
    return F

T = input("Nhap xau S2: ")
P = input("Nhap xau S1: ")
F = failure_function(P)
i = 0
j = 0
check = 0

while i <= len(T) - len(P):     # Tiến hành kiểm tra nếu i chưa chạy hết độ dài của T-P
    inew = i + j
    if T[inew] == P[j]:
        inew += 1
        j += 1
        if j == len(P):
            print(f"\nXau S1 co xuat hien trong xau S2, bat dau tu vi tri thu {i}")
            check = 1
            break
    else:
        i = i + j - F[j]
        if F[j] == -1:
            j = 0
        else:
            j = F[j]
if check == 0:
    print("\nXau S1 khong xuat hien trong xau S2")

print("\nBang F[j]")
for i in range(len(P)):
    print(f"\n{i} | {F[i]}")