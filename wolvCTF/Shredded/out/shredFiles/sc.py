shuffledLine = [2, 4, 18, 31, 19, 21, 13, 5, 12, 30, 27, 28, 25, 9,
                16, 6, 26, 24, 17, 29, 11, 14, 1, 3, 15, 7, 32, 0, 20, 23, 10, 8, 22]
lines = []
code_C = ["" for _ in range(40)]*35

for i in shuffledLine:
    with open(f"shred{i}.txt", 'r') as file:
        tmp = file.read()
        lines.append(tmp.rstrip())

for line in lines:
    for i in range(len(line)):
        if line[i] != '\n':
            code_C[i] += line[i]

for i in code_C:
    print(i)
