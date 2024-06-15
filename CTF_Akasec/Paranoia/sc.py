from pwn import *

while (True):
    # context.log_level = 'debug'
    p = remote('20.80.240.190', 1234)
    # for i in range(100):
    # p.recvuntil(b'Test')
    a = p.recvline()
    arr = a[:-1].decode()
    # nums = list(map(int, arr.split()))

    # print(arr)
    s = process('./sc')
    # print(str(arr).encode())
    s.sendline(arr.encode())
    result = s.recvline()
    print(result)
s.close()
# p.interactive()
