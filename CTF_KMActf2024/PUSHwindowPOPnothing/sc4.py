from z3 import *

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
sus = [0x4b, 0x4d, 0x41, 0x43, 0x54, 0x46, 0x7b, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61,
       0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x7d]
Input = [0x4b, 0x4d, 0x41, 0x43, 0x54, 0x46, 0x7b, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61,
         0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x7d]
solver = Solver()
sus = [BitVec(f'x[{i}]', 8) for i in range(64)]
# sus=[BitVec]
cnt = 0
# lpBuffer = [1, 5]
# if (lpBuffer == 5):

v6 = 0
v8 = 0
v14 = 0
v10 = 0
v11 = [0]*100
v11 = [BitVec(f'y[{i}]', 8) for i in range(64)]
curr_len = len(sus)
while (v6 < curr_len):
    v12 = sus[v6]
    v6 += 1
    if (v6 >= curr_len):
        v13 = 0
    else:
        v13 = sus[v6]
        v6 += 1
    if (v6 >= curr_len):
        v14 = 0
    else:
        v14 = sus[v6]
        v6 += 1
    v10 = (v12 << 16) + v14 + (v13 << 8)
    v11[v8] = aAbcdefghijklmn[(v10 >> 18) & 63]
    v9 = v8 + 1
    v11[v9] = aAbcdefghijklmn[(v10 >> 12) & 63]
    v9 += 1
    v11[v9] = aAbcdefghijklmn[(v10 >> 6) & 63]
    v9 += 1
    v11[v9] = aAbcdefghijklmn[v14 & 63]
    v8 = v9 + 1
i = 0
while (i < dword_7FF6E10151D0[curr_len % 3]):
    v11[4 * ((curr_len + 2) // 3) - 1 - i] = 61
    i += 1
print("b64: ", end='')
for i in v11:
    print(chr(i), end='')
print()
sus = v11
# v3 = lpBuffer[1]
# v0 = sus[cnt]


for r in vm:
    v0 = sus[cnt]
    if r == 0x80000003:
        dword_7FF783225880[cnt] = 0x80000003
        if sus[cnt] & 0x80:
            sus[cnt] |= 0xFFFFFF00
        for i in range(10):
            sus[cnt] = (7 * (i ^ v0) + ((i + 51) ^ (sus[cnt] + 69))) & 0xff
        solver.add(sus[cnt] == Checker[cnt])
        cnt += 1
    if r == 0xC0000005:
        dword_7FF783225880[cnt] = 0xC0000005
        if sus[cnt] & 0x80:
            sus[cnt] |= 0xFFFFFF00
        for i in range(10):
            sus[cnt] = ((sus[cnt] + i + 85) ^ 7) & 0xff
        solver.add(sus[cnt] == Checker[cnt])
        cnt += 1
        # print("0xC0000005", sus)
        # break
    if r == 0xC000001D:
        dword_7FF783225880[cnt] = 0xC000001D
        if sus[cnt] & 0x80:
            sus[cnt] |= 0xFFFFFF00
        for k in range(10):
            sus[cnt] = ((sus[cnt] << (k % 3)) & 0x4F ^ (
                91 * ((k + v0) ^ sus[cnt]) + k + (v0 >> (((k >> 31) ^ k & 1) - (k >> 31))))) & 0xff
        solver.add(sus[cnt] == Checker[cnt])
        cnt += 1
    if r == 0xC0000094:
        dword_7FF783225880[cnt] = 0xC0000094
        if sus[cnt] & 0x80:
            sus[cnt] |= 0xFFFFFF00
        for m in range(10):
            sus[cnt] = ((m ^ v0) + 93 * ((m + v0) ^
                        (3 * v0 + m + sus[cnt] + 4 * m))) & 0xff
        # print("0xC0000094: ", sus)
        solver.add(sus[cnt] == Checker[cnt])
        cnt += 1
    if r == 0xC0000096:
        dword_7FF783225880[cnt] = 0xC0000096
        for n in range(10):
            if sus[cnt] & 0x80:
                sus[cnt] |= 0xFFFFFF00
            # print(hex(
            #     (77 * ((7 * n) ^ ((sus[cnt] + ((v0 << (n % 3))) + 45) & 0xffffffff)))), end=" ")
            # print(hex(
            #     ((77 * ((7 * n) ^ ((sus[cnt] + ((v0 << (n % 3))) + 45) & 0xffffffff))) + n + v0)), end=" ")
            sus[cnt] = (
                ((77 * ((7 * n) ^ ((sus[cnt] + ((v0 << (n % 3))) + 45) & 0xffffffff))) + n + v0) % 255) & 0xff
            # print(hex(sus[cnt]))
        solver.add(sus[cnt] == Checker[cnt])
        cnt += 1

        # print("0xC0000096: ", sus, hex(v0))
        # break
    # print(cnt)
# break
# if (lpBuffer == 1):


# v6 = 0
# v8 = 0
# v14 = 0
# v10 = 0
# v11 = [0]*100
# curr_len = len(sus)
# while (v6 < curr_len):
#     v12 = sus[v6]
#     v6 += 1
#     if (v6 >= curr_len):
#         v13 = 0
#     else:
#         v13 = sus[v6]
#         v6 += 1
#     if (v6 >= curr_len):
#         v14 = 0
#     else:
#         v14 = sus[v6]
#         v6 += 1
#     v10 = (v12 << 16) + v14 + (v13 << 8)
#     v11[v8] = aAbcdefghijklmn[(v10 >> 18) & 0x3F]
#     v9 = v8 + 1
#     v11[v9] = aAbcdefghijklmn[(v10 >> 12) & 0x3F]
#     v9 += 1
#     v11[v9] = aAbcdefghijklmn[(v10 >> 6) & 0x3F]
#     v9 += 1
#     v11[v9] = aAbcdefghijklmn[v14 & 0x3F]
#     v8 = v9 + 1
# i = 0
# while (i < dword_7FF6E10151D0[curr_len % 3]):
#     v11[4 * ((curr_len + 2) // 3) - 1 - i] = 61
#     i += 1

if solver.check() == sat:
    print(solver.model())
else:
    print('Fail')
# print(sus)
# for i in sus:
#     print(chr(i), end='')
