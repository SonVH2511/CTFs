## CTFs/Imaginary2024

- Haycuvotuvalacquanlenemoi, sau 2 giải rating 100, tới tuần này cũng được thở chút(nhưng vẫn pay 40k TxT). WU này mình sẽ bỏ các bài không thuần rev hoặc quá dễ(và tất nhiên là cả những bài mình chưa làm được-sẽ cố gắng cập nhật sau :v) đi. Giờ thì bắt đầu thôi^^.

- Note: tin vui là mình fix được git và push mọi thứ lên bình thường, tin xấu là mình pull nhánh hơi cũ và reset lại hết nên mất sạch file thực thi các chall và script rồi(mấy cái đường dẫn đến chall dưới kia côk hết), mọi thứ dưới đây là những gì còn sót lại. :((

### Watchdog

- Chall: [Watchdog](Watchdog/watchdog)

- Challenge giải toán thường thấy, cũng chẳng biết phải phân tích thêm gì ở bài này. Đơn giản chỉ là code lại cả chương trình rồi solve bằng `Z3`.

- Nếu có gì cần lưu ý thì..., ta phải set giá trị biến lên 64bit thay vì 8bit. Mình cũng không rõ tại sao, ở giải UIUctf trước mình cũng gặp một trường hợp tương tự và chỉ ra kết quả chuẩn xác nhất khi độ lớn của Bitvec được nâng lên.

- Tất nhiên để 8bit cũng không sai, nhưng nó sẽ đẻ ra 1tỉ trường hợp thỏa mãn, mọi người có thể thử bằng cách sửa script của mình để dưới :v

```python
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
```

```
flag: ictf{i_l0ve_interp0lati0n_2ca38d6ef0a709e0}
```

### Unconditional

- Chall: [Unconditional](Unconditional/chal)

- Không hiểu sao dạo này hơi nhiều bài `z3`, chúng chẳng có gì để giải thích đâu :)).

```python
from z3 import *

table1 = [0x52, 0x64, 0x71, 0x51, 0x54, 0x76]
table2 = [1, 3, 4, 2, 6, 5]
outp = [0xb4, 0x31, 0x8e, 0x02, 0xaf, 0x1c, 0x5d, 0x23, 0x98, 0x7d, 0xa3, 0x1e, 0xb0, 0x3c, 0xb3, 0xc4,
        0xa6, 0x06, 0x58, 0x28, 0x19, 0x7d, 0xa3, 0xc0, 0x85, 0x31, 0x68, 0x0a, 0xbc, 0x03, 0x5d, 0x3d, 0x0b]

solver = Solver()
flag = [BitVec(f'flag_{i}', 8) for i in range(33)]

for i in range(33):
    solver.add(Or(
        And(flag[i] >= ord('a'), flag[i] <= ord('z')),
        And(flag[i] >= ord('0'), flag[i] <= ord('9')),
        flag[i] == ord('_'),
        flag[i] == ord('{'),
        flag[i] == ord('}')
    ))

cnt1 = 0
cnt2 = 0
for i in range(33):
    v3 = flag[i]
    v4 = (i & 1) != 0
    v1 = And(v3 > ord('`'), v3 <= ord('z'))
    shifted_right = LShR(v3, table2[cnt2])
    shifted_left = (v3 << (8 - table2[cnt2])) & 0xFF
    cond1 = (If(v1, (shifted_right | shifted_left), 0) +
             If(Not(v1), ((v3 << 6) | LShR(v3, 2)) ^ table1[cnt1], 0)) & 0xFF
    cond2 = (If(v1, (v3 ^ table1[cnt1]), 0) +
             If(Not(v1), (4 * v3) | LShR(v3, 6), 0)) & 0xFF
    res = If((i & 1) == 0, cond1, cond2) & 0xFF
    solver.add(res == outp[i])
    cnt1 = (v4 + cnt1) % 6
    cnt2 = (v4 + cnt2) % 6

if solver.check() == sat:
    model = solver.model()
    flag_result = ''.join([chr(model[flag[i]].as_long()) for i in range(33)])
    print(flag_result)
else:
    print('No solution found')
```

```
flag: ictf{m0r3_than_1_way5_t0_c0n7r0l}
```

### Rust

- Chall: [rust](Rust/rust), [output.txt](Rust/output.txt)

- Nội dung của hàm `encryptor` đơn giản như này.

![alt text](image.png)

- Thứ duy nhất ta thiếu là key, nhưng lại biết format flag là `ictf{` nên dễ dàng xor ngược lại để lấy key.

```python
enc = [-42148619422891531582255418903, -42148619422891531582255418927, -42148619422891531582255418851, -42148619422891531582255418907, -42148619422891531582255418831, -42148619422891531582255418859, -42148619422891531582255418855, -42148619422891531582255419111, -42148619422891531582255419103, -42148619422891531582255418687, -42148619422891531582255418859, -42148619422891531582255419119, -42148619422891531582255418843, -42148619422891531582255418687, -42148619422891531582255419103, -42148619422891531582255418907, -42148619422891531582255419107, -42148619422891531582255418915, -42148619422891531582255419119, -42148619422891531582255418935, -42148619422891531582255418823]

key = 0x883085554737383682184979
res = []
for i in enc:
    tmp = (~i - 0x539) ^ key
    res.append((tmp << 3)//32)
for i in res:
    print(chr(i), end='')

```

```
flag: ictf{ru57_r3v_7f4d3a}
```

### SVM

- Chall: [Encryptor](SVM/svm_revenge), [flag-enc](SVM/root-output.bin)

- Bài này vẫn là `z3` thôi, tuy nhiên nó khác các bài trên rằng các công đoạn mã hóa của encryptor được thực hiện thông qua một kiểu dữ liệu đặc biệt.

- Chương trình thực hiện mã hóa từng byte một rồi trả ra file `output.bin` như dưới.

![alt text](image-2.png)

- Cụ thể hàm mã hóa, chương trình thực hiện chạy con VM với bộ truy vấn như dưới.

![alt text](image-3.png)

- VM

![alt text](image-4.png)

- Sau khi debug 1 lúc thì mình thấy dữ liệu được lưu trữ ở dạng dslk, với các Node được nối với nhau thông qua địa chỉ của node liền sau. Tiếp tới là test chức năng của các hàm rồi rename lại.

- Quan sát mảng truy vấn ta có thể dump ra dưới đây.

![alt text](image-1.png)

- Khúc đầu truy vấn 4 là nó nhặt ra 16ptu rồi truyền vào `Flag<>`.

- Sau đấy là xen kẽ truy vấn 2,5 lần lượt là push `Flag[val]` với `val` vào đuôi.

- Truy vấn 1 là thêm tích của từng cặp 1 vào.

- Ví dụ cặp đầu tiên là `0x02, 0x01, 0x05, 0xAA, 0x02, 0x02, 0x05, 0xED` thì mình có cái dslk:

![alt text](image-5.png)

- 2 4 5 là khởi tạo, 1 3 là xử lý nhân, cộng rồi đều thêm vào đuôi.

- Tới đây thì chỉ cần viết script z3 để giải thôi, tuy nhiên mình đã có chút sai sót mà sau khi được anh Sơn giải thích mới phát hiện ra.

- Kiểu dữ liệu mà chương trình xây dựng thủ công không đơn thuần là dslk, nó là 1 cái `queue` được lưu trữ dưới dạng dslk :v.

- Vì hiểu lầm này nên mình không mô phỏng lại hàm `getFirstNode` được và stuck trong việc dựng lại chương trình. Khi mọi thứ rõ ràng rồi thì công đoạn cuối cũng không còn gì.

```
flag: ictf{S_d1dnt_5t4nd_f0r_5t4ck_b3c4u53_h3r3_I_us3d_4_L1nk3d_qu3u3}
```

### FlagChecker

## Mong WRITEUP này giúp ích cho các bạn!

```
from KMA
Author: 13r_ə_Rɪst
```
