# from z3 import *
# import base64
# import numpy as np
# a = "KMACTF{"+('a'*(45-len("KMACTF")))+'}'
# print(a)
# a = 'KMACTF{aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa}'
# print(hex(len(a)*2))
# print(chr(0x000000000000004B))
Checker = [0x72, 0xBB, 0xB2, 0xCD, 0x58, 0xB2, 0x81, 0x0E, 0xA4, 0xB1,
           0xED, 0xDB, 0x84, 0xB2, 0xC0, 0xAA, 0x60, 0xD0, 0xE8, 0xE8,
           0xB0, 0x12, 0x81, 0x1E, 0xED, 0xD0, 0xF3, 0x05, 0xB0, 0xB1,
           0x04, 0x04, 0x7D, 0xF3, 0xC0, 0xE8, 0xED, 0x12, 0xF3, 0xC2,
           0x7D, 0x0E, 0x0E, 0x0E, 0x7D, 0x04, 0xC0, 0xBB, 0xED, 0xB1,
           0x81, 0xED, 0xA4, 0xCF, 0xC0, 0x68, 0x84, 0xD0, 0xE2, 0x1B,
           0xC2, 0x58, 0x30, 0x30]
# print(len(Checker))
vm = [0xC0000094, 0xC0000005, 0xC0000096, 0xC0000005, 0xC0000094, 0xC0000096, 0xC000001D, 0xC0000094, 0xC0000094, 0xC000001D, 0xC0000094, 0xC000001D, 0xC0000096, 0xC0000096, 0xC0000094, 0x80000003, 0xC0000094, 0xC0000096, 0xC0000096, 0xC0000096, 0xC000001D, 0xC0000094, 0xC000001D, 0x80000003, 0xC0000005, 0xC0000096, 0xC0000094, 0xC0000005, 0xC000001D, 0xC000001D, 0x80000003, 0xC0000005,
      0xC000001D, 0xC0000094, 0xC0000094, 0xC0000096, 0xC0000005, 0xC0000094, 0xC0000094, 0xC0000096, 0xC000001D, 0xC0000094, 0xC000001D, 0xC000001D, 0xC000001D, 0x80000003, 0xC0000094, 0xC0000005, 0xC0000005, 0xC000001D, 0xC000001D, 0xC0000094, 0xC0000094, 0xC0000005, 0xC0000094, 0xC000001D, 0xC0000096, 0xC0000096, 0xC0000005, 0x80000003, 0xC0000096, 0xC0000094, 0xC0000096, 0xC0000096]
aAbcdefghijklmn = [0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47, 0x48, 0x49, 0x4A,
                   0x4B, 0x4C, 0x4D, 0x4E, 0x4F, 0x50, 0x51, 0x52, 0x53, 0x54,
                   0x55, 0x56, 0x57, 0x58, 0x59, 0x5A, 0x61, 0x62, 0x63, 0x64,
                   0x65, 0x66, 0x67, 0x68, 0x69, 0x6A, 0x6B, 0x6C, 0x6D, 0x6E,
                   0x6F, 0x70, 0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x78,
                   0x79, 0x7A, 0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37,
                   0x38, 0x39, 0x2B, 0x2F, 0x00]
dword_7FF6E10151D0 = [0, 2, 1, 0]
dword_7FF783225880 = [0]*100
sus = [0x4b, 0x4d, 0x41, 0x43, 0x54, 0x46, 0x7b, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
       0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x7d]

Input = [0x4b, 0x4d, 0x41, 0x43, 0x54, 0x46, 0x7b, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
         0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x7d]

# solver = Solver()
# sus = [BitVec(f'x[{i}]', 8) for i in range(64)]
# sus=[BitVec]
# cnt = 0
# lpBuffer = [1, 5]
# if (lpBuffer == 5):
cnt = 0
p = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
# sus = [0]*1000
pp = 'S01BQ1RGe2'
for r in vm:
    print()
    print(cnt, end=": ")
    for ii in p:
        v1 = ord(ii)
        v0 = ord(ii)
        if r == 0x80000003:
            dword_7FF783225880[cnt] = 0x80000003
            if v1 & 0x80:
                v1 |= 0xFFFFFF00
            for i in range(10):
                v1 = (7 * (i ^ v0) + ((i + 51) ^ (v1 + 69))) & 0xff
            cnt += 1
        if r == 0xC0000005:
            dword_7FF783225880[cnt] = 0xC0000005
            if v1 & 0x80:
                v1 |= 0xFFFFFF00
            for i in range(10):
                v1 = ((v1 + i + 85) ^ 7) & 0xff
            cnt += 1
            # print("0xC0000005", sus)
            # break
        if r == 0xC000001D:
            dword_7FF783225880[cnt] = 0xC000001D
            if v1 & 0x80:
                v1 |= 0xFFFFFF00
            for k in range(10):
                v1 = ((v1 << (k % 3)) & 0x4F ^ (
                    91 * ((k + v0) ^ v1) + k + (v0 >> (((k >> 31) ^ k & 1) - (k >> 31))))) & 0xff
            cnt += 1
        if r == 0xC0000094:
            dword_7FF783225880[cnt] = 0xC0000094
            if v1 & 0x80:
                v1 |= 0xFFFFFF00
            for m in range(10):
                v1 = ((m ^ v0) + 93 * ((m + v0) ^
                                       (3 * v0 + m + v1 + 4 * m))) & 0xff
            # print("0xC0000094: ", sus)
            cnt += 1
        if r == 0xC0000096:
            dword_7FF783225880[cnt] = 0xC0000096
            for n in range(10):
                if v1 & 0x80:
                    v1 |= 0xFFFFFF00
                v1 = (
                    ((77 * ((7 * n) ^ ((v1 + ((v0 << (n % 3))) + 45) & 0xffffffff))) + n + v0) % 255) & 0xff
            cnt += 1
        if (v1 == Checker[cnt-1]):
            print(ii, end=" ")
            pp += ii
        if ii != '=':
            cnt -= 1
# print()
# print(pp)
# print(sus)
# for i in sus:
#     print(hex(i), end=" ")