from z3 import *
cipher = [0xD1, 0x46, 0x40, 0x91, 0x2F, 0x64, 0x42, 0xD6, 0xE9, 0x2D,
          0x19, 0x28, 0x10, 0xC8, 0x79, 0x88, 0x70, 0x32, 0xC6, 0x47,
          0x35, 0x8D, 0x33, 0xE7, 0xB8, 0x70, 0xF2, 0x87, 0xDB, 0xDB,
          0xDB, 0xFD, 0x26, 0x5B, 0xA6, 0xB5, 0xA5, 0xDF, 0x9A, 0x5B,
          0x57, 0xB7, 0xB5, 0x7D, 0xC4, 0xAD, 0xE5, 0xC4, 0x72, 0x56,
          0x58, 0x11, 0x2B, 0xAB, 0x86, 0x5A, 0x76, 0x8A, 0x67, 0x3E,
          0x82, 0x8C, 0x74, 0x91, 0xC9, 0x66, 0x32, 0x1D, 0x3D, 0xD3,
          0x33, 0x80, 0xD1, 0x10, 0xE7, 0xC7, 0x59, 0x4E, 0x31, 0x65,
          0x91, 0xED, 0x66, 0x18, 0xBE, 0x9B, 0x0C, 0x26, 0x78, 0x75,
          0xE7, 0x9E, 0x0C, 0xE8, 0xC2, 0xE6, 0xFC, 0x3C, 0x53, 0x8C,
          0xC1, 0x0B, 0x2A, 0x12, 0x31, 0xAA, 0xA8, 0x32, 0x1B, 0x68,
          0x90, 0x68, 0xF9, 0xBC, 0x73, 0xB7, 0x3E, 0xE4, 0x09, 0xAE,
          0xC9, 0xE9, 0xCD, 0xAC, 0x8A, 0xC4, 0x8C, 0x4F, 0x0F, 0x68,
          0xDA, 0xA8, 0x76, 0x2A, 0x8A, 0x6D, 0x53, 0x7F, 0xAC, 0xD5,
          0xFE, 0x3C, 0x9F, 0x5C, 0x9A, 0x15, 0x22, 0x16, 0x7F, 0x1C,
          0xCC, 0x92, 0x13, 0x51, 0xBF, 0xCF, 0x7C, 0x95, 0xCA, 0xFF,
          0xCB, 0x59, 0xAF, 0xE9, 0x25, 0x0F, 0x4A, 0xA6, 0x4C, 0x1E,
          0x7A, 0xD4, 0x2D, 0x58, 0xB0, 0xB0, 0x2A, 0xD6, 0xB5, 0x8C,
          0xBF, 0x15, 0xA7, 0xB3, 0x77, 0xEB, 0xEA, 0x03, 0xD0, 0x4A,
          0xC4, 0x65, 0x9B, 0xD4, 0xC1, 0xE8, 0xD8, 0xB6, 0x44, 0xE1,
          0x5B, 0x1E, 0x99, 0x1C, 0x7E, 0xDF, 0xB5, 0x62, 0x27, 0xB2,
          0x93, 0x5E, 0xFA, 0x39, 0x70, 0xBF, 0x58, 0x4F, 0x23, 0xAF,
          0x6A, 0xA7, 0xAD, 0x48, 0xE8, 0x14, 0x19, 0x76, 0x20, 0x1D,
          0x1D, 0x63, 0x03, 0x42, 0xF3, 0x1D, 0x63, 0x03, 0x42, 0xF3,
          0x17, 0xAF, 0x87, 0xBC, 0x87, 0x26, 0xEC, 0x84, 0x84, 0xAC,
          0x85, 0x4D, 0xFD, 0xF7, 0x09, 0x1F, 0x55, 0x86, 0x90, 0x21,
          0x81, 0xC8, 0xC8, 0xDA, 0x75, 0x4D, 0xAF, 0x15, 0xAF, 0x4E,
          0xEE, 0x99, 0x69, 0x39, 0xB0, 0x7A, 0xF6, 0xFB, 0x94, 0x16,
          0x41, 0x48, 0xEC, 0x38, 0x28, 0xCD, 0x05, 0x1C, 0xC6, 0x49,
          0xCE, 0x18, 0xE0, 0x1A, 0x6E, 0x66, 0xE4, 0xA4, 0xF2, 0x96,
          0x4B, 0xEC, 0x74, 0x24, 0xA7, 0xEF, 0xDA, 0x64, 0x0A, 0x8A,
          0xA3, 0x29, 0xD7, 0xD8, 0xB5, 0x0A, 0xC1, 0x42, 0x08, 0xDC,
          0x46, 0x2B, 0x33, 0x22, 0xF3, 0xC9, 0xDF, 0x22, 0x69, 0xCD,
          0x66, 0xCF, 0x04, 0x2A, 0x07, 0x01, 0x2F, 0x05, 0xB6, 0x07,
          0xBA, 0xF8, 0xE5, 0x7E, 0x9B, 0x52, 0xFC, 0x91, 0x49, 0x86,
          0x25, 0xA3, 0x2E, 0x64, 0x9E, 0xF1, 0xFC, 0x0F, 0x35, 0x21,
          0x28, 0x6D, 0x48, 0x63, 0xF5, 0x11, 0xD5, 0xC8, 0xD4, 0xC1,
          0xD0, 0x05, 0x9C, 0x5C, 0xAA, 0x49, 0x1B, 0xEF, 0x75, 0xBD,
          0x6A, 0x90, 0xBD, 0x13, 0x76, 0x6E, 0xAD, 0xFF, 0xE2, 0xFB,
          0x25, 0x39, 0xBA, 0x15, 0x2D, 0xC3, 0x61, 0x75, 0x8E, 0xD7,
          0xAD, 0xD4, 0x68, 0xE4, 0x2C, 0x7C, 0xE8, 0xD1, 0x46, 0x74,
          0x49, 0x5F, 0x26, 0x01, 0xED, 0x84, 0xCD, 0x71, 0x2D, 0x27,
          0x73, 0xE9, 0xAB, 0x87, 0x09, 0x14, 0xF0, 0x51, 0x0E, 0xCC,
          0x0C, 0xCE, 0xBF, 0xBB, 0x2F, 0x86, 0x09, 0x89, 0x46, 0xDA,
          0x59, 0x3C, 0x4D, 0xC4, 0x88, 0x19, 0x63, 0xF9, 0xA0, 0x76,
          0x26, 0x45, 0x2D, 0xA4, 0x66, 0x76, 0x5B, 0x71, 0x21, 0x13,
          0x36, 0xC1, 0x77, 0xEC, 0xF4, 0xF3, 0xED, 0x11, 0xA8, 0xF0,
          0x2B, 0x4B, 0xA8, 0xA2, 0xB7, 0x32, 0x53, 0x58, 0x6B, 0xD1,
          0x27, 0xEB, 0xE2, 0x05, 0xE7, 0x1F, 0x58, 0x68, 0x07, 0x3C,
          0x9D, 0x1E, 0x30, 0x22, 0xC9, 0xA5, 0x85, 0x41, 0xD4, 0xDE,
          0x45, 0x28, 0xB1, 0x26, 0x61, 0x16, 0xBB, 0x58, 0xF8, 0xB2,
          0xAD, 0xF4, 0xEC, 0x9B, 0x92, 0x13, 0x0D, 0x64, 0xDA, 0x8F,
          0x08, 0xD4, 0xF1, 0xCC, 0xEA, 0x33, 0xC1, 0x1B, 0xC5, 0x6D,
          0xF6, 0xAB, 0x4E, 0x1F, 0x3F, 0x67, 0x7A, 0xF0, 0xE0, 0xEF,
          0x1D, 0xA5, 0x3A, 0x18, 0xDD, 0x3B, 0x3C, 0x65, 0xA5, 0x07,
          0x5D, 0x89, 0x29, 0xAC, 0xEA, 0x8B, 0x23, 0x2B, 0xD3, 0x58,
          0x3B, 0xBC, 0xCC, 0x69, 0x3B, 0x20, 0x64, 0xE4, 0xDB, 0xCD,
          0x4E, 0x61, 0xAC, 0x17, 0xAF, 0x98, 0xEA, 0xEA, 0x87, 0xDF,
          0xDD, 0x36, 0x41, 0xF3, 0x46, 0x0D, 0x6B, 0xC9, 0xB1, 0x71,
          0xF6, 0x0E, 0xD9, 0x0C, 0x7E, 0xA1, 0x43, 0xCD, 0x83, 0x04,
          0xA4, 0x6A, 0xA9, 0x60, 0x14, 0x4D, 0x77, 0x88, 0x04, 0xBF,
          0x3E, 0x51, 0xAB, 0xBE, 0x09, 0x2C, 0xC0, 0xE6, 0x1F, 0xE5,
          0x42, 0xFF, 0x15, 0x32, 0xFC, 0x4A, 0x22, 0x94, 0xF8, 0x66,
          0xCA, 0x8D, 0x91, 0xAF, 0x8B, 0x61, 0xA4, 0x38, 0x17, 0x1E,
          0xD4, 0x6F, 0x19, 0x50, 0xBF, 0x68, 0xB0, 0x12, 0x91, 0x2A,
          0xC0, 0x83, 0x12, 0xBD, 0x0C, 0x69, 0xC9, 0x95, 0xAC, 0x6E,
          0xCF, 0xCE, 0xAE, 0xB4, 0x58, 0x6F, 0xA4, 0x26, 0xB8, 0x9C,
          0x40, 0x54, 0x5B, 0xB1, 0x48, 0x80, 0xD2, 0x62, 0xC3, 0xBD,
          0x8A, 0xFA, 0x60, 0x10, 0x17, 0xB2, 0xE8, 0x35, 0x11, 0x64,
          0x85, 0x70, 0x3C, 0x9A, 0x10, 0x2A, 0x12, 0xD9, 0x9F, 0xBE,
          0x69, 0x35, 0x63, 0x5E, 0x4A, 0x2F, 0x11, 0x50, 0xE2, 0x34,
          0x78, 0x0E, 0xBD, 0x85, 0x57, 0x15, 0xAE, 0x7C, 0x0B, 0x85,
          0xFA, 0x15, 0xDF, 0xF9, 0xA3, 0x7E, 0x0C, 0x15, 0xD8, 0x82,
          0x86, 0xDD, 0xFE, 0x51, 0xDA, 0xA9, 0x31, 0x22, 0xDA, 0xDB,
          0x0B, 0xFF, 0xE7, 0x33, 0x63, 0xA3, 0xEA, 0xE2, 0x61, 0x35,
          0x19, 0x62, 0x35, 0x87, 0x13, 0xDE, 0x35, 0x85, 0xFC, 0x18,
          0x42, 0xBC, 0x12, 0x0E, 0x77, 0x61, 0x25, 0x6C, 0x97, 0x1A,
          0x2D, 0x72, 0x41, 0x1B, 0x99, 0x49, 0xAE, 0x7E, 0x97, 0x66,
          0x72, 0x58, 0x48, 0xF9, 0x25, 0x61, 0x81, 0x38, 0x83, 0x6A,
          0x7E, 0x71, 0xA0, 0x02, 0x38, 0x50, 0x93, 0x6D, 0xD3, 0x59,
          0xC0, 0xE3, 0x3E, 0xD7, 0xA7, 0xC4, 0x8B, 0x5A, 0x49, 0x0C,
          0x1B, 0x0B, 0x75, 0xD7, 0x96, 0x97, 0x1D, 0x32, 0xF9, 0x11,
          0x24, 0xB0, 0xEE, 0x4C, 0x91, 0x9D, 0x66, 0x51, 0xA9, 0x3C,
          0x4C, 0x41, 0xB8, 0xE5, 0xE7, 0x9A, 0x22, 0xD4, 0xF3, 0x1D,
          0xBB, 0x3A, 0x06, 0x88, 0x2C, 0x07, 0x27, 0x85, 0x74, 0x0C,
          0x0A, 0xB3, 0x99, 0x05, 0x2A, 0x60, 0xDF, 0x02, 0x7B, 0x60,
          0xBB, 0xE5, 0xC4, 0xB7, 0x30, 0x57, 0x14, 0x81, 0x6D, 0xE5,
          0x88, 0xD1, 0x43, 0x13, 0x83, 0x32, 0x99, 0xBF, 0x4D, 0x56,
          0xC6, 0xA1, 0x2F, 0x66, 0x53, 0x87, 0xB3, 0x93, 0x14, 0xA3,
          0x5E, 0x5E, 0x87, 0x86, 0x79, 0x33, 0xEC, 0xF1, 0xC0, 0x64,
          0xAB, 0xF2, 0x23, 0x4D, 0x40, 0xDC, 0xC3, 0xC4, 0x3F, 0x3A,
          0x15, 0x28, 0xB7, 0x86, 0xE1, 0xD7, 0x15, 0xDA, 0x74, 0xC1,
          0x05, 0x44, 0x46, 0x05, 0x28, 0x07, 0xD6, 0xBE, 0xAF, 0x5C,
          0xA8, 0x3B, 0x0B, 0x14, 0x4E, 0x14, 0xCF, 0xB7, 0xF1, 0xAB,
          0x7C, 0xF5, 0x63, 0xF0, 0xDC, 0xC2, 0x30, 0xDB, 0xC5, 0x2F,
          0xB9, 0xC5, 0x57, 0x2A, 0xBF, 0x50, 0xF5, 0x39, 0x5D, 0x5A,
          0x76, 0x63, 0x93, 0x7B, 0x61, 0x1D, 0x12, 0xE7, 0xC3, 0x0B,
          0x61, 0xA9, 0xFB, 0x26, 0x15, 0x62, 0xBA, 0x32, 0x35, 0x4E,
          0x09, 0xC2, 0x32, 0x31, 0xB2, 0x95, 0xD5, 0x8E, 0x51, 0xA2,
          0xC3, 0x34, 0x1D, 0xB8, 0x61, 0x8D, 0x25, 0xB5, 0x97, 0x1D,
          0x02, 0xFA, 0x55, 0xF9, 0xA3, 0xB1, 0x4A, 0xBA, 0x4C, 0xBE,
          0x2B, 0x41, 0xA8, 0x71, 0x5F, 0x1B, 0xDD, 0x2C, 0x54, 0x76,
          0x58, 0xC1, 0xDE, 0x6E, 0x2A, 0x7C, 0x5F, 0x93, 0xA1, 0x04,
          0xDF, 0x45, 0x31, 0xE0, 0x11, 0x32, 0x47, 0x9B, 0x1C, 0x0D,
          0x04, 0x92, 0x02, 0x44, 0x29, 0xB2, 0x11, 0x32, 0x7C, 0xD6,
          0xF1, 0x2E, 0xBE, 0xB3, 0xA9, 0x04, 0xE9, 0xFA, 0x51, 0x0F,
          0x28, 0x45, 0x3E, 0x83, 0x2B, 0x6F, 0x6D, 0xFA, 0xE8, 0x85,
          0x52, 0x0F, 0x97, 0x93, 0x1D, 0xA3, 0xF0, 0xAB, 0x07, 0x3F,
          0xB8, 0x3A, 0x30, 0xF8, 0x92, 0x2D, 0x04, 0x98, 0x27, 0x06,
          0xA0, 0xC2, 0x5C, 0x1D, 0xBE, 0x08, 0x60, 0x1E, 0xD7, 0x3F,
          0x77, 0x02, 0xDF, 0x77, 0x2C, 0xA3, 0xCE, 0x64, 0x99, 0x51]
# target = [0x0F, 0x21, 0xCB, 0x47, 0xF6, 0xB0, 0x0E, 0xA0, 0x69, 0x51,
#           0x5A, 0x08, 0x47, 0x7E, 0x21, 0xD5, 0x8E, 0x31, 0xF4, 0xD6,
#           0xAF, 0xD0, 0x9A, 0x40, 0x03, 0x2B, 0xD6, 0x4C, 0xD7, 0x58,
#           0xD1, 0x47, 0xD6, 0xA9, 0x9E, 0x29, 0x64, 0x73, 0xAA, 0x48,
#           0xDF, 0x46, 0xC2, 0xBA]
target = [0x41, 0xA5, 0xC3, 0xC7, 0x9A, 0x35, 0x7E, 0xE9, 0x20, 0xB8,
          0x4C, 0xB8, 0x46, 0x50, 0x29, 0x0A, 0xAC, 0xC2, 0x19, 0xFA,
          0xAB, 0xCC, 0xE4, 0xF4, 0x92, 0x68, 0xFE, 0xDF, 0xD6, 0x22,
          0xAA, 0x2A, 0x3D, 0xA5, 0x3A, 0x58, 0x28, 0x84, 0x35, 0x0F,
          0xE6, 0xE9, 0x31, 0x92]
# print(len(target))
# inp = [BitVec('x1[%d]'%i, 8) for i in range(44)]
# s = Solver()
# for i in range(len(inp)):
#     s.add(inp[i] > 0x20)
#     s.add(inp[i] < 0x7f)

# print("*"*44)
# FAKE HEADER: de(RYpt3d_bu
Str = "KCSC{kcscctf*******************************}"
Input = [BitVec('x1[%d]' % i, 8) for i in range(44)]
s = Solver()
for i in range(len(Input)):
    s.add(Input[i] > 0x20)
    s.add(Input[i] < 0x7f)
header = 'KCSC{kcscctf'
# header ='de(RYpt3d_bu'

for i in range(len(header)):
    s.add(Input[i] == ord(header[i]))
# for i in range(12):
#     s.add(Input[i] == ord(Str[i]))
# for i in Str:
#     Input.append(ord(i))
_len = 44
_24 = 24
# print(0x2c)
# print(len(Input))

v2 = 0
v32 = 0
v17 = 0
for j in range(_24):
    v7 = Input[0]
    if j & 1 != 0:
        for v6 in range(_len):
            _mod3 = v32 % 3
            if _mod3 == 0:
                # if i == _len-1:
                # v7 = Input[i]
                # v34 = Input[v6+1]
                if v6 != _len-1:
                    # print(v6)
                    # print(Input[v6+1])
                    # v7 = Input[v6+1]
                    Input[v6] = (Input[v6] ^ (Input[v6+1]-cipher[v2])) & 0xff
                else:
                    Input[v6] = (Input[v6] ^ (v7-cipher[v2])) & 0xff
            elif (_mod3 - 1) == 1:
                if v6 == _len-1:
                    Input[v6] = (((v7 + cipher[v2]) & 0xff) - Input[v6]) & 0xff
                else:
                    Input[v6] = ((cipher[v2] + Input[v6+1])-Input[v6]) & 0xff
            else:
                if v6 == _len-1:
                    Input[v6] = (Input[v6] + (v7 ^ cipher[v2])) & 0xff
                    # Input[v6] &= 0xff
                else:
                    Input[v6] = (Input[v6] + (cipher[v2] ^ Input[v6+1])) & 0xff
                    # Input[v6] &= 0xff
            v32 += 1
            v2 += 1
    else:
        v5 = 0
        v24 = 0
        for v6 in range(_len):
            _mod3 = v32 % 3

            if _mod3 == 0:
                if v6 == 0:
                    v5 = Input[0] ^ cipher[v2]
                else:
                    v24 = Input[v6] ^ ((Input[v6-1]-cipher[v2]) & 0xff)
                    Input[v6-1] = v5
                    v5 = v24
            elif (_mod3 - 1) == 1:
                if v6 == 0:
                    v5 = (Input[0] - cipher[v2]) & 0xff
                else:
                    v24 = (Input[v6-1] + cipher[v2] - Input[v6]) & 0xff
                    Input[v6-1] = v5
                    v5 = v24
            else:
                if v6 == 0:
                    v5 = (Input[0] + cipher[v2]) & 0xff
                else:
                    v24 = (Input[v6] + (Input[v6-1] ^ cipher[v2])) & 0xff
                    Input[v6-1] = v5
                    v5 = v24

            if v6 == _len-1:
                Input[v6] = v5
            v32 += 1
            v2 += 1

for i in range(44):
    s.add(Input[i] == target[i])

if s.check() == sat:
    print(s.model())
else:
    print('Fail')