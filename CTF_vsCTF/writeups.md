## CTFs/L3akCTF

### intro

- Patch lại đoạn sleep để in thẳng thứ dưới đây ra.

```
                                 /$$      /$$$$$$   /$$$   /$$          /$$$$$$$$         /$$$$$$                  /$$$$$$              /$$$$$$  /$$$$$$$  /$$$$$$$   /$$                       /$$ /$$$
                                | $$     /$$__  $$ /$$_/ /$$$$         |__  $$__/        /$$$_  $$                /$$__  $$            /$$__  $$| $$__  $$| $$____/ /$$$$                      | $$|_  $$
 /$$    /$$ /$$$$$$$  /$$$$$$$ /$$$$$$  | $$  \__/| $$  |_  $$   /$$$$$$$ | $$  /$$$$$$ | $$$$\ $$        /$$$$$$|__/  \ $$ /$$    /$$|__/  \ $$| $$  \ $$| $$     |_  $$   /$$$$$$$   /$$$$$$ | $$  | $$
|  $$  /$$//$$_____/ /$$_____/|_  $$_/  | $$$$    /$$$    | $$  | $$__  $$| $$ /$$__  $$| $$ $$ $$       /$$__  $$  /$$$$$/|  $$  /$$/   /$$$$$/| $$$$$$$/| $$$$$$$  | $$  | $$__  $$ /$$__  $$| $$  | $$$
 \  $$/$$/|  $$$$$$ | $$        | $$    | $$_/   |  $$    | $$  | $$  \ $$| $$| $$  \__/| $$\ $$$$      | $$  \__/ |___  $$ \  $$/$$/   |___  $$| $$__  $$|_____  $$ | $$  | $$  \ $$| $$  \ $$|__/  | $$/
  \  $$$/  \____  $$| $$        | $$ /$$| $$      \ $$    | $$  | $$  | $$| $$| $$      | $$ \ $$$      | $$      /$$  \ $$  \  $$$/   /$$  \ $$| $$  \ $$ /$$  \ $$ | $$  | $$  | $$| $$  | $$      | $$
   \  $/   /$$$$$$$/|  $$$$$$$  |  $$$$/| $$      |  $$$ /$$$$$$| $$  | $$| $$| $$      |  $$$$$$/      | $$     |  $$$$$$/   \  $/   |  $$$$$$/| $$  | $$|  $$$$$$//$$$$$$| $$  | $$|  $$$$$$$ /$$ /$$$/
    \_/   |_______/  \_______/   \___/  |__/       \___/|______/|__/  |__/|__/|__/       \______//$$$$$$|__/      \______/     \_/     \______/ |__/  |__/ \______/|______/|__/  |__/ \____  $$|__/|___/
                                                                                                |______/                                                                              /$$  \ $$
                                                                                                                                                                                     |  $$$$$$/
                                                                                                                                                                                      \______/
```

```
flag: vsctf{1nTr0_r3v3R51ng!}
```

### funchecker

- Khá trôn, phần mô tả nhắc tới `.net` mà chẳng liên quan gì, thậm chí quăng vào các tool phân tích chuyên dụng cũng không chỉ ra được gì.

- Debug tới đoạn check và bruteforce thôi.

```C
__int64 __fastcall check(__int64 a1)
{
  __int64 v3; // rax
  unsigned __int8 *v4; // rbx
  _QWORD *v5; // rcx
  int Input_len; // edx
  _QWORD *v7; // r8
  unsigned int v8; // eax
  __int64 v9; // r8
  int v10; // r10d
  int v11; // r9d
  int i; // r11d

  if ( *(_DWORD *)(a1 + 8) != 1 )
    return sub_7FF786B85C10((__int64)&unk_7FF786BD3350);
  if ( *(&qword_7FF786BD5398 - 1) )
    sub_7FF786B21348();
  v3 = sub_7FF786BB53C0(*(_QWORD *)(qword_7FF786C2C278 + 8), *(_QWORD *)(a1 + 16));
  v4 = (unsigned __int8 *)v3;
  if ( v3 )
  {
    v5 = (_QWORD *)(v3 + 16);
    Input_len = *(_DWORD *)(v3 + 8);
  }
  else
  {
    v5 = 0i64;
    Input_len = 0;
  }
  v7 = 0i64;
  if ( Input_len )
    v7 = v5;
  if ( seemChecker(v7, Input_len, 0i64) == 0xA8A85CFA9660DB0Fui64 && *((_DWORD *)v4 + 2) == 40 )
  {
    v8 = 0;
    while ( 1 )
    {
      v9 = v4[v8 + 16];
      v10 = 4;
      v11 = 6;
      for ( i = 0; i < 5; ++i )
      {
        v9 ^= __ROR8__(v9, v11) ^ __ROL8__(v9, v10);
        v10 *= 2;
        v11 *= 2;
      }
      if ( *(_QWORD *)(*(_QWORD *)(qword_7FF786C2C168 + 8) + 8i64 * v8 + 16) != v9 )
        break;
      if ( (int)++v8 >= 0x28 )
        return sub_7FF786B85C10((__int64)&unk_7FF786BCFA00);
    }
  }
  return sub_7FF786B85C10((__int64)&unk_7FF786BD0C48);
}
```

- Hàm check có 2 cái, cái đầu tiên kiểm tra với len() khá sợ, còn trong khối lệnh điều kiện khi thỏa mãn 2 điều kiện `seemChecker(v7, Input_len, 0i64) == 0xA8A85CFA9660DB0Fui64 && *((_DWORD *)v4 + 2) == 40` thì thực hiện check từng phần tử sau khi mã hóa với một dải `const`.

```python
def __ROL8__(n, rotations, bits=64):
    rotations %= bits
    return ((n << rotations) | (n >> (bits - rotations))) & ((1 << bits) - 1)


def __ROR8__(n, rotations, bits=64):
    rotations %= bits
    return ((n >> rotations) | (n << (bits - rotations))) & ((1 << bits) - 1)


print(hex(__ROR8__(0x589FDA54EB82CC74, 0x60)))
print(hex(__ROL8__(0x589FDA54EB82CC74, 0x40)))

const = [0xfa97d8710c8b9b54, 0xeb82cc74589fda54, 0xee928c654d8bdf01, 0x5a35d0732e291bfe, 0xff879860199f9e01, 0x690aec7cd215d8fe, 0x7d0fb86893159cab, 0xf30c0333f3c0fff, 0xbec388645cda9f54, 0xf30c0333f3c0fff, 0x5f2590623b3d1eab, 0xc9a8e47ef0b75854, 0x226e7c5abd78d301, 0xddadb06ab1b71c01, 0x5f61c4322e6d4faa, 0x6c1aac6dc701ddab, 0xf7494632a6c5efe, 0xeb82cc74589fda54, 0x226e7c5abd78d301, 0xbbd3c87549ce9a01,
         0xffc3cc300ccfcf00, 0xfa97d8710c8b9b54, 0xffc3cc300ccfcf00, 0xbbd3c87549ce9a01, 0xeb82cc74589fda54, 0x5f61c4322e6d4faa, 0x7d0fb86893159cab, 0xafd69c6108cede54, 0x226e7c5abd78d301, 0x7d0fb86893159cab, 0x4e3084676f295fab, 0x5a35d0732e291bfe, 0x5f61c4322e6d4faa, 0xfa97d8710c8b9b54, 0xf7494632a6c5efe, 0x226e7c5abd78d301, 0x4e3084676f295fab, 0xf30c0333f3c0fff, 0x5a35d0732e291bfe, 0x88ecf47ab5f25901]
ans = ""
flag_comp = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=<>,.?/{}[]\|~:;"\''


for i in range(0x28):
    for c in flag_comp:
        v9 = ord(c)
        v10 = 4
        v11 = 6
        for j in range(5):
            v9 = v9 ^ (__ROR8__(v9, v11) ^ __ROL8__(v9, v10))
            v10 *= 2
            v11 *= 2
        if (v9 == const[i]):
            # print(c, " ", hex(v9), " ", i, " ", const[i])
            ans += c
            break
print(ans)
```

```
flag: vsctf{n0b0dy_l1kes_r3v3rs1ng_nat1ve_a0t}
```

## Mong WRITEUP này giúp ích cho các bạn!

```py
from KMA
Author: 13r_ə_Rɪst
```
