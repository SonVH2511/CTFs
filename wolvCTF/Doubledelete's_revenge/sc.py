def ror(n, rotations=13, bits=32):
    return ((n >> rotations) | (n << (bits - rotations))) & ((1 << bits) - 1)


flag = ""
final_ouput = []
segment = []
enc_flag = []
with open("flag.txt.enc", 'rb') as file:
    enc_flag = file.read()

for i in range(0, len(enc_flag), 4):
    segment.append(int.from_bytes(enc_flag[i:i+4], byteorder='little'))

for i in segment:
    tmp = ror(i)
    final_ouput.append(tmp.to_bytes(4, byteorder='little'))

for i in final_ouput:
    flag += i.decode()

print(flag)
# wctf{i_th1nk_y0u_m1sund3rst00d_h0w_r0t13_w0rk5}
