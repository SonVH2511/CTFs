__str1 = ''
ans = [0x1EE04D9B, 0xF77CAAAC, 0x44F4ECA3, 0x82E5EFFA]


def rol(value, shift):
    return ((value << shift) & 0xffffffff) | ((value & 0xffffffff) >> (32 - shift))


def solve(cnt):

    for num in range(0x2f2f2f2f, 0x7e7e7e7e):
        # for i in range(32):
        # tmp = (num ^ rol(num, 22))
        if (num ^ rol(num, 22)) == ans[cnt]:
            print("cnt: ", cnt)
            return num


# _hex_L3AK = 0x4c33414b

# for i in range(32):
#     tmp = (_hex_L3AK ^ rol(_hex_L3AK, i))
#     if tmp == 0x1EE04D9B:
#         print(i)


for cnt in range(4):
    print(hex(solve(cnt)))

# cnt: 0
# 0x4c33414b
# cnt: 1
# 0x7b627230
# cnt: 2
# 0x5f63346e
# cnt: 3
# 0x5f723376
