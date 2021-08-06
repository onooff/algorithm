import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    a, b = map(int, input().split(' '))
    q = [(a, '')]
    chk = {a}
    while len(q) > 0:
        tmp = q.pop(0)
        # print(">>>", a, b, tmp)
        num = tmp[0]
        string = tmp[1]

        if num == b:
            print(string)
            break

        d = (num*2) % 10000
        s = num-1
        if num == 0:
            s = 9999
        l = ((num % 1000)*10)+num//1000
        r = (num//10)+((num % 10)*1000)
        if d not in chk:
            chk.add(d)
            q.append((d, string+'D'))
        if s not in chk:
            chk.add(s)
            q.append((s, string+'S'))
        if l not in chk:
            chk.add(l)
            q.append((l, string+'L'))
        if r not in chk:
            chk.add(r)
            q.append((r, string+'R'))
