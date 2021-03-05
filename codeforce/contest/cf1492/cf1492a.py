t = int(input())

for tc in range(t):
    p, a, b, c = map(int, input().split())
    ans = 0
    chk = list()
    chk.append((a-(p % a)) % a)
    chk.append((b-(p % b)) % b)
    chk.append((c-(p % c)) % c)
    print(chk)
