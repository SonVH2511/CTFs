src = [0x4c224c31cbdd25ee,
       0x4b9ccb2d7d03763,
       0x4c754732b404062c,
       0x4d44fe74a5c69d06,
       0x65343e75d717f5d9,
       0x3c26dd9e25bd76fe,
       0xd06d930cadcc39a9]

buf = []
for i in range(6, -1, -1):
    buf.append(src[i] & 0xFFFFFFFF)
    buf.append(src[i] >> 32)

delta = 0x9E3779B9
k0 = 0x54684935
k1 = (0x6fceac95 ^ 0xFFFFFFFF) + 1
k2 = 0x6579666f
k3 = 0x72544541

sum = 0
for i in range(32):
    sum += delta
tmp = sum

for i in range(7):
    sum = tmp
    v0 = buf[i * 2]
    v1 = buf[i * 2 + 1]
    for j in range(32):
        v1 = (v1 - ((sum + v0) ^ (((v0 << 4) + k2) & 0xFFFFFFFF)
              ^ (((v0 >> 5) + k3) & 0xFFFFFFFF))) & 0xFFFFFFFF
        v0 = (v0 - ((sum + v1) ^ (((v1 << 4) + k0) & 0xFFFFFFFF)
              ^ (((v1 >> 5) + k1) & 0xFFFFFFFF))) & 0xFFFFFFFF
        sum -= delta
    buf[i * 2] = v0
    buf[i * 2 + 1] = v1

for i in buf:
    hex_values = hex(i)[2:]
    result_string = ''.join([chr(int(hex_values[i:i+2], 16))
                            for i in range(0, len(hex_values), 2)])
    print(result_string[::-1], end='')
