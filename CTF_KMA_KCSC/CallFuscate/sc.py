key = [0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01,
       0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76, 0xCA, 0x82, 0xC9, 0x7D,
       0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4,
       0x72, 0xC0, 0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC,
       0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15, 0x04, 0xC7,
       0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2,
       0xEB, 0x27, 0xB2, 0x75, 0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E,
       0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
       0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB,
       0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF, 0xD0, 0xEF, 0xAA, 0xFB,
       0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C,
       0x9F, 0xA8, 0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5,
       0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2, 0xCD, 0x0C,
       0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D,
       0x64, 0x5D, 0x19, 0x73, 0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A,
       0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
       0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3,
       0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79, 0xE7, 0xC8, 0x37, 0x6D,
       0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A,
       0xAE, 0x08, 0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6,
       0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A, 0x70, 0x3E,
       0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9,
       0x86, 0xC1, 0x1D, 0x9E, 0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9,
       0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
       0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99,
       0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16]

ans = [0xE5, 0xA8, 0x07, 0x2E, 0xE8, 0x67, 0xB5, 0x0C, 0xF9, 0x05,
       0xA1, 0xA8, 0xFA, 0x05, 0x0A, 0x66, 0xA0, 0xC1, 0x20, 0x4E,
       0xE3, 0x7D, 0xD0, 0x04, 0x21, 0x67, 0xEC, 0x9E, 0x7D, 0xBC,
       0x2D, 0x8D, 0x9B, 0x65, 0xDC, 0x71, 0xE4, 0x57, 0x81, 0x11,
       0x1A, 0x71, 0x7F, 0x84, 0x2C, 0x88, 0x25, 0x94]

seed = "confused"

# tmp = [0xAC, 0x67, 0x94, 0x90, 0x9C, 0xE4, 0x16, 0x93, 0xAC, 0x67, 0x94, 0x90, 0x9C, 0xE4, 0x16, 0x93, 0xAC, 0x67, 0x94, 0x90, 0x9C, 0xE4, 0x16, 0x93,
#        0xAC, 0x67, 0x94, 0x90, 0x9C, 0xE4, 0x16, 0x93, 0xAC, 0x67, 0x94, 0x90, 0x9C, 0xE4, 0x16, 0x93, 0xAC, 0x67, 0x94, 0x90, 0x9C, 0xE4, 0x16, 0x93]
# print(len(tmp))


def ror(n, rotations=1, bits=8):
    return ((n >> rotations) | (n << (bits - rotations))) & ((1 << bits) - 1)


def rol(n, rotations=1, bits=8):
    return ((n << rotations) | (n >> (bits - rotations))) & ((1 << bits) - 1)


flag_comp = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=<>,.?/{}[]\|~:;"\''

flag = ""


for i in range(0, len(ans), 8):
    for cnt in range(100):
        for j in range(256):
            if ((key[(ord(seed[7]) + ans[i+7]) & 0xff]) + j) & 0xff == ror(ans[i+0]):
                ans[i+0] = j
                break
        for j in range(256):
            if ((key[(ord(seed[6]) + ans[i+6]) & 0xff]) + j) & 0xff == ror(ans[i+7]):
                ans[i+7] = j
                break
        for j in range(256):
            if ((key[(ord(seed[5]) + ans[i+5]) & 0xff]) + j) & 0xff == ror(ans[i+6]):
                ans[i+6] = j
                break
        for j in range(256):
            if ((key[(ord(seed[4]) + ans[i+4]) & 0xff]) + j) & 0xff == ror(ans[i+5]):
                ans[i+5] = j
                break
        for j in range(256):
            if ((key[(ord(seed[3]) + ans[i+3]) & 0xff]) + j) & 0xff == ror(ans[i+4]):
                ans[i+4] = j
                break
        for j in range(256):
            if ((key[(ord(seed[2]) + ans[i+2]) & 0xff]) + j) & 0xff == ror(ans[i+3]):
                ans[i+3] = j
                break
        for j in range(256):
            if ((key[(ord(seed[1]) + ans[i+1]) & 0xff]) + j) & 0xff == ror(ans[i+2]):
                ans[i+2] = j
                break
        for j in range(256):
            if ((key[(ord(seed[0]) + ans[i+0]) & 0xff]) + j) & 0xff == ror(ans[i+1]):
                ans[i+1] = j
                break

for k in ans:
    print(hex(k), end=" ")
print()
for k in ans:
    flag += chr(k)
    # print(chr(k), end="")
print(flag)

# dưới đây là nháp

# print(hex((key[0x69]+0x6b) & 0xff))


# print()

# for i in range(0, len(ans), 8):
#     for j in range(100):
#         ans[i+1] = rol(key[(ord(seed[0]) + ans[i+0]) & 0xff]+ans[i+1])
#         ans[i+2] = rol(key[(ord(seed[1]) + ans[i+1]) & 0xff]+ans[i+2])
#         ans[i+3] = rol(key[(ord(seed[2]) + ans[i+2]) & 0xff]+ans[i+3])
#         ans[i+4] = rol(key[(ord(seed[3]) + ans[i+3]) & 0xff]+ans[i+4])
#         ans[i+5] = rol(key[(ord(seed[4]) + ans[i+4]) & 0xff]+ans[i+5])
#         ans[i+6] = rol(key[(ord(seed[5]) + ans[i+5]) & 0xff]+ans[i+6])
#         ans[i+7] = rol(key[(ord(seed[6]) + ans[i+6]) & 0xff]+ans[i+7])
#         ans[i+0] = rol(key[(ord(seed[7]) + ans[i+7]) & 0xff]+ans[i+0])
#         ans[i+0] = ror(key[(ord(seed[7]) + ans[i+7]) & 0xff]+ans[i+0])
#         ans[i+7] = ror(key[(ord(seed[6]) + ans[i+6]) & 0xff]+ans[i+7])
#         ans[i+6] = ror(key[(ord(seed[5]) + ans[i+5]) & 0xff]+ans[i+6])
#         ans[i+5] = ror(key[(ord(seed[4]) + ans[i+4]) & 0xff]+ans[i+5])
#         ans[i+4] = ror(key[(ord(seed[3]) + ans[i+3]) & 0xff]+ans[i+4])
#         ans[i+3] = ror(key[(ord(seed[2]) + ans[i+2]) & 0xff]+ans[i+3])
#         ans[i+2] = ror(key[(ord(seed[1]) + ans[i+1]) & 0xff]+ans[i+2])
#         ans[i+1] = ror(key[(ord(seed[0]) + ans[i+0]) & 0xff]+ans[i+1])

# print(hex(ror(key[(ord("k")+ord("c")) & 0xff]+ord("m"))))
# print(hex(key[(ord("k")+ord("c")) & 0xff]+ord("m")))
# print(hex(ror(0xf1)))

# ans = [0xc8, 0xf1, 0x62, 0xa7, 0x96, 0x23, 0x16, 0x05]
# ans = [0x6b, 0x6d, 0x61, 0x63, 0x74, 0x66, 0x7b, 0x61]

# for j in range(100):
# print()

# ans[i+1] = ror((key[(ord(seed[0]) + ans[i+0]) & 0xff]+ans[i+1]) & 0xff)
# ans[i+2] = ror((key[(ord(seed[1]) + ans[i+1]) & 0xff]+ans[i+2]) & 0xff)
# ans[i+3] = ror((key[(ord(seed[2]) + ans[i+2]) & 0xff]+ans[i+3]) & 0xff)
# ans[i+4] = ror((key[(ord(seed[3]) + ans[i+3]) & 0xff]+ans[i+4]) & 0xff)
# ans[i+5] = ror((key[(ord(seed[4]) + ans[i+4]) & 0xff]+ans[i+5]) & 0xff)
# ans[i+6] = ror((key[(ord(seed[5]) + ans[i+5]) & 0xff]+ans[i+6]) & 0xff)
# ans[i+7] = ror((key[(ord(seed[6]) + ans[i+6]) & 0xff]+ans[i+7]) & 0xff)
# ans[i+0] = ror((key[(ord(seed[7]) + ans[i+7]) & 0xff]+ans[i+0]) & 0xff)

# for i in range(255):
#     if ((0xf9 + i) & 0xff) == 0x64:
#         print(hex(i))

# print(hex(key[(ord(seed[7]) + ans[7]) & 0xff]))

# print(hex(0xf9+0x6b))
# print(hex(0x64 & 0xff))
# i = 0
# for j in range(256):
#     if ((key[(ord(seed[7]) + ans[i+7]) & 0xff]) + j) & 0xff == ror(ans[i+0]):
#         ans[i+0] = j
#         print(hex(j))


# for i in range(0, len(ans), 8):
# for i in range(9):

# i = 0

# ans[i+0] = ror(ans[i+0])-(key[(ord(seed[7]) + ans[i+7]) & 0xff])
# ans[i+7] = ror(ans[i+7])-(key[(ord(seed[6]) + ans[i+6]) & 0xff])
# ans[i+6] = ror(ans[i+6])-(key[(ord(seed[5]) + ans[i+5]) & 0xff])
# ans[i+5] = ror(ans[i+5])-(key[(ord(seed[4]) + ans[i+4]) & 0xff])
# ans[i+4] = ror(ans[i+4])-(key[(ord(seed[3]) + ans[i+3]) & 0xff])
# ans[i+3] = ror(ans[i+3])-(key[(ord(seed[2]) + ans[i+2]) & 0xff])
# ans[i+2] = ror(ans[i+2])-(key[(ord(seed[1]) + ans[i+1]) & 0xff])
# ans[i+1] = ror(ans[i+1])-(key[(ord(seed[0]) + ans[i+0]) & 0xff])

# print()
# print(hex(ord('d')))
# print(hex(key[0x05+ord('d')]))
# print(hex(0x05+ord('d')))
# for i in ans:
#     print(hex(ror(i)), end=" ")
# print()
# i = 0
# ans[i+0] = ror(ans[i+0])-(key[(ord(seed[7]) + ans[i+7]) & 0xff])
# ans[i+7] = ror(ans[i+7])-(key[(ord(seed[6]) + ans[i+6]) & 0xff])
# ans[i+6] = ror(ans[i+6])-(key[(ord(seed[5]) + ans[i+5]) & 0xff])
# ans[i+5] = ror(ans[i+5])-(key[(ord(seed[4]) + ans[i+4]) & 0xff])
# ans[i+4] = ror(ans[i+4])-(key[(ord(seed[3]) + ans[i+3]) & 0xff])
# ans[i+3] = ror(ans[i+3])-(key[(ord(seed[2]) + ans[i+2]) & 0xff])
# ans[i+2] = ror(ans[i+2])-(key[(ord(seed[1]) + ans[i+1]) & 0xff])
# ans[i+1] = ror(ans[i+1])-(key[(ord(seed[0]) + ans[i+0]) & 0xff])

# ans[i+0] = ror((key[(ord(seed[7]) + ans[i+7]) & 0xff]+ans[i+0]) & 0xff)
# ans[i+7] = ror((key[(ord(seed[6]) + ans[i+6]) & 0xff]+ans[i+7]) & 0xff)
# ans[i+6] = ror((key[(ord(seed[5]) + ans[i+5]) & 0xff]+ans[i+6]) & 0xff)
# ans[i+5] = ror((key[(ord(seed[4]) + ans[i+4]) & 0xff]+ans[i+5]) & 0xff)
# ans[i+4] = ror((key[(ord(seed[3]) + ans[i+3]) & 0xff]+ans[i+4]) & 0xff)
# ans[i+3] = ror((key[(ord(seed[2]) + ans[i+2]) & 0xff]+ans[i+3]) & 0xff)
# ans[i+2] = ror((key[(ord(seed[1]) + ans[i+1]) & 0xff]+ans[i+2]) & 0xff)
# ans[i+1] = ror((key[(ord(seed[0]) + ans[i+0]) & 0xff]+ans[i+1]) & 0xff)

# ans[i+0] = ror(key[(ord(seed[7]) + ans[i+7]) & 0xff]+ans[i+0])
# ans[i+7] = ror(key[(ord(seed[6]) + ans[i+6]) & 0xff]+ans[i+7])
# ans[i+6] = ror(key[(ord(seed[5]) + ans[i+5]) & 0xff]+ans[i+6])
# ans[i+5] = ror(key[(ord(seed[4]) + ans[i+4]) & 0xff]+ans[i+5])
# ans[i+4] = ror(key[(ord(seed[3]) + ans[i+3]) & 0xff]+ans[i+4])
# ans[i+3] = ror(key[(ord(seed[2]) + ans[i+2]) & 0xff]+ans[i+3])
# ans[i+2] = ror(key[(ord(seed[1]) + ans[i+1]) & 0xff]+ans[i+2])
# ans[i+1] = ror(key[(ord(seed[0]) + ans[i+0]) & 0xff]+ans[i+1])

# tmp = "kmactf{a"

# for i in tmp:
#     print(hex(ord(i)), end=",")

# print(chr(0x7b))

# print(chr(0x69))

# print(hex(0xF8-key[ord("c")+ord("k")]))
# print(chr(0x6d))


# print(hex(key[(ord(seed[0]) + ans[i+0]) & 0xff]+ans[i+1]))
# print(hex(ror(key[(ord(seed[7]) + ans[i+7]) & 0xff]+ans[i+0])))
# print(hex(ror(0xf1)))

# print(0xca-0xc8)
# print(chr(0x64))
# print(hex(0x64+0x05))


# print(chr(0x6d))
# print(hex(ord("k")+ord("c")))


# print(ans)
# print(hex(ord("m")))
# print(hex(ord('b')))


# print(chr(0xa8))


# for i in key:
#     flag += chr(i)
# print(flag)

# print(ror(25))

# print(len(key))

# print(ord(seed[7])

# print(i)

# flag = "kmactf{abcdefghiklmaaaaaaaaaaaaaaaaaaaaaaaaaaaa}"

# # print(0x38)
# print(48/8)

# print(len(flag))

# print("kmactf{" + "a"*(48-8)+"}")

# print(len(ans))

# flag = " kmactf{12341234qwerqwer}"
# print(hex(len(flag)))

# res = 0x64657375666E6F63
# while res != 0:
#     print(chr(res & 0xff), end="")
#     res >>= 8
# print(chr(res & 0xff))
