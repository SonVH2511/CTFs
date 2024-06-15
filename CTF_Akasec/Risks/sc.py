from z3 import *


def outPut(comp):
    arr = []
    while comp != 0:
        arr.append(comp & 0xff)
        comp = comp >> 8
    return arr


param_1 = [0]*4

flag_pos = [BitVec("x{}".format(i), 64) for i in range(4)]
s = Solver()


param_1[0] = flag_pos[0] + 0x75978f47ac76cf
param_1[1] = flag_pos[1] + 0xff889b2d229768ef
param_1[0] = param_1[0] ^ 0x76bf86ade5d5cc
param_1[2] = flag_pos[2] + 0x760f38b4bc69dc
param_1[0] = param_1[0] ^ 0x559f46365cee21
param_1[0] = param_1[0] + 0x5c6476bf0d4a19
param_1[0] = param_1[0] ^ 0xed41cda9780
param_1[2] = param_1[2] ^ 0x1e555c027a4e43
param_1[3] = flag_pos[3] + 0xfff29f96915a6e96
param_1[0] = param_1[0] ^ 0x4c46c321e8dc3d
param_1[2] = param_1[2] + 0x440d7b5dafb63c
param_1[3] = param_1[3] ^ 0x39549dd6e1299b
param_1[0] = param_1[0] + 0xff80a83276856f6b
param_1[0] = param_1[0] + 0x3869018f758dd0
param_1[0] = param_1[0] + 0xfff507f694ac1618
param_1[0] = param_1[0] + 0xffaef9a6a60ac41c
param_1[2] = param_1[2] ^ 0x4bb739ae97e2b2
param_1[0] = param_1[0] ^ 0xb9c189c728744
param_1[3] = param_1[3] ^ 0x63b60e480e2904
param_1[1] = param_1[1] + 0x70ea19e458d1dd
param_1[0] = param_1[0] ^ 0x1c380c9255dc4a
param_1[0] = param_1[0] ^ 0x72195b264896c6
param_1[0] = param_1[0] + 0xb58f5721006db
param_1[1] = param_1[1] + 0xfff1a19d465554d0
param_1[1] = param_1[1] + 0x45c8dee1a136cd
param_1[1] = param_1[1] + 0xff95aa1bc2ad9c07
param_1[3] = param_1[3] + 0xffed79b44c733cd6
param_1[0] = param_1[0] + 0x27d894eb9caa9b
param_1[3] = param_1[3] + 0xff9cb13f334ec53a
param_1[3] = param_1[3] + 0x3c2a0d8d36145a
param_1[1] = param_1[1] + 0x30a473f940b5dd
param_1[2] = param_1[2] + 0x7239ea8aa2bc49
param_1[1] = param_1[1] + 0x71e89e42b8b132
param_1[1] = param_1[1] + 0xff887455a5eb36fd
param_1[2] = param_1[2] + 0xffc07313a3962d72
param_1[2] = param_1[2] + 0xffcf924d075d2a72
param_1[1] = param_1[1] ^ 0x3707089012b521
param_1[2] = param_1[2] + 0x12b99b0e57e3bb
param_1[1] = param_1[1] + 0x3e897bb78bc162
param_1[2] = param_1[2] + 0xffc244c1f804fc9b
param_1[3] = param_1[3] ^ 0x21e211817f468b
param_1[3] = param_1[3] + 0x44c0052fcca332
param_1[1] = param_1[1] + 0x4f53af9faf8acf
param_1[1] = param_1[1] + 0x2fda660863a649
param_1[1] = param_1[1] + 0xffa9f06d0990b3ac
param_1[2] = param_1[2] + 0x2e93addef2df4f
param_1[3] = param_1[3] + 0x4531b2344b641b
param_1[3] = param_1[3] + 0xfff8e89a72f8e26c
param_1[1] = param_1[1] + 0x15c6da9bc36ed0
param_1[2] = param_1[2] ^ 0x738278f8599e2d
param_1[1] = param_1[1] ^ 0x44dd76d42e4513
param_1[1] = param_1[1] + 0xffb57183e089ceb4
param_1[2] = param_1[2] ^ 0x27972fbdfd287c
param_1[0] = param_1[0] ^ 0x7eb9039a2b6bf0
param_1[2] = param_1[2] + 0xffc75c67f5de1b31

param_1[0] = param_1[0] ^ 0x131e29f760409
param_1[1] = param_1[1] + 0x23fe2dd7650a73
param_1[1] = param_1[1] + 0xfff70308e97acf79
param_1[2] = param_1[2] + 0xffb870f6f2950920
param_1[0] = param_1[0] ^ 0x58bd244826ef43
param_1[2] = param_1[2] + 0xffdc5874e8d03bbc
param_1[1] = param_1[1] + 0xffb3ce0944bbfc19
param_1[0] = param_1[0] ^ 0x38b3e1c4b3be14
param_1[3] = param_1[3] ^ 0x6de4b0dccee1f8
param_1[2] = param_1[2] + 0x48e99a2ccfbefa
param_1[2] = param_1[2] + 0x2803831f197314
param_1[2] = param_1[2] ^ 0x7fd3195c5e8bfb
param_1[1] = param_1[1] + 0x2311f9e5515a6d
param_1[3] = param_1[3] + 0x29e99994341bad
param_1[2] = param_1[2] + 0xffa46f41e698229f
param_1[0] = param_1[0] ^ 0x16097f9beb9df8
param_1[2] = param_1[2] ^ 0x58f5f5f9e64f77
param_1[2] = param_1[2] + 0xffce81bd3383de95
param_1[0] = param_1[0] + 0x1437a45ffed077
param_1[2] = param_1[2] + 0x4ec7609899b599
param_1[3] = param_1[3] + 0x77832406a422ee
param_1[0] = param_1[0] ^ 0xa299bfabd147f
param_1[0] = param_1[0] + 0xff9731d63e0a4ce9
param_1[0] = param_1[0] ^ 0x3ea0b669b87301
param_1[0] = param_1[0] ^ 0x7bc3ff2762eeb0
param_1[0] = param_1[0] + 0x2ff3559df23d95
param_1[2] = param_1[2] + 0xffb0934ca254c450
param_1[0] = param_1[0] + 0xff8b3b8d33d104e1
param_1[3] = param_1[3] ^ 0x2f268e55029508
param_1[2] = param_1[2] + 0xffe1c76d94c5b270
param_1[3] = param_1[3] ^ 0x5575918734e1cd
param_1[0] = param_1[0] + 0xffe368f50fe7ff81
param_1[0] = param_1[0] ^ 0x22b615021c1680
param_1[0] = param_1[0] + 0xff95c819c49f5170
param_1[2] = param_1[2] + 0x485e655976a7ee
param_1[0] = param_1[0] + 0x6f4847b022b253
param_1[1] = param_1[1] ^ 0x392622311d6f3d
param_1[1] = param_1[1] + 0xffb3096849dd7eb3
param_1[3] = param_1[3] ^ 0x6e8b5de620fa
param_1[3] = param_1[3] + 0x21d4322fefd286
param_1[3] = param_1[3] + 0xffe14e96454625c5
param_1[3] = param_1[3] ^ 0x4757d3b35495bb
param_1[1] = param_1[1] + 0xffc4845886e53673
param_1[0] = param_1[0] ^ 0x57617d2db4d1c4
param_1[0] = param_1[0] ^ 0x69bd97ec881da
param_1[2] = param_1[2] ^ 0x57ac6bbc11593
param_1[2] = param_1[2] ^ 0x5c2cbf22512aa3
param_1[2] = param_1[2] + 0x1860e298e3c0d5
param_1[2] = param_1[2] + 0xffe6f1b24728fb11
param_1[0] = param_1[0] + 0x4561b3931db109
param_1[0] = param_1[0] ^ 0x1a70a95138d536
param_1[2] = param_1[2] + 0x32ff8082367e19
param_1[3] = param_1[3] + 0xff99a53e605869f2
param_1[0] = param_1[0] + 0x1e359449108efb
param_1[0] = param_1[0] + 0xff9338172cb899f9
param_1[0] = param_1[0] + 0x33dbc3093cba9e
param_1[1] = param_1[1] + 0x7d005d760e8a00
param_1[0] = param_1[0] ^ 0x630abe094f2fcb
param_1[2] = param_1[2] ^ 0x5c693ca6ad4098
param_1[2] = param_1[2] ^ 0x1218c2c1fc6aab
param_1[2] = param_1[2] ^ 0x78d35fbb138c9c
param_1[3] = param_1[3] + 0x42dfb926a777d2
param_1[3] = param_1[3] ^ 0x3f60fd507495c5
param_1[1] = param_1[1] + 0x2cca6aa235fa04
param_1[0] = param_1[0] + 0x5a8e68db17f162
param_1[0] = param_1[0] + 0x1287bd45883bda
param_1[0] = param_1[0] + 0xffe7b46bbeb822c6
param_1[3] = param_1[3] + 0x5234b2a7901fd8
param_1[3] = param_1[3] + 0xa856e4c03b946
param_1[1] = param_1[1] ^ 0x6312ec05f527a4
param_1[1] = param_1[1] + 0x46ce8a9c234e2f
param_1[3] = param_1[3] + 0x171cfaebba97ed

param_1[2] = param_1[2] ^ 0x21552380a54ebd
param_1[2] = param_1[2] ^ 0x217fe5a723014c
param_1[2] = param_1[2] + 0xff929930c56e6594
param_1[2] = param_1[2] ^ 0x7eb96f8929799a
param_1[3] = param_1[3] + 0x67d0ff39897513
param_1[3] = param_1[3] + 0x26a2f35c92df10
param_1[2] = param_1[2] + 0xffd5d8a901dbebd6
param_1[2] = param_1[2] + 0xad9fcf45aef6
param_1[2] = param_1[2] + 0xffc53d1702ef8aa8
param_1[0] = param_1[0] + 0x591ac5d1939c8b
param_1[2] = param_1[2] ^ 0x33d94a84565532
param_1[2] = param_1[2] ^ 0x308afb7e01e13e
param_1[3] = param_1[3] + 0xffb48db7039082e1
param_1[2] = param_1[2] ^ 0x55662e74858cf1
param_1[3] = param_1[3] + 0xffa5b828a6179210
param_1[1] = param_1[1] ^ 0x1638c6225c560d
param_1[2] = param_1[2] ^ 0x40641fcdaf2a6d
param_1[0] = param_1[0] + 0x1907586d8aaec6
param_1[1] = param_1[1] ^ 0x2ac0e1d87fbfd3
param_1[0] = param_1[0] + 0x4903ecf455fa05
param_1[1] = param_1[1] + 0xff84efef75a89283
param_1[2] = param_1[2] ^ 0x575e02c2ec2e98
param_1[2] = param_1[2] ^ 0x5686c924044043
param_1[0] = param_1[0] + 0xffa75728515de781
param_1[0] = param_1[0] + 0x6c40d33a5de8b4
param_1[0] = param_1[0] + 0xffae776809930118
param_1[1] = param_1[1] + 0x77250c081305ce
param_1[2] = param_1[2] + 0xffeff0d64a3fb770
param_1[3] = param_1[3] + 0x1106386668917b
param_1[2] = param_1[2] ^ 0x2a958285eaabc6
param_1[1] = param_1[1] + 0x17e82fdc4bb7e6
param_1[2] = param_1[2] + 0x6e5b6deacda2b3
param_1[1] = param_1[1] + 0xffe4362cd469721d
param_1[1] = param_1[1] ^ 0x46a8ddb8e7831e
param_1[0] = param_1[0] + 0x5ef639bb0d96fc
param_1[3] = param_1[3] ^ 0x540dd0d8537808
param_1[3] = param_1[3] + 0xffd7468d44d84bfc
param_1[2] = param_1[2] + 0xffb5048de8c6e26a
param_1[0] = param_1[0] ^ 0x457b282105f5ff
param_1[1] = param_1[1] ^ 0x2eff779ebf04ee
param_1[1] = param_1[1] ^ 0x282c4c9602a8d1
param_1[0] = param_1[0] ^ 0x5892a99ecd56db
param_1[1] = param_1[1] + 0x7306fd8fb4ac48
param_1[3] = param_1[3] + 0x4b3f6ca9126599
param_1[3] = param_1[3] + 0xffed5514bbd0b395
param_1[0] = param_1[0] + 0x19b2a80c1ebde0
param_1[2] = param_1[2] ^ 0x34ab995333d7bc
param_1[0] = param_1[0] ^ 0x4b803835540e77
param_1[2] = param_1[2] ^ 0x4aaf3dd459117d
param_1[3] = param_1[3] ^ 0x45b9bf142dd7b9
param_1[0] = param_1[0] + 0xffdae06e2a1c7254
param_1[1] = param_1[1] + 0xff805d1980ad21aa
param_1[0] = param_1[0] + 0xff8aba0c42d40896
param_1[0] = param_1[0] + 0x425422cc59e30
param_1[0] = param_1[0] + 0x235f71339ac927
param_1[2] = param_1[2] + 0xffb282c744cb6616
param_1[2] = param_1[2] + 0xffa61489eb15d360
param_1[0] = param_1[0] ^ 0x8db3daacc3ff9
param_1[2] = param_1[2] ^ 0x97368bc6e7d41
param_1[3] = param_1[3] ^ 0x86c96f6b4510f
param_1[2] = param_1[2] ^ 0x1951f11deeb2fa
param_1[1] = param_1[1] + 0x5dc2de99056b51
param_1[2] = param_1[2] + 0xffb654da8cc4cb5f


param_1[3] = param_1[3] + 0xffdb0267f30481de
param_1[0] = param_1[0] + 0xd349975ed71ce
param_1[3] = param_1[3] + 0x396b3ec36373cc
param_1[3] = param_1[3] ^ 0x2d2d96a9d4da30
param_1[2] = param_1[2] ^ 0x656498272858da
param_1[2] = param_1[2] + 0xffb3ad5ab10bc1f3
param_1[0] = param_1[0] + 0x23b2f30be0e9ab
param_1[0] = param_1[0] + 0xff99bef8c799559b
param_1[0] = param_1[0] + 0xffe049bda2d90572
param_1[2] = param_1[2] + 0xff9d4568f99d45eb
param_1[2] = param_1[2] ^ 0x26ed48b4153eb0
param_1[2] = param_1[2] ^ 0x1af75e7b5b8c5f
param_1[2] = param_1[2] + 0xffe9fc2941b7bd92
param_1[1] = param_1[1] ^ 0x4b4b690f995f73
param_1[0] = param_1[0] + 0xffa3bcbff21dd191
param_1[2] = param_1[2] ^ 0x6feb10d533c4b1
param_1[1] = param_1[1] + 0xffb8a8e39fec3250
param_1[2] = param_1[2] + 0xffdb2496d81b4293
param_1[0] = param_1[0] + 0xffb778b645f31de9
param_1[0] = param_1[0] ^ 0x531e0306cda7a9
param_1[2] = param_1[2] ^ 0x3521f52cd98bf4
param_1[1] = param_1[1] + 0xff880d1e8951a4a0
param_1[2] = param_1[2] + 0x3858d7d314a793
param_1[2] = param_1[2] + 0xffd7c92ed6f1e27a
param_1[1] = param_1[1] + 0x37f1e8ac57fd21
param_1[2] = param_1[2] + 0x794d667495ec53
param_1[0] = param_1[0] + 0xf80ea376dfe9c
param_1[2] = param_1[2] + 0x7077ef6357df45
param_1[1] = param_1[1] + 0xfffe413b9b12d6da
param_1[3] = param_1[3] + 0x562536f5f8bacf
param_1[3] = param_1[3] + 0xff9f07032cf0845d
param_1[0] = param_1[0] ^ 0x4ba91df7d06027
param_1[0] = param_1[0] + 0xfff6ae6bcf2ebbbc
param_1[3] = param_1[3] ^ 0x55cdaa7dfb2afc
param_1[3] = param_1[3] + 0x318ce149b3a1fc
param_1[3] = param_1[3] + 0xffd5d916adc11571
param_1[0] = param_1[0] + 0xffc3560b3c7ef5e9
param_1[1] = param_1[1] + 0xa8c0f5e148a9e
param_1[2] = param_1[2] ^ 0x7b607330d80f26
param_1[0] = param_1[0] ^ 0x3c139ff1892f4f
param_1[1] = param_1[1] + 0x1f63d4725b825e
param_1[3] = param_1[3] + 0x6be58b7a89dd9d
param_1[1] = param_1[1] ^ 0x67b81b10716f5
param_1[1] = param_1[1] + 0x70efa9f526c942
param_1[3] = param_1[3] ^ 0x411eb7ecadc3cb
param_1[3] = param_1[3] ^ 0x250c9395e3a054
param_1[0] = param_1[0] + 0x78f186d15f1e3b

s.add(param_1[0] == 0x3167deae217139c1)
s.add(param_1[1] == 0x6745aeaf0c9a62e5)
s.add(param_1[2] == 0x62664d91c2da0c7b)
s.add(param_1[3] == 0x7ee01bea8defde65)

print(s.check())
model = s.model()
flag_bytes = b""

print(model)
oiut = []
ans = [3565552817372490593, 7436677046894157678,
       7148183886289055839, 9021675632591138352]
for i in ans:
    oiut += outPut(i)
print(oiut)
for i in oiut:
    print(chr(i), end="")
# akasec{1n_my_b4g_0n3_s3c0nd_0n3}
