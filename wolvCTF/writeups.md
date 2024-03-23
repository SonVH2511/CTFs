## CTFs/WolvCTF

### rev_BabyRE

- Chall warmup nên cũng không cần nghĩ nhiều, `f12` thôi^^.

![alt text](_IMG/image.png)

```
flag: wctf{n1c3_oNe_y0u_Found_m3}
```

### rev_Shredded

- Chall yêu cầu ta giải mã đoạn code `shredded.c` để lấy được chương trình `checkflag`. Vấn đề duy nhất ở đây là các file `shred{*}.txt` bị shuffle nên cần trace lại. Đây là script của mình.

```python
shuffledLine = [2, 4, 18, 31, 19, 21, 13, 5, 12, 30, 27, 28, 25, 9,
                16, 6, 26, 24, 17, 29, 11, 14, 1, 3, 15, 7, 32, 0, 20, 23, 10, 8, 22]
lines = []
code_C = ["" for _ in range(40)]*35

for i in shuffledLine:
    with open("shred{i}.txt", 'r') as file:
        tmp = file.read()
        lines.append(tmp.rstrip())

for line in lines:
    for i in range(len(line)):
        if line[i] != '\n':
            code_C[i] += line[i]

for i in code_C:
    print(i)
```

![alt text](_IMG/image-1.png)

- Mở file `code.c` mới được truyền dữ liệu vào, ta có đoạn chương trình sau.

```C
#include <stdio.h>
#include <string.h>
int main()
{
    char flag[] = "REDACTED";
    char inter[51];
    int len = strlen(flag);
    for (int i = 0; i < len; i++)
    {
        inter[i] = flag[i];
    }
    for (int i = len; i < 50; i++)
    {
        inter[i] = inter[(i * 2) % len];
    }
    inter[50] = '\0';
    char a;
    for (int i = 0; i < 50; i++)
    {
        a = inter[i];
        inter[i] = inter[((i + 7) * 15) % 50];
        inter[((i + 7) * 15) % 50] = a;
    }
    for (int i = 0; i < 50; i++)
    {
        a = inter[i];
        inter[i] = inter[((i + 3) * 7) % 50];
        inter[((i + 3) * 7) % 50] = a;
    }
    for (int i = 0; i < 50; i++)
    {
        inter[i] = inter[i] ^ 0x20;
        inter[i] = inter[i] ^ 0x5;
    }
    for (int i = 0; i < 50; i++)
    {
        a = inter[i];
        inter[i] = inter[((i + 83) * 12) % 50];
        inter[((i + 83) * 12) % 50] = a;
    }
    for (int i = 0; i < 50; i++)
    {
        printf("\\x%X", inter[i]);
    }
    return 0;
}
```

- Vì viết script ngược lại ra data rác, mình cần viết script có hướng tiếp cận khác, mình sẽ viết xuôi các lần shuffle rồi map lại các vị trí của 50 kí tự sau khi thay đổi, và xếp ngược lại vị trí bạn đầu.(cũng không hiểu sao viết ngược lại không đúng nữa vì chỉ toàn `swap` thôi mà nhỉ@@).

```python
inter = [0x14, 0x5D, 0x14, 0x57, 0x16, 0x43, 0x46, 0x7A, 0x56, 0x16, 0x57, 0x17, 0x4B, 0x16, 0x52, 0x4C, 0x61, 0x1C, 0x1C, 0x7A, 0x1D, 0x7A, 0x11, 0x51, 0x52,
         0x16, 0x5E, 0x62, 0x6D, 0x5E, 0x61, 0x7A, 0x16, 0x17, 0x61, 0x16, 0x6B, 0x61, 0x4E, 0x69, 0x14, 0x6B, 0x6D, 0x51, 0x57, 0x6D, 0x6D, 0x58, 0x5D, 0x4B]
flag = ""

shuffledPos = [i for i in range(0, 50)] # mảng này sẽ cho biết vị trí ban đầu của các giá trị sau khi shuffle

for i in range(len(inter)):
    a = shuffledPos[i]
    shuffledPos[i] = shuffledPos[((i + 7) * 15) % 50]
    shuffledPos[((i + 7) * 15) % 50] = a

for i in range(len(inter)):
    inter[i] = inter[i] ^ 0x5 ^ 0x20

for i in range(len(inter)):
    a = shuffledPos[i]
    shuffledPos[i] = shuffledPos[((i + 3) * 7) % 50]
    shuffledPos[((i + 3) * 7) % 50] = a

for i in range(len(inter)):
    a = shuffledPos[i]
    shuffledPos[i] = shuffledPos[((i + 83) * 12) % 50]
    shuffledPos[((i + 83) * 12) % 50] = a

# print(shuffledPos) # in ra để biết thêm chi tiết^^

for j in range(50):
    for i in range(len(shuffledPos)):
        if shuffledPos[i] == j:
            flag += chr(inter[i])

print(flag)
```

```
flag: wctf{sHr3DDinG_L1k3_H3NDr1x_93284}
```

### rev_Doubledelete's revenge

- Chương trình cấp cho ta file thực thi mã hóa `reveng1` và flag đã bị mã hóa `flag.txt.enc`.

- Một phép toán duy nhất được sử dụng là `__ROL4__`, xoay trái với tham số truyền vào mặc định là 13.

![alt text](_IMG/image-2.png)

- Đọc data từ `encrypted_flag`, có độ dài 48 gấp 4 lần số lần lặp là 12. Check lại mã máy, giá trị được rol nằm trong `eax`~4 byte.

![alt text](_IMG/image-3.png)

- Chương trình `rol` 13 đơn vị cặp 4 kí tự một rồi trả về từng byte, vậy ta sẽ ghép lại 4 byte một và `ror` 13 đơn vị để đảo ngược lại.

```python
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
```

```
flag: wctf{i_th1nk_y0u_m1sund3rst00d_h0w_r0t13_w0rk5}
```

### rev_Assembled

- Đây là lần đầu mình gặp chall trình bày như này^^. kiểu biểu diễn luồng chương trình khá lạ nhưng cũng không phức tạp.

- Những thứ cần nhặt ra ở đây là mảng `data`, `seed` = 0x3148, và mảng `key[256]`.

- Một chút phân tích chương trình, hàm kiểm tra gồm 24 lần lặp, mỗi lần sẽ thực hiện biến đổi `seed`(trong `eax`) với giá trị khởi tạo luôn quan sát được là 0x3148.

![alt text](_IMG/image-4.png)

- Giá trị này sau khi được xử lý qua vài phép toán như trên sẽ dùng để lấy giá trị trong một dải data khác rồi xor với flag nên mình viết một đoạn script để nhặt các giá trị này ra luôn.

```python
seed = 0x003148

for i in range(len(data)):
    if seed % 2 == 0:
        seed >>= 1
    else:
        tmp = seed
        seed <<= 1
        seed += tmp
        seed += 1
    print(hex(seed))
```

- Thu được chuỗi sau:

```python
final_key = [0x3148, 0x18a4, 0xc52, 0x629, 0x127c, 0x93e, 0x49f,  0xdde, 0x6ef, 0x14ce, 0xa67, 0x1f36,
             0xf9b, 0x2ed2, 0x1769, 0x463c, 0x231e, 0x118f, 0x34ae, 0x1a57, 0x4f06, 0x2783, 0x768a, 0x3b45, 0xb1d0]
```

- Tiếp đó, chương trình lấy ra giá trị tại rsp[al=final_key], cùng với kí tự trong input flag và `xor`, rồi kiểm tra với giá trị tương ứng trong mảng `data`.

![alt text](_IMG/image-5.png)

- Vậy ta chỉ cần `xor` ngược lại là lấy được flag. Nhớ là phải lấy byte thấp của `final_key` trước khi truy cập vào key để lấy giá trị ra `xor`^^.

```python
data = [0xF2, 0x0F, 0x6C, 0xEC, 0x1A, 0xE2, 0x57, 0x70, 0x70, 0x86,
        0xEA, 0xBA, 0xB5, 0x63, 0xCF, 0x8C, 0xF8, 0x0B, 0x6C, 0xE0,
        0x6E, 0x15, 0x53, 0x45]

key = [0x49, 0x89, 0xC6, 0x41, 0xB8, 0x00, 0x00, 0x00, 0x00, 0xB8,
       0x00, 0x00, 0x00, 0x00, 0x48, 0x8D, 0x1C, 0x25, 0x0E, 0x11,
       0x40, 0x00, 0x66, 0xB8, 0x48, 0x31, 0xF9, 0xFF, 0xE3, 0x41,
       0x88, 0xC1, 0x4D, 0x0F, 0xB6, 0xC9, 0x42, 0x8A, 0x0C, 0x0C,
       0x43, 0x8A, 0x3C, 0x10, 0x48, 0x8D, 0x1D, 0x0A, 0x00, 0x00,
       0x00, 0x4C, 0x8D, 0x0D, 0xDE, 0xFF, 0xFF, 0xFF, 0x41, 0xFF,
       0xE1, 0x41, 0x8A, 0xB8, 0x83, 0x11, 0x40, 0x00, 0x40, 0x38,
       0xF9, 0x0F, 0x85, 0x41, 0xFF, 0xFF, 0xFF, 0x66, 0xA9, 0x01,
       0x00, 0x74, 0x18, 0x66, 0x89, 0xC3, 0x66, 0xD1, 0xE0, 0x66,
       0x01, 0xD8, 0x66, 0xFF, 0xC0, 0x49, 0xFF, 0xC0, 0x49, 0x83,
       0xF8, 0x18, 0x7C, 0xB5, 0x41, 0xFF, 0xE6, 0x66, 0xD1, 0xE8,
       0x49, 0xFF, 0xC0, 0x49, 0x83, 0xF8, 0x18, 0x7C, 0xA6, 0x41,
       0xFF, 0xE6, 0x66, 0x6C, 0x61, 0x67, 0x3F, 0x20, 0x63, 0x6F,
       0x72, 0x72, 0x65, 0x63, 0x74, 0x21, 0x0A, 0x77, 0x72, 0x6F,
       0x6E, 0x67, 0x20, 0x3A, 0x28, 0x0A, 0xF2, 0x0F, 0x6C, 0xEC,
       0x1A, 0xE2, 0x57, 0x70, 0x70, 0x86, 0xEA, 0xBA, 0xB5, 0x63,
       0xCF, 0x8C, 0xF8, 0x0B, 0x6C, 0xE0, 0x6E, 0x15, 0x53, 0x45,
       0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
       0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
       0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01,
       0x00, 0x00, 0x00, 0x04, 0x00, 0xF1, 0xFF, 0x00, 0x00, 0x00,
       0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
       0x00, 0x00, 0x00, 0x0A, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01,
       0x00, 0x5D, 0x10, 0x40, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
       0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x20, 0x00, 0x00,
       0x00, 0x00, 0x00, 0x01, 0x00, 0x5F]

final_key = [0x3148, 0x18a4, 0xc52, 0x629, 0x127c, 0x93e, 0x49f,  0xdde, 0x6ef, 0x14ce, 0xa67, 0x1f36,
             0xf9b, 0x2ed2, 0x1769, 0x463c, 0x231e, 0x118f, 0x34ae, 0x1a57, 0x4f06, 0x2783, 0x768a, 0x3b45, 0xb1d0]

flag = ""

for i in range(len(data)):
    flag += chr(key[final_key[i] & 0xff] ^ data[i])
print(flag)
```

```
flag: wctf{h4ppy_d3c0mp1l1ng!}
```

### rev_Missing_resources

- Chall này có tên `Missing resources` có lẽ bởi việc cung cấp thiếu tài nguyên để thực thi chương trình, cài đặt các dll thiếu tại [đây](Missing_resources/CD/).

![alt text](_IMG/image-7.png)

- Sau khi hoàn thành cài đặt và tiến hành debug động, thì dưới đây là vị trí duy nhất ta phải `patch` để bypass và nhảy vào hàm xử lý.

![alt text](_IMG/image-8.png)

- Sau đó là một loạt các lượt `xor` của dải data `v11`.

![alt text](_IMG/image-9.png)

- Cuối cùng là kết quả của phép `xor` trên.

![alt text](_IMG/image-6.png)

```
flag: wctf{ch@mp1on-d11-sn1ff3r}
```

### rev_Game_graphics_debugging

- Hơi khó hiểu Chall này còn cùi hơn cả mấy bài warmup nữa @@. Ta được cấp một file thực thi. Khi chạy nó ta thu được chút thông tin rằng có sự xuất hiện của các string như `The flag is somewhere inside me...` hay `ooh spinny` sẽ xuất hiện trong chương trình. Đó cũng là hướng tiếp cận Chall này của mình.

![alt text](_IMG/image-12.png)

- Chương trình khá đồ sộ và đồng thời không có `input` và `output`, sẽ rất khó để giải quyết theo cách thông thường, thay vào đó mình sẽ trace theo string được cấp ở phần giao diện quan sát được.

![alt text](_IMG/image-11.png)

- Thấy được một string quen thuộc trong `f12` ta xref theo tới một hàm xử lý.

![alt text](_IMG/image-10.png)

- Quan sát từng hàm một, mình thấy có một đoạn xor liên tục như bài `Missing resources` trên nên thực hiện debug động và nhặt data ra.

![alt text](_IMG/image-14.png)

![alt text](_IMG/image-13.png)

- Hơi bất ngờ vì dễ(--\*).

![alt text](_IMG/image-15.png)

```
flag: wctf{your-d3sc3nt-into-gamedev-beg1ns}
```

### rev_Befudged_up

- Chall này cấp cho ta một file gồm các tổ hợp lệnh truy vấn `prog.befunge` và hai file python xử lý input và thực thi theo tổ hợp truy vấn.

  ![alt text](_IMG/image-16.png)

- Khi mình thử in ra các giá trị trong từng truy vấn, mình nhận thấy một điểm khá đáng chú ý. Rằng ở `case 'g'`, tùy thuộc vào độ chính xác của `flag` mà lượng output sẽ có độ chênh lệch. Nói một chút về `case 'g'`, truy vấn này thực hiện đẩy giá trị tại `GRIG[x][y]` vào `stack` để thực thi chương trình hoặc tương tự, mọi người có thể in ra GRID sau khi được khởi tạo thì sẽ rõ thứ được push vào `stack` là gì, chúng hoàn toàn là nội dung file truy vấn `prog.befunge` ta được cấp, phân thành mảng từng dòng một. Mình có suy đoán rằng đây là một trong các truy vấn điều khiển luồng chương trình nên in ra giá trị của nó xem thử.

  ![alt text](_IMG/image-17.png)

- Cụ thể, với input là `wctf{`, độ dài của output là 899 nói cách khác là số lần thực thi truy vấn `g` `case 'g':` là 899 lần.

![alt text](_IMG/image-18.png)

- Tuy nhiên, với input là `wctf*` với \* là bất kì kí tự khác. Số lượng thực thi có vẻ khác, tuy nhiên không có độ xê dịch lớn.

![alt text](_IMG/image-19.png)

![alt text](_IMG/image-20.png)

- Từ manh mối này mình thử thay đổi cách lấy input để quét qua dải kí tự xem suy đoán của bản thân có đúng không. Bằng cách đặt biến đếm trong đoạn xử lý của truy vấn `g` và thay đổi chương trình một chút để nhận input từ mảng được khởi tạo thay vì `stdin` ở truy vấn `~`, mn có thể quan sát ở dưới.

```python
from befunge import read_in, befunge

prog = read_in('prog.befunge')
print('flag? ')

flag_comp = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=<>,.?/{}[]\|~:;"\''
flag = ['w', 'c', 't', 'f', '{', '', '', '', '', '', '', '', '',]
i = 5

for j in flag_comp:
    flag[i] = j
    ret = befunge(prog, flag)
    print(ret)
```

```python
def befunge(GRID, flag):
    ret = 0
    i = -1
    PC = [0, 0]
    DIR = 0
    DIR_DELTAS = [0, 1, 0, -1, 0]
    STACK = []
    STRINGMODE = False

    MAXITER = 2**20

    for _ in range(MAXITER):
        try:
            ch = GRID[PC[0]][PC[1]]
            if STRINGMODE:
                if ch == '"':
                    STRINGMODE = False
                else:
                    STACK.append(ord(ch))
            else:
                match ch:
                    case '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9':
                        STACK.append(int(ch))
                    case '+':
                        a = STACK.pop()
                        b = STACK.pop()
                        STACK.append(a+b)
                    case '-':
                        a = STACK.pop()
                        b = STACK.pop()
                        STACK.append(b-a)
                    case '*':
                        a = STACK.pop()
                        b = STACK.pop()
                        STACK.append(a*b)
                    case '/':
                        a = STACK.pop()
                        b = STACK.pop()
                        STACK.append(b//a)
                    case '%':
                        a = STACK.pop()
                        b = STACK.pop()
                        STACK.append(b % a)
                    case '!':
                        a = STACK.pop()
                        if a == 0:
                            STACK.append(1)
                        else:
                            STACK.append(0)
                    case '`':
                        a = STACK.pop()
                        b = STACK.pop()
                        if b > a:
                            STACK.append(1)
                        else:
                            STACK.append(0)
                    case '>' | '^' | '<' | 'v':
                        DIR = '>v<^'.index(ch)
                    case '_':
                        a = STACK.pop()
                        if a == 0:
                            DIR = 0
                        else:
                            DIR = 2
                    case '|':
                        a = STACK.pop()
                        if a == 0:
                            DIR = 1
                        else:
                            DIR = 3
                    case '"':
                        STRINGMODE = True
                    case ':':
                        STACK.append(STACK[-1])
                    case '\\':
                        STACK[-2], STACK[-1] = STACK[-1], STACK[-2]
                    case '$':
                        STACK.pop()
                    case '.':
                        print(STACK.pop(), end=' ')
                    case ',':
                        print(chr(STACK.pop()), end='')
                    case '#':
                        PC[0] += DIR_DELTAS[DIR]
                        PC[1] += DIR_DELTAS[DIR + 1]
                    case 'p':
                        y = STACK.pop()
                        x = STACK.pop()
                        v = STACK.pop()
                        GRID[y][x] = chr(v)
                    case 'g':
                        y = STACK.pop()
                        x = STACK.pop()
                        STACK.append(ord(GRID[y][x]))
                        ret += 1
                        # print((GRID[y][x]))  # test
                    case '~':
                        i += 1
                        x = flag[i]
                        # x = sys.stdin.read(1)
                        STACK.append(ord(x))
                    case '@':
                        break
                    case ' ':
                        pass
                    case _:
                        print(f'Error: unknown character "{ch}"')
                        break
                # end match
            PC[0] += DIR_DELTAS[DIR]
            PC[1] += DIR_DELTAS[DIR + 1]
        except Exception as e:
            print('oh no', e, PC)
            break
    return ret
```

- Đầu ra thể hiện như dự đoán, một kí tự chính xác sẽ có gọi tới truy vấn `g`. Nói cách khác, chương trình có vẻ là sẽ check từng kí tự một và dừng ngay khi xuất hiện kí tự không đúng. Hay nếu xuất hiện kí tự chuẩn, lượng `ret` sẽ lớn hơn trung bình, cụ thể ở đây là kí tự thứ 16 trong chuỗi `flag_comp`~`p`^^.

![alt text](_IMG/image-21.png)

- Từ ý tưởng này, mình viết một script để vét cạn như sau. Chặn đuôi bằng kí tự `}` và duyệt.

```python
from befunge import read_in, befunge

prog = read_in('prog.befunge')
print('flag? ')
flag = ['w', 'c', 't', 'f', '{', 'p', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
        '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

i = 6
default_len = 926
flag_comp = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=<>,./{}[]\|~:;?"\''
while flag[i-1] != '}':
    for j in flag_comp:
        flag[i] = j
        ret = befunge(prog, flag)
        if j == 'a':
            default_len = ret
        elif ret >= (default_len+50):
            i += 1
            for f in flag:
                print(f, end='')
            # print(flag)
            break

for j in flag_comp:
    flag[i] = j
    ret = befunge(prog, flag)
    print(ret)
```

![alt text](_IMG/image-22.png)

- Các bạn tham khảo source của mình tại đây: [befunge.py](Befudged_up/befunge.py), [runner.py](Befudged_up/runner.py),

- Note: Các bạn chỉnh script trên cho đoạn flag_comp có một kí tự không xuất hiện nhiều lên đầu bởi nếu chữ `a` có xuất hiện trong flag thì chương trình này sẽ lỗi bởi thiếu lệnh check pre-char, cũng may mà flag không gồm kí tự `a`^^.

```
flag: wctf{pr30ccup13d_w1+h_wh3+h3r_0r_n0t_1_c0uld}
```

### rev_Maize

- Chall này mình thấy khi được gợi ý rằng ma trận hình hộp thì không còn khó lắm. Trước tiên mình giải thích về cách mà chương trình này hoạt động.

- Đầu tiên chương trình yêu cầu nhập flag, và check format `wctf{}`. Nội dung flag sẽ được mang đi xor với đống `const` có sẵn.

  ![alt text](_IMG/image-23.png)

- Tiếp đến, phần nội dung của flag được xử lý tạo thành các truy vấn thực hiện quá trình di chuyển trong `maze`, cho tới khi đạt được điều kiện `des_pos == 0x260000005ALL && step_cnt == 223`, tức là vị trí hiện tại trùng với vị trí `{0x5a, 0x26}`, và có số bước di chuyển tối đa là 223.

![alt text](_IMG/image-24.png)

- Đó là sơ bộ nội dung chương trình, đi vào phân tích sâu hơn. Trước tiên, khi quan sát ma trận được cấp, ta thấy một vị trí được đánh dấu `*` duy nhất chính là điểm xuất phát, ta có thể thấy rõ hơn khi debug động nếu xem biến `des_pos` trước khi chương trình thực hiện xử lí các bước nhảy. Vị trí xuất phát nằm ở ô `{0x27, 0x26}`.(lưu ý rằng tọa độ trong WU sẽ viết ngược lại so với Chall vì mình quen xử lý giá trị [x][y] hơn là [y][x] ^^).

  ![alt text](_IMG/image-27.png)
  ![alt text](_IMG/image-25.png)

- Tiếp tới là nội dung flag, một mẩu flag được sử dụng 4 lần với một phép toán để tách thành giá trị 0,1,2,3 tương ứng với 4 phương thức di chuyển xuống, lên, trái, phải. Mọi người có thể thấy được phương hướng di chuyển của chương trình trong quá trình debug bằng cách vét tham số đầu vào với phép toán có sẵn ở trên.

  ![alt text](_IMG/image-26.png)

- Giờ mình sẽ phân tích cách di chuyển của chương trình. Mình thử nhập giá trị đầu vào là kí tự `C` để cho ra bước di đầu tiên là sang phải bởi dễ dàng quan sát tại ma trận được cấp sẵn rằng đó là nước đi hợp lệ duy nhất.

```python
flag_comp = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=<>,./{}[]\|~:;?"\''
for i in flag_comp:
    a = ord(i) ^ 48
    if ((a >> (2 * 0)) & 3) == 3:
        print(i) # CHỌN bừa 1 kí tự nằm trong đây để thử
```

- Với nước đi đầu tiên là sang phải, mình dự tính sau khi xử lý, `des_pos` sẽ bằng `{0x27, 0x27}` và `step_cnt = 1`, tức là dịch phải 1 đơn vị và số nước đi tối ưu bằng 1. Tuy nhiên kết quả đầu ra lại khác với mong đợi:

  ![alt text](_IMG/image-28.png)

- `des_pos` sau khi xử lý lại là `{0x27,0x28}`, tức là đi được thêm một bước so với dự đoán, số nước di chuyển cũng được ghi lại đầy đủ là 2.

  ![alt text](_IMG/image-29.png)

- Ảnh mình đánh dấu 1, 2 dưới đây là các bước di chuyển được trong lần truy vấn đầu tiên. Tới đây, mình suy đoán rằng có thể chương trình sẽ di chuyển tới đoạn rẽ và đánh dấu liên tục, kiểm chứng bằng cách cho chạy tiếp các nước di chuyển tiếp theo của kí tự `C` ~ `3, 0, 3, 1`.

![alt text](_IMG/image-30.png)

- Ta thu được các vị trí sau 4 lần xủ lí của kí tự `C` như dưới.

```
2800000027h -> {0x27,0x28}
280000002Ah -> {0x2A,0x28}
2C0000002Ah -> {0x2A,0x2C}
2C00000029h -> {0x29,0x2C}
```

- Chúng tương ứng với các vị trí mình đánh dấu `X` trong ảnh.

  ![alt text](_IMG/image-31.png)

- Vậy nhận định ở trên là đúng, đó là về mặt phân tích. Nếu quan sát kĩ hơn thì ngay trong chương trình có hàm kiểm tra rồi đệ quy để duyệt tới vị trí cuối của nút rẽ.

  ![alt text](_IMG/image-32.png)

- Viết ![chương trình](rev_Maize/sc.cpp) duyệt BFS loang đánh dấu nhặt ra bộ 4 lần rẽ một để ghép lại thành bộ để vét cạn kí tự xem có xuất hiện các cụm có nghĩa không.

![alt text](_IMG/image-36.png)

- `output` chương trình tương tự đường đi của ảnh tham khảo bên trên.

```python
m1 = [[3, 0, 3, 1],
      [3, 0, 3, 3],
      [3, 1, 2, 1],
      [3, 3, 1, 3],
      [3, 0, 0, 2],
      [0, 0, 2, 2],
      [2, 0, 2, 2]]
xor_key = [48, 134, 5, 236, 220, 149, 210, 101, 77,
           220, 111, 68, 23, 186, 105, 81, 156, 66, 48, 0]
cnt = 0
for move in m1:
    print(move, end="")
    flag_comp = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=<>,./{[]\|~:;?"\''
    for i in flag_comp:
        tmp = ord(i) ^ xor_key[cnt]
        for j in range(0, 4, 1):
            a = ((tmp >> (2 * j)) & 3)
            if a != move[j]:
                break
            elif j == 3:
                cnt += 1
                print(i)
                break
```

![alt text](_IMG/image-33.png)

- Trông rõ ràng là ta đang đi đúng hướng^^.

- Vấn đề cuối cùng là làm sao chuyển mặt `maze` đây? Cái này thì ta nhặt hàm này gắn vào chương trình duyệt của mình là được.

  ![alt text](_IMG/image-34.png)

- Nhưng tới đây vẫn chưa xong@@. Các mặt của maze có trình tự đọc không giống nhau, cụ thể hơn là trong mặt phẳng thì không được. Giống như một khối rubik khi giải mặt nào thì cần nhìn trực diện mặt đó vậy, công thức di chuyển ở trên được áp dụng cho mặt xuất phát. Lật sang mặt thứ 2, quy tắc không có thay đổi bởi vẫn cùng chiều, mặt thứ 2 sang 3 phải xoay 90 độ, mặt thứ 3 sang 4 lật có công thức di chuyển ngược lại so với tương quan của mặt đầu và mặt cuối cùng đối xứng với mặt xuất phát nên vẫn giữ quy tắc đầu tiên. Khá khó mô tả bằng lời nhưng sẽ dễ nhận ra trong quá trình debug thôi!

- Xoay một hồi mình có script^^.

```python
# không phải mình không muốn viết ngắn đâu nma tích hợp lại thành các vòng lặp lồng nhau nó cứ bị lỗi ak @@.
m1 = [[3, 0, 3, 1],
      [3, 0, 3, 3],
      [3, 1, 2, 1],
      [3, 3, 1, 3],
      [3, 0, 0, 2],
      [0, 0, 2, 2],
      [2, 0, 2, 2],
      [0, 0, 3, 0],
      [3, 0, 2, 0],
      [3, 0, 0, 2],
      [1, 2, 0, 0],
      [3, 0, 3, 1],
      [3, 0, 2, 0],
      [0, 3, 0, 2],
      [0, 2, 0, 0],
      [3, 1, 2, 1],
      [3, 3, 3, 3],
      [3, 1, 3, 1],
      [3, 0, 0, 0],
      [2, 1, 3, 0]]

xor_key = [48, 134, 5, 236, 220, 149, 210, 101, 77,
           220, 111, 68, 23, 186, 105, 81, 156, 66, 48, 0]
flag_comp = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=<>,./{}[]\|~:;?"\''
flag = ""

for i in flag_comp:
    a = ord(i) ^ 48
    if ((a >> (2 * 0)) & 3) == 3 and ((a >> (2 * 1)) & 3) == 0 and ((a >> (2 * 2)) & 3) == 3 and ((a >> (2 * 3)) & 3) == 1:
        flag += i
for i in flag_comp:
    a = ord(i) ^ 134
    if ((a >> (2 * 0)) & 3) == 3 and ((a >> (2 * 1)) & 3) == 0 and ((a >> (2 * 2)) & 3) == 3 and ((a >> (2 * 3)) & 3) == 3:
        flag += i
for i in flag_comp:
    a = ord(i) ^ 5
    if ((a >> (2 * 0)) & 3) == 3 and ((a >> (2 * 1)) & 3) == 1 and ((a >> (2 * 2)) & 3) == 2 and ((a >> (2 * 3)) & 3) == 1:
        flag += i
for i in flag_comp:
    a = ord(i) ^ 236
    if ((a >> (2 * 0)) & 3) == 3 and ((a >> (2 * 1)) & 3) == 3 and ((a >> (2 * 2)) & 3) == 1 and ((a >> (2 * 3)) & 3) == 3:
        flag += i
for i in flag_comp:
    a = ord(i) ^ 220
    if ((a >> (2 * 0)) & 3) == 3 and ((a >> (2 * 1)) & 3) == 0 and ((a >> (2 * 2)) & 3) == 0 and ((a >> (2 * 3)) & 3) == 2:
        flag += i
for i in flag_comp:
    a = ord(i) ^ 149
    if ((a >> (2 * 0)) & 3) == 0 and ((a >> (2 * 1)) & 3) == 0 and ((a >> (2 * 2)) & 3) == 2 and ((a >> (2 * 3)) & 3) == 2:
        flag += i
for i in flag_comp:
    a = ord(i) ^ 210
    if ((a >> (2 * 0)) & 3) == 2 and ((a >> (2 * 1)) & 3) == 0 and ((a >> (2 * 2)) & 3) == 2 and ((a >> (2 * 3)) & 3) == 2:
        flag += i
for i in flag_comp:
    a = ord(i) ^ 101
    if ((a >> (2 * 0)) & 3) == 0 and ((a >> (2 * 1)) & 3) == 0 and ((a >> (2 * 2)) & 3) == 3 and ((a >> (2 * 3)) & 3) == 0:
        flag += i
for i in flag_comp:
    a = ord(i) ^ 77
    if ((a >> (2 * 0)) & 3) == 3 and ((a >> (2 * 1)) & 3) == 0 and ((a >> (2 * 2)) & 3) == 2 and ((a >> (2 * 3)) & 3) == 0:
        flag += i
for i in flag_comp:
    a = ord(i) ^ 220
    if ((a >> (2 * 0)) & 3) == 3 and ((a >> (2 * 1)) & 3) == 0 and ((a >> (2 * 2)) & 3) == 0 and ((a >> (2 * 3)) & 3) == 2:
        flag += i
for i in flag_comp:
    a = ord(i) ^ 111
    if ((a >> (2 * 0)) & 3) == 1 and ((a >> (2 * 1)) & 3) == 2 and ((a >> (2 * 2)) & 3) == 0 and ((a >> (2 * 3)) & 3) == 0:
        flag += i
for i in flag_comp:
    a = ord(i) ^ 68
    if ((a >> (2 * 0)) & 3) == 3 and ((a >> (2 * 1)) & 3) == 0 and ((a >> (2 * 2)) & 3) == 3 and ((a >> (2 * 3)) & 3) == 1:
        flag += i
for i in flag_comp:
    a = ord(i) ^ 23
    if ((a >> (2 * 0)) & 3) == 3 and ((a >> (2 * 1)) & 3) == 0 and ((a >> (2 * 2)) & 3) == 2 and ((a >> (2 * 3)) & 3) == 0:
        flag += i
for i in flag_comp:
    a = ord(i) ^ 186
    if ((a >> (2 * 0)) & 3) == 0 and ((a >> (2 * 1)) & 3) == 3 and ((a >> (2 * 2)) & 3) == 0 and ((a >> (2 * 3)) & 3) == 2:
        flag += i
for i in flag_comp:
    a = ord(i) ^ 105
    if ((a >> (2 * 0)) & 3) == 0 and ((a >> (2 * 1)) & 3) == 2 and ((a >> (2 * 2)) & 3) == 0 and ((a >> (2 * 3)) & 3) == 0:
        flag += i
for i in flag_comp:
    a = ord(i) ^ 81
    if ((a >> (2 * 0)) & 3) == 3 and ((a >> (2 * 1)) & 3) == 1 and ((a >> (2 * 2)) & 3) == 2 and ((a >> (2 * 3)) & 3) == 1:
        flag += i
for i in flag_comp:
    a = ord(i) ^ 156
    if ((a >> (2 * 0)) & 3) == 3 and ((a >> (2 * 1)) & 3) == 3 and ((a >> (2 * 2)) & 3) == 3 and ((a >> (2 * 3)) & 3) == 3:
        flag += i
for i in flag_comp:
    a = ord(i) ^ 66
    if ((a >> (2 * 0)) & 3) == 3 and ((a >> (2 * 1)) & 3) == 1 and ((a >> (2 * 2)) & 3) == 3 and ((a >> (2 * 3)) & 3) == 1:
        flag += i
for i in flag_comp:
    a = ord(i) ^ 48
    if ((a >> (2 * 0)) & 3) == 3 and ((a >> (2 * 1)) & 3) == 0 and ((a >> (2 * 2)) & 3) == 0 and ((a >> (2 * 3)) & 3) == 0:
        flag += i
for i in flag_comp:
    a = ord(i) ^ 0
    if ((a >> (2 * 0)) & 3) == 2 and ((a >> (2 * 1)) & 3) == 1 and ((a >> (2 * 2)) & 3) == 3 and ((a >> (2 * 3)) & 3) == 0:
        flag += i
print(flag)
```

![alt text](_IMG/image-35.png)

```
flag: wctf{Cub3_5pUn_f746a6c536}
```

## Mong WRITEUP này giúp ích cho các bạn!

```
from KMA
Author: 13r_ə_Rɪst
```
