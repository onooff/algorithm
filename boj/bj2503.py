import sys
inputs = sys.stdin.readlines()

query = list()
for i in range(1, len(inputs)):
    tmp = inputs[i].split()
    tmp[1] = int(tmp[1])
    tmp[2] = int(tmp[2])
    tmp.append(set(tmp[0]))
    query.append(tmp)

nums = list()
n = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
chk = set()


def make_nums(s):
    global nums, n, chk
    for i in range(9):
        if i not in chk:
            if len(s) == 2:
                nums.append(s+n[i])
            else:
                chk.add(i)
                make_nums(s+n[i])
                chk.discard(i)


make_nums('')

ans = 0
for chk in nums:
    is_ans = True
    for q in query:
        s = 0
        b = 0
        for i in range(3):
            if chk[i] in q[3]:
                if chk[i] == q[0][i]:
                    s += 1
                else:
                    b += 1
        if not(s == q[1] and b == q[2]):
            is_ans = False
            break
    if is_ans:
        ans += 1
sys.stdout.write(str(ans))
