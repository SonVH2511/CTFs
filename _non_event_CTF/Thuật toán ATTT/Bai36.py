def LastOccurrence(P, x):
    for i in range(len(P) - 1, -1, -1):
        if P[i] == x:
            return i
    return -1


T = input("Nhap xau S2: ")
P = input("Nhap xau S1: ")
m = len(P)
i = m - 1
j = m - 1
check = 0

while i < len(T):
    if T[i] == P[j]:
        if j == 0:
            print(f"\nS1 co xuat hien trong S2, co vi tri bat dau la {i}")
            check = 1
            break
        i -= 1
        j -= 1
    else:
        temp = 1 + LastOccurrence(P, T[i])
        if j > temp:
            min_val = temp
        else:
            min_val = j
        i = i + m - min_val
        j = m - 1

if check == 0:
    print("\nS1 khong xuat hien trong S2")

print("\nBang L(x) - Last Occurrence:")
L = ['*' for _ in range(len(T))]
for x in range(len(T)):
    L[x] = T[x]
    for y in range(x + 1, len(T)):
        if L[x] == T[y]:
            T = T[:y] + '*' + T[y + 1:]     # Đánh dấu ký tự đã xử lý bằng *

for k in range(len(L)):
    if L[k] != '*' and L[k] != ' ':
        # In ra ký tự và vị trí cuối cùng xuất hiện của ký tự trong P
        print(f"\n{L[k]} | {LastOccurrence(P, L[k])}")
