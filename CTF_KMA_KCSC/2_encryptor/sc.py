with open("flag.bmp.encrypted", "rb") as encrypted_file:
    lines = encrypted_file.read()

# tmp__ = []
# for i in lines:
#     tmp__.append((i))

# tmp = [tmp__]*1000000

for K in range(4294967296):
    cnt = K
    f = 1
    data = []
    # data = tmp[cnt]
    for i in lines:
        data.append((i))

    key = []
    for num in range(4):
        key.append((K & 0xff))
        K = (K-(K & 0xff)) >> 8
    # print(key)

    this = [i for i in range(0, 256)]
    tmp1 = 0
    tmp2 = 0
    for i in range(0, 256):
        tmp1 = ((key[i % 4]) + this[i] + tmp1) % 256
        tmp2 = this[i] & 0xff
        this[i] = this[tmp1]
        this[tmp1] = tmp2

    i = j = 0
    for ch in range(len(data)):
        i = (i + 1) % 256
        j = (j + this[i]) % 256
        this[i], this[j] = this[j], this[i]
        data[ch] = (data[ch] ^ this[(this[i] + this[j]) % 256]) & 0xff
        if (ch == 0 and data[0] != 66) or (ch == 1 and data[1] != 77):
            f = 0
            break

    if cnt % 1000 == 0:  # check process
        print(cnt)

    if f == 1 and cnt != 19056:
        print(cnt)
        byte_data = bytes(data)
        with open("tmp.bmp", "wb") as encrypted_file:
            encrypted_file.write(byte_data)
        break
    f = 1
