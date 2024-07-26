
from z3 import *


def my_pow(a1, a2):
    if a2 == 0:
        return 1

    if (a2 == 1):
        return a1
    if ((a2 & 1) != 0):
        return a1 * my_pow((a1 * a1) & 0xffffffffffffffff, ((a2 - 1) >> 1) & 0xffffffffffffffff)
    return my_pow((a1 * a1) & 0xffffffffffffffff, (a2 >> 1) & 0xffffffffffffffff)


solver = Solver()
x = [BitVec(f'x[{i}]', 64) for i in range(44)]
for i in range(43):
    solver.add(x[i] >= 48)
    solver.add(x[i] <= 126)


ans = [0x348A627D10659, 0x27485A840365FE61, 0x9E735DADF26D31CD, 0x82714BC9F9B579D9, 0x3DFB7CC801D16BC9, 0x602A04EFE5DAD659, 0x0EB801D915A30D3D, 0x217DBE10EDCB20A1, 0x0ADEE2637E875CA19, 0x0CD44AED238E9871, 0x0D3BFF76AE6B504D, 0x7181426EFF59E789, 0x477616CB20C2DAC9, 0x0CE1206E1E46CE4A9, 0x946E7CB964A3F87D, 0x499607CBF0C3291, 0x6871D4372347C759, 0x75412F56B7D8B01, 0x0F8E57C264786E34D, 0x194CA6020EC505B9, 0x3E1A22E34FE84949, 0x0A46DE25172742B79,
       0x0CD0E971BCBFE6E3D, 0x56561961138A2501, 0x78D2B538AB53CA19, 0x0A9980CA75AB6D611, 0x5F81576B5D4716CD, 0x17B9860825B93469, 0x0C012F75269298349, 0x17373EE9C7A3AAC9, 0x0B2E50798B11E1A7D, 0x0ADA5A6562E0FD7F1, 0x0EC3D9A68F1C99E59, 0x3D828B35505D79A1, 0x0F76E5264F7BD16CD, 0x0DD230B3EC48ED399, 0x80D93363DCD354C9, 0x7031567681E76299, 0x8977338CD4E2A93D, 0x8A5708A1D4C02B61, 0x2066296A21501019, 0x9E260D94A4D775B1, 0x0E7667BBD72280F4D, 0x12DF4035E1684349]
# print(len(ans))
# print("ictf{"+"x"*(43-5))
solver.add(x[0] == 105)
solver.add(x[1] == 99)
solver.add(x[2] == 116)
solver.add(x[3] == 102)
solver.add(x[4] == 123)
solver.add(x[43] == 125)

cnt = 0
for i in range(2, 43+3):
    v4 = 42
    out = 0
    while (v4 >= 0):
        v5 = 43-v4-1
        # v2 = x[v5]
        out = (out + (x[v5]*my_pow(i, v4)) &
               0xffffffffffffffff) & 0xffffffffffffffff
        v4 -= 1
    solver.add(out == ans[cnt])
    cnt += 1
all_solutions = []
while solver.check() == sat:
    model = solver.model()
    solution = [model[x[i]].as_long() for i in range(43)]
    for i in solution:
        print(chr(i), end="")
    print()
    all_solutions.append(solution)
    print(all_solutions)
    block = []
    for i in range(43):
        block.append(x[i] != solution[i])
    solver.add(Or(block))
