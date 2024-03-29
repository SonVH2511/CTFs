def rol_byte(value, shift):
    return ((value << shift) & 0xFF) | ((value & 0xFF) >> (8 - shift))


flag_comp = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=<>,./{[]\|~:;?"\''
key = [0xC3, 0x83, 0x23, 0x23, 0xB3, 0xC3, 0x83, 0xE3, 0xA3, 0xE3, 0x33, 0x0C]

for i in key:
    for j in flag_comp:
        if (rol_byte((~(ord(j)+96)) & 0xff, 4) ^ 0x55) == i:
            print(j)
# jctf{62881624049}
