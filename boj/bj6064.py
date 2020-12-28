t = int(input())

for tc in range(t):
    M, N, x, y = map(int, input().split())

    '''
    10 12 3 9 일때
    x가 3이 나오는 경우
    3, 13, 23, 33, ... M*cnt1+x
    y가 9가 나오는 경우
    9, 21, 33, 45, ... N*cnt2+y
    33에서 만나니까 답 33?
    그러면 끝나는 해 구하는 방법은? M*N?
    '''

    ans = 1
    i = x
    j = y
    limit = M*N
    setx = set()
    ans_OK = False
    while i <= limit:
        setx.add(i)
        i += M
    while j <= limit:
        if j in setx:
            ans_OK = True
            break
        j += N

    if ans_OK:
        print(j)
    else:
        print(-1)
