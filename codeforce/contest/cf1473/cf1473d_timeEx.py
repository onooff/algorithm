t = int(input())

for tc in range(t):
    n, m = map(int, input().split())
    p = input()
    for i in range(m):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        s = set()
        x = 0
        s.add(x)

        for j in range(0, l):
            if p[j] == '+':
                x += 1
            else:
                x -= 1
            # print('>>>', x)
            s.add(x)
        for j in range(r+1, n):
            if p[j] == '+':
                x += 1
            else:
                x -= 1
            # print('>>>', x)
            s.add(x)
        print(len(s))
        # print("------------------")
