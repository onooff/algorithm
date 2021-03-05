t = int(input())

for tc in range(t):
    n = int(input())
    l = list(map(int, input().split()))

    h = 0
    v = 0
    d = 0

    def is_h(i):
        global l
        if i <= 0 or i >= len(l)-1:
            return False
        return l[i] > l[i-1] and l[i] > l[i+1]

    def is_v(i):
        global l
        if i <= 0 or i >= len(l)-1:
            return False
        return l[i] < l[i-1] and l[i] < l[i+1]

    for i in range(1, n-1):
        for j in range(l[i]):
            print('■', end='')
        print()
        cnt = 0
        if is_h(i):
            h += 1
            cnt = 1
            if is_v(i-1):
                cnt += 1
            if is_v(i+1):
                cnt += 1
            d = max(cnt, d)
        elif is_v(i):
            v += 1
            cnt = 1
            if is_h(i-1):
                cnt += 1
            if is_h(i+1):
                cnt += 1
            d = max(cnt, d)
    print('>>>test : ', h, v)
    print(h+v-d)
