from z3 import *

# a1 = [0]*6
# param_1 = [BitVec(f'a1[{i}]', 32) for i in range(6)]
solver = Solver()


def sub_40163D(a1, a2):
    v9 = 0
    v5 = 0
    v6 = 0
    for i in range(32):
        v7 = a1 & 1
        v8 = a2 & 1
        a1 >>= 1
        a2 >>= 1
        v9 += ((v5 ^ v8 ^ v7) << v6) & 0xffffffff
        v5 = v5 & v7 | v8 & v7 | v5 & v8
        v6 += 1
    return (((v5 << v6) & 0xffffffff) + v9) & 0xffffffff


def sub_40174A(a1, a2):
    v5 = 0
    v6 = 0
    for i in range(32):
        v7 = a1 & 1
        v8 = a2 & 1
        a1 >>= 1
        a2 >>= 1
        v5 = (v5+((v8 ^ v7) << v6)) & 0xffffffff
        v6 += 1
    return v5


def sub_4017A9(a1, a2):
    v5 = 0
    v6 = 0
    for i in range(32):
        v7 = a1 & 1
        v8 = a2 & 1
        a1 >>= 1
        a2 >>= 1
        v5 = (v5+((v8 & v7) << v6)) & 0xffffffff
        v6 += 1
    return v5


def sub_4016FE(a1, a2):
    v4 = 0
    v5 = 0
    while (a1):
        v4 = (v4+((a1 & 1) * (a2 << v5)) & 0xffffffff) & 0xffffffff
        a1 >>= 1
        v5 += 1
    return v4


a1 = BitVec(f'a1', 32)
a2 = BitVec(f'a2', 32)
a3 = BitVec(f'a3', 32)
a4 = BitVec(f'a4', 32)
a5 = BitVec(f'a5', 32)
a6 = BitVec(f'a6', 32)


v7 = sub_40163D(a1, (0-a2) & 0xffffffff)
v18 = sub_40163D(v7, a3) % 0x10AE961
v19 = sub_40163D(a1, a2) % 0x1093A1D
v8 = sub_4016FE(2, a2)
v9 = sub_4016FE(3, a1)
v10 = sub_40163D(v9, (0-v8) & 0xffffffff)
v20 = v10 % sub_40174A(a1, a4)
v11 = sub_40163D(a3, a1)
v21 = sub_4017A9(a2, v11) % 0x6E22
v22 = sub_40163D(a2, a4) % a1
v12 = sub_40163D(a4, a6)
v23 = sub_40174A(a3, v12) % 0x1CE628
v24 = sub_40163D(a5, (0-a6) & 0xffffffff) % 0x1172502
v25 = sub_40163D(a5, a6) % 0x2E16F83

solver.add(a1 > 0x5F5E100)
solver.add(a2 > 0x5F5E100)
solver.add(a3 > 0x5F5E100)
solver.add(a4 > 0x5F5E100)
solver.add(a5 > 0x5F5E100)
solver.add(a6 > 0x5F5E100)

solver.add(a1 <= 0x3B9AC9FF)
solver.add(a2 <= 0x3B9AC9FF)
solver.add(a3 <= 0x3B9AC9FF)
solver.add(a4 <= 0x3B9AC9FF)
solver.add(a5 <= 0x3B9AC9FF)
solver.add(a6 <= 0x3B9AC9FF)

solver.add(v18 == 0x3F29B9)
solver.add(v19 == 0x8BDCD2)
solver.add(v20 == 0x212C944D)
solver.add(v21 == 0x31BE)
solver.add(v22 == 0x2038C43C)
solver.add(v23 == 0x1386E2)
solver.add(v24 == 0x103CF4F)
solver.add(v25 == 0x16AB0D7)

if solver.check() == sat:
    model = solver.model()
    print("Solution found:")
    print(model)

else:
    print("No solution found")
# 705965527
# 780663452
# 341222189
# 465893239
# 966221407
# 217433792
