inter = [0x14, 0x5D, 0x14, 0x57, 0x16, 0x43, 0x46, 0x7A, 0x56, 0x16, 0x57, 0x17, 0x4B, 0x16, 0x52, 0x4C, 0x61, 0x1C, 0x1C, 0x7A, 0x1D, 0x7A, 0x11, 0x51, 0x52,
         0x16, 0x5E, 0x62, 0x6D, 0x5E, 0x61, 0x7A, 0x16, 0x17, 0x61, 0x16, 0x6B, 0x61, 0x4E, 0x69, 0x14, 0x6B, 0x6D, 0x51, 0x57, 0x6D, 0x6D, 0x58, 0x5D, 0x4B]
flag = ""

shuffledPos = [i for i in range(0, 50)]

for i in range(len(inter)):
    tmp = shuffledPos[i]
    shuffledPos[i] = shuffledPos[((i + 7) * 15) % 50]
    shuffledPos[((i + 7) * 15) % 50] = tmp

for i in range(len(inter)):
    inter[i] = inter[i] ^ 0x5 ^ 0x20

for i in range(len(inter)):
    tmp = shuffledPos[i]
    shuffledPos[i] = shuffledPos[((i + 3) * 7) % 50]
    shuffledPos[((i + 3) * 7) % 50] = tmp

for i in range(len(inter)):
    tmp = shuffledPos[i]
    shuffledPos[i] = shuffledPos[((i + 83) * 12) % 50]
    shuffledPos[((i + 83) * 12) % 50] = tmp

# print(shuffledPos)

for j in range(50):
    for i in range(len(shuffledPos)):
        if shuffledPos[i] == j:
            flag += chr(inter[i])

print(flag)
# wctf{sHr3DDinG_L1k3_H3NDr1x_93284}


# inter = [0x14, 0x5D, 0x14, 0x57, 0x16, 0x43, 0x46, 0x7A, 0x56, 0x16, 0x57, 0x17, 0x4B, 0x16, 0x52, 0x4C, 0x61, 0x1C, 0x1C, 0x7A, 0x1D, 0x7A, 0x11, 0x51, 0x52,
#          0x16, 0x5E, 0x62, 0x6D, 0x5E, 0x61, 0x7A, 0x16, 0x17, 0x61, 0x16, 0x6B, 0x61, 0x4E, 0x69, 0x14, 0x6B, 0x6D, 0x51, 0x57, 0x6D, 0x6D, 0x58, 0x5D, 0x4B]
# flag = ""


# shuffledPos = [i for i in range(0, 50)]

# for i in range(len(inter)):
#     tmp = shuffledPos[i]
#     shuffledPos[i] = shuffledPos[((i + 7) * 15) % 50]
#     shuffledPos[((i + 7) * 15) % 50] = tmp

# for i in range(len(inter)):
#     tmp = shuffledPos[i]
#     shuffledPos[i] = shuffledPos[((i + 3) * 7) % 50]
#     shuffledPos[((i + 3) * 7) % 50] = tmp

# for i in range(len(inter)):
#     tmp = shuffledPos[i]
#     shuffledPos[i] = shuffledPos[((i + 83) * 12) % 50]
#     shuffledPos[((i + 83) * 12) % 50] = tmp

# for i in range(len(inter)):
#     inter[i], inter[shuffledPos[i]] = inter[shuffledPos[i]], inter[i]


# for i in range(len(inter)):
#     inter[i] = inter[i] ^ 0x5 ^ 0x20
#     flag += chr(inter[i])
# print(flag)
