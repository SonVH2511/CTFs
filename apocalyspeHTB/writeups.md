## SubTask/apocalyspeHTB

### Crushing

![alt text](_IMG/image.png)

- Chall này cấp cho người chơi 2 file, `message.txt.cz` cùng `crush`. Dựa trên mô tả của chall, file `message.txt.cz` chính là đoạn hội thoại bị mã hóa. Vậy file `crush` có vẻ là file mã hóa ta cần detect.

- Chương trình mã hóa khá ngắn gọn. Thoạt nhìn không giống mã hóa đối xứng nên không thể truyền ngược vào được. Mình cần phân tích xem chương trình hoạt động ra sao để giải mã.
  ![alt text](_IMG/image-1.png)

- Chương trình mã hóa nhặt từng kí tự từ `input` và đẩy vào hàm `add_char_to_map()`. Nếu kí tự được truyền vào lần đầu, thì thực hiện khối lệnh `else` ở dưới, nếu không chạy dòng lệnh trên.

![alt text](_IMG/image-2.png)

- Thứ ta cần quan tâm ở đây là `v6`. Cẩn thận quan sát, `Map[input]` được ép kiểu về `_QWORD **` khi gán với `v6`, tức là giá trị lưu trong `Map[]` là con trỏ, Nếu debug kí hơn với giá trị truyền vào cụ thể, ta có thể dễ dàng thấy được bản chất mảng `Map[]` chính là một mảng được xây dựng thủ công mô phỏng lại `STL Map<>` như `C++`. Nó lưu theo dạng ánh xạ, `v6` = Map[input] ~ một địa chỉ trỏ tới một dải data khác, nếu vị trí trỏ tới được lưu vào giá trị bằng `v5 = i` trước đó, thực hiện dịch con trỏ lên cho tới `null` và lưu giá trị vào. Tóm lại là lưu data theo dạng `key - Arr:value`, Con trỏ của kí tự `a` trỏ tới con trỏ kiểm soát vị trí nó được xuất hiện `i`.

![alt text](_IMG/image-3.png)

- Nêu một ví dụ dễ hiểu, nếu chuỗi đầu vào của ta là `abcdefgh1234abcdef4321`. Các giá trị được lưu như sau.

![alt text](_IMG/image-4.png)

- Vậy ta đã rõ cách lấy giá trị của chương trình. Tới hàm `serialize_and_output`, phần `output` được in ra gồm 2 thứ. Số lần kí tự `chr(i)` xuất hiện = `ptr = list_len(Map[i])`. Và vị trí của các kí tự đó `j = (void *)*v2`.

![alt text](_IMG/image-5.png)

- Vậy chương trình mã hóa sẽ mã hóa sẽ lấy ra vị trí của các kí tự trong văn bản rồi in lần lượt chúng ra theo thứ tự trong bảng mã `ASCII`, bằng chứng là nó duyệt `Map[]` từ 0-254 trong hàm `serialize_and_output`. Sau đó in lần lượt vị trí của kí tự đó ra.

- Kiểm chứng bằng cách xem giá trị trong văn bản bị mã hóa. Dễ dàng thấy được kí tự đầu tiên xuất hiện là kí tự thứ 10 ~ `0xa` ~ `\n`.

![alt text](_IMG/image-6.png)

- Lưu ý rằng các giá trị được in ra dạng 8 byte một, convert sang số nguyên bằng cách dịch bit và cộng thêm là được.

![alt text](_IMG/image-7.png)

- Sau đây là script của mình để giải mã file `message.txt.cz`.

```python
with open('message.txt.cz', 'rb') as file:
    content = file.read()
i = 0
tmp = 0
b = 0
message = [0]*9000
__to_Int_Cipher = []
while i < len(content):
    if (i+1) % 8 != 0:
        # content[i] <<= 8*tmp
        b += content[i] << (8*tmp)
        tmp += 1
    else:
        __to_Int_Cipher.append(b)
        tmp = 0
        b = 0
    i += 1

# # print(__to_Int_Cipher)

i = 0
mod = 0
while i < len(__to_Int_Cipher):
    j = i + 1
    tmpDec = __to_Int_Cipher[i]
    k = i-mod
    while tmpDec != 0:
        mod += 1
        message[__to_Int_Cipher[j]] = k
        j += 1
        tmpDec -= 1
    i += __to_Int_Cipher[i]+1
# print(message)
msg = ''
for p in message:
    msg += chr(p)
print(msg)
```

- Đoạn hội thoại sau khi được giải mã:

```txt
Organizer 1: Hey, did you finalize the password for the next... you know?

Organizer 2: Yeah, I did. It's "HTB{4_v3ry_b4d_compr3ss1on_sch3m3}"

Organizer 1: "HTB{4_v3ry_b4d_compr3ss1on_sch3m3}," got it. Sounds ominous enough to keep things interesting. Where do we spread the word?

Organizer 2: Let's stick to the usual channels: encrypted messages to the leaders and discreetly slip it into the training manuals for the participants.

Organizer 1: Perfect. And let's make sure it's not leaked this time. Last thing we need is an early bird getting the worm.

Organizer 2: Agreed. We can't afford any slip-ups, especially with the stakes so high. The anticipation leading up to it should be palpable.

Organizer 1: Absolutely. The thrill of the unknown is what keeps them coming back for more. "HTB{4_v3ry_b4d_compr3ss1on_sch3m3}" it is then.
```

```
Flag: HTB{4_v3ry_b4d_compr3ss1on_sch3m3}
```

### Metagaming

- Chall này cấp cho ta source `C++`. Chương trình không thể thực thi nên mình đọc chay.

- Tóm gọn chương trình như sau. Chương trình thực thi gồm 2 đoạn chính, `mã hóa` và `kiểm tra`.

- Flag được truyền vào hàm mã hóa với các truy vấn cụ thể gồm 3 phần, `opcode` dùng để rẽ nhánh trong hàm xử lý, `op0` và `op1` tùy mục đích mà thay đổi trong từng case.

```C++
struct insn_t
{
    uint32_t opcode = 0;
    uint32_t op0 = 0;
    uint32_t op1 = 0;
};
```

- Sau khi xử lý, `Flag` được mã hóa thành `registers` và kiểm tra với từng số nguyên một.

![alt text](_IMG/image-9.png)

- Quan sát cẩn ở case `opcode == 0`, đây là case lấy giá trị từ `flag[op1]` vào `regs[op0]`. Ý tưởng của mình là tìm các case `insn_t(0, 0->5, op1)` bởi ta biết được format flag là `HTB{}`.

![alt text](_IMG/image-8.png)

- Nhặt ra các case có op0 = 1.

```C++
insn_t(21, 0, 0)
insn_t(0, 14, 0)
insn_t(24, 14, 0)
insn_t(5, 0, 14)
insn_t(0, 14, 1)
insn_t(5, 0, 14)
insn_t(0, 14, 2)
insn_t(5, 0, 14)
insn_t(0, 14, 3)
insn_t(5, 0, 14)
insn_t(8, 0, 2769503260)
insn_t(10, 0, 997841014)
insn_t(2, 0, 4065997671)
insn_t(8, 0, 690011675)
insn_t(8, 0, 540576667)
insn_t(2, 0, 1618285201)
insn_t(8, 0, 1123989331)
insn_t(8, 0, 1914950564)
insn_t(8, 0, 4213669998)
insn_t(8, 0, 1529621790)
insn_t(10, 0, 865446746)
insn_t(8, 0, 449019059)
insn_t(8, 0, 906976959)
insn_t(8, 0, 892028723)
insn_t(10, 0, 1040131328)
insn_t(2, 0, 3854135066)
insn_t(2, 0, 4133925041)
insn_t(2, 0, 1738396966)
insn_t(8, 0, 550277338)
insn_t(10, 0, 1043160697)
insn_t(3, 0, 1)
```

- Mình nhặt ra các lệnh có `op0 = 0` bởi thấy `insn_t(0, 14, 0-3)` Chương trình thực hiện nhặt ra giá trị từng kí tự của flag bộ 4 lần một và nối chúng thành một số nguyên.

```C++
Flag[0] = (int)'H';
Flag[1] = (int)'T';
Flag[2] = (int)'B';
Flag[3] = (int)'{';

Regs[0] = 0;

Regs[14] = Flag[0];
Regs[14] <<= 0;
Regs[0] |= Regs[14];

Regs[14] = Flag[1];
Regs[14] <<= 8;
Regs[0] |= Regs[14];

Regs[14] = Flag[2];
Regs[14] <<= 16;
Regs[0] |= Regs[14];

Regs[14] = Flag[3];
Regs[14] <<= 24;
Regs[0] |= Regs[14];

Regs[0] ^= 1176768057;
Regs[0] -= 2368952475;
Regs[0] ^= 2826144967;
Regs[0] += 1275301297;
Regs[0] -= 2955899422;
Regs[0] ^= 2241699318;
Regs[0] += 537794314;
Regs[0] += 473021534;
Regs[0] += 2381227371;
Regs[0] -= 3973380876;
Regs[0] -= 1728990628;
Regs[0] += 2974252696;
Regs[0] += 1912236055;
Regs[0] ^= 3620744853;
Regs[0] ^= 2628426447;
Regs[0] -= 486914414;
Regs[0] -= 1187047173;
```

- Cuối cùng là truy vấn `insn_t(3, 0, 1)`. Thực hiện xor(Regs[0],Regs[1]). Sau đó so sánh Regs[0] với `0x3ee88722` với 4 kí tự đầu có trước, ta suy ngược ra giá trị Regs[1] tại thời điểm `xor`.

![alt text](_IMG/image-13.png)

Điều tương tự xuất hiện với Regs[0] -> Regs[9].

![alt text](_IMG/image-10.png)

Vậy ta có thể dựa vào nó mà bruteForce. 10 biến, mỗi biến nhặt ra bộ 4 kí tự một liên tiếp của `flag`, từ source ta còn biết ràng `flag` có độ dài 40 tương ứng với 10 `Regs[]` đầu. Vậy chỉ cần nhặt ra truy vấn của từng `op0` một sẽ ra được đáp án.

![alt text](_IMG/image-11.png)

- script vét cạn như sau ![script](rev_metagaming/sc.cpp)

```
flag: HTB{m4n_1_l0v4_cXX_TeMpl4t35_9fb60c17b0}
```

###

## Mong WRITEUP này giúp ích cho các bạn!

```

from KMA
Author: 13r_ə_Rɪst
Email: sonvha2k23@cvp.vn

```
