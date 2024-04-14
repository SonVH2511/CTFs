secret = "Mai ben nhau ban nhe :)"
# true_secret = "9FPIU6vUxfQOHaisOChDY1F"

v7_key = [0x40, 0x46, 0xCE, 0xA9, 0x8C, 0xC4, 0x6D, 0x80, 0x5F, 0xB1,
          0xFE, 0x0F, 0xC2, 0x7E, 0xAA, 0x17, 0xC2, 0xF7, 0x34, 0x27,
          0x62, 0x0A, 0x99, 0xAC, 0x58, 0x30, 0xC1, 0xAC, 0x1D, 0x10,
          0xED, 0x8A, 0xCE]

Buf2 = [0xE3, 0x2E, 0xD0, 0xA6, 0xD6, 0x7D, 0x54, 0x3F, 0xAC, 0xF, 0x24,
        0x10, 0x9C, 0xCB, 0x26, 0xBC, 0xB3, 0x89, 0x84, 0x24, 0x80, 0xBD, 0x48]

this = [i for i in range(0, 256)]
tmp1 = 0
tmp2 = 0

# KSA Phase
for i in range(0, 256):
    tmp1 = (ord(secret[i % 0x17]) + this[i] + tmp1) % 256
    tmp2 = this[i] & 0xff
    this[i] = this[tmp1]
    this[tmp1] = tmp2

# PRGA Phase
i = j = 0
for ch in range(len(Buf2)):
    i = (i + 1) % 256
    j = (j + this[i]) % 256
    this[i], this[j] = this[j], this[i]
    Buf2[ch] = (Buf2[ch] ^ this[(this[i] + this[j]) % 256]) & 0xff

for i in range(len(Buf2)):
    # Buf2[i] = Buf2[i] ^ 0xAA
    Buf2[i] = Buf2[i] ^ 0xAB

for i in Buf2:
    print(chr(i), end='')
print()

# KSA Phase
this = [i for i in range(0, 256)]
tmp1 = 0
tmp2 = 0
for i in range(0, 256):
    tmp1 = (Buf2[i % 0x17] + this[i] + tmp1) % 256
    tmp2 = this[i] & 0xff
    this[i] = this[tmp1]
    this[tmp1] = tmp2

# PRGA Phase
i = j = 0
for ch in range(len(v7_key)):
    i = (i + 1) % 256
    j = (j + this[i]) % 256
    this[i], this[j] = this[j], this[i]
    v7_key[ch] = (v7_key[ch] ^ this[(this[i] + this[j]) % 256]) & 0xff
# for i in range(len(Buf2)):
#     Buf2[i] = Buf2[i] ^ 0xAA


for i in v7_key:
    print(chr(i), end='')
print()

print(hex(0 ^ 0xAA))
print(hex(1 ^ 0xAA))
