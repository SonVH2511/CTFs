from befunge import read_in, befunge

prog = read_in('prog.befunge')
print('flag? ')
flag = ['w', 'c', 't', 'f', '{', 'p', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
        '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

i = 6
default_len = 926
flag_comp = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=<>,.?/{}[]\|~:;"\''
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


# prog = read_in('prog.befunge')
# print('flag? ')

# flag_comp = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=<>,.?/{}[]\|~:;"\''
# flag = ['w', 'c', 't', 'f', '{', '', '', '', '', '', '', '', '',]
# i = 5

# for j in flag_comp:
#     flag[i] = j
#     ret = befunge(prog, flag)
#     print(ret)
