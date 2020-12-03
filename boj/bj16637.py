import itertools

length = input()
exp = input()
expl = list()
op = list()
for i in range(len(exp)):
    expl.append(exp[i])
    if i % 2 == 1:
        op.append(i)

nPr = itertools.permutations(op, len(op))
# print(list(nPr))

result = -9999999999999999999999999999

for l in list(nPr):
    tmp = expl[:]
    cnt = 0
    print(l, exp)
    for i in l:
        cnt += 1
        idx = 1
        while True:
            if tmp[i-idx][-1:].isdigit():
                left = tmp[i-idx]
                tmp[i-idx] = ''
                break
            else:
                idx += 1
        idx = 1
        while True:
            if tmp[i+idx][-1:].isdigit():
                right = tmp[i+idx]
                tmp[i+idx] = ''
                break
            else:
                idx += 1

        print('>>>>>>>>>', left, right, end='')

        if tmp[i] == '*':
            tmp[i] = str(int(left)*int(right))
        elif tmp[i] == '+':
            tmp[i] = str(int(left)+int(right))
        else:  # '-'
            tmp[i] = str(int(left)-int(right))
        if cnt == len(op):
            result = max(result, int(tmp[i]))
        print("=======", tmp[i], tmp)
    # print('<<<<<<<<<<<<<<<<<<', result)

print(result)
