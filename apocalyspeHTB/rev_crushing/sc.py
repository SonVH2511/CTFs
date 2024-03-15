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
# HTB{4_v3ry_b4d_compr3ss1on_sch3m3}
