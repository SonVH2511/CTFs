# Sàng Số Nguyên Tố

def SNT(n):
    # Khởi tạo danh sách đánh dấu các số từ 2 đến n là True
    primes = [True] * (n+1)

    # Sàng = Loại bỏ các số không phải SNT 
    primes[0] = primes[1] = False
    i = 2
    while (i * i <= n):
        if (primes[i] == True):
            for j in range(i*i, n+1, i):
                primes[j] = False
        i += 1

    # Trả về danh sách các số nguyên tố từ 2 đến n
    return [i for i in range(2,n+1) if primes[i] == True]

# Sàng SoNgTo trên đoạn A -> B

import math

def SNT(A, B):
    primes = [True] * (B - A + 1)
    for i in range(2, int(math.sqrt(B)) + 1):
        for j in range(max(i * i, (A + i - 1) // i * i), B + 1, i):
            primes[j - A] = False
    return [i for i in range(max(2, A), B + 1) if primes[(i-A)] == True]

def SNT(A,B):
    primes = [True] * (B+1)
    primes[0] = primes[1] = False
    for i in range(2, int(math.sqrt(B)) + 1):
        for j in range(max(i * i, (A + i - 1) // i * i), B + 1, i):
            primes[j] = False
    return [i for i in range(max(2, A), B + 1) if primes[(i)] == True]