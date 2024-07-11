key = "LLURULDUL"
# cipher = [0x33122A35, 0xB2645787, 0x34A6EF00, 0x3EDEE001, 0x40EC2101,
#           0xB0691D26, 0x7BB269B0, 0x6EB2256, 0xCB5DF2BE, 0x512B0F79,0x55]
cipher = [0x35, 0x2a, 0x12, 0x33, 0x87, 0x57, 0x64, 0xb2, 0x0, 0xef, 0xa6, 0x34, 0x1, 0xe0, 0xde, 0x3e, 0x1, 0x21, 0xec,
          0x40, 0x26, 0x1d, 0x69, 0xb0, 0xb0, 0x69, 0xb2, 0x7b, 0x56, 0x22, 0xeb, 0x6, 0xbe, 0xf2, 0x5d, 0xcb, 0x79, 0xf, 0x2b, 0x51, 0x55]


def rc4(secret, Buf2):
    this = [i for i in range(0, 256)]
    tmp1 = 0
    tmp2 = 0

    # KSA Phase
    for i in range(0, 256):
        tmp1 = (ord(secret[i % len(secret)]) + this[i] + tmp1) % 256
        tmp2 = this[i] & 0xFF
        this[i] = this[tmp1]
        this[tmp1] = tmp2

    # PRGA Phase
    i = j = 0
    for ch in range(len(Buf2)):
        i = (i + 1) % 256
        j = (j + this[i]) % 256
        this[i], this[j] = this[j], this[i]
        Buf2[ch] = (Buf2[ch] ^ this[(this[i] + this[j]) % 256]) & 0xFF


rc4(key, cipher)
for i in cipher:
    print(chr(i), end="")
print()
print(cipher)
print(len(cipher))
# U_cRackeD_th1$_maG1cBaLL_!!_@flare-on.com
# U_cRackeD_th1$_maG1cBaLL_!!_@flare-on.co

#   v45 = 0;
#   v36[0] = 0x33122A35;
#   v36[1] = 0xB2645787;
#   v36[2] = 0x34A6EF00;
#   v36[3] = 0x3EDEE001;
#   v36[4] = 0x40EC2101;
#   v36[5] = 0xB0691D26;
#   v36[6] = 0x7BB269B0;
#   v36[7] = 0x6EB2256;
#   v36[8] = 0xCB5DF2BE;
#   v36[9] = 0x512B0F79;
#   v36[10] = 0x55;

#   v37 = 85;
#   v42 = 0;
#   v43 = 15;
