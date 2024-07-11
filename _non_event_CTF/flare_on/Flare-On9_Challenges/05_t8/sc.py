A = "HTTP/1.0 200 OK\x0d\x0aServer: Apache On 9 \x0d\x0aDate: Tue, 14 Jun 2022 16:14:36 GMT\x0d\x0a\x0d\x0aTdQdBRa1nxGU06dbB27E7SQ7TJ2+cd7zstLXRQcLbmh2nTvDm1p5IfT/Cu0JxShk6tHQBRWwPlo9zA1dISfslkLgGDs41WK12ibWIflqLE4Yq3OYIEnLNjwVHrjL2U4Lu3ms+HQc4nfMWXPgcOHb4fhokk93/AJd5GTuC5z+4YsmgRh1Z90yinLBKB+fmGUyagT6gon/KHmJdvAOQ8nAnl8K/0XG+8zYQbZRwgY6tHvvpfyn9OXCyuct5/cOi8KWgALvVHQWafrp8qB/JtT+t5zmnezQlp3zPL4sj2CJfcUTK5copbZCyHexVD4jJN+LezJEtrDXP1DJNg=="
print(hex(0x110011001100110011001100110011 ^ 0x7F007E003C007400630070007D0077))
__flare = [0x66, 0x00, 0x6C, 0x00, 0x61, 0x00, 0x72, 0x00, 0x65, 0x00,
           0x2D, 0x00, 0x6F, 0x00, 0x6E, 0x00, 0x2E, 0x00, 0x63, 0x00,
           0x6F, 0x00, 0x6D, 0x00]
# print(hex(len(__flare)))
tmp = [0xF8, 0x4D, 0x79, 0x00, 0x40, 0xFC, 0x6F, 0x00, 0x50, 0xFC,
       0x6F, 0x00, 0x54, 0xFC, 0x6F, 0x00]
for i in tmp:
    print(chr(i))
