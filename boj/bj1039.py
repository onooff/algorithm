n, k = map(int, input().split())
if n < 10 or (n < 100 and n % 10 == 0):
    print(-1)
else:
    q = [n]
    while k > 0:
        sett = set()
        for num in q:
            nl = list(str(num))
            for i in range(len(nl)-1):
                for j in range(i+1, len(nl)):
                    nl[i], nl[j] = nl[j], nl[i]
                    sett.add(int(''.join(nl)))
                    nl[i], nl[j] = nl[j], nl[i]
        q = list(sett)
        k -= 1
    print(max(q))
