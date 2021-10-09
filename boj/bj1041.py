'''
센터 ((n-2)^2)*5+(n-2)*4 개
엣지 (n-2)*4 + (n-1)*4 개
코너 4 개
 D
EABF
 C
'''
n = int(input())
a, b, c, d, e, f = map(int, input().split())
af_round = [b+c, c+e, e+d, d+b]
be_round = [a+d, d+f, f+c, c+a]
cd_round = [a+b, b+f, f+e, e+a]
dice = [a, b, c, d, e, f]
if n == 1:
    summ = sum(dice)
    ans = summ
    for i in range(6):
        ans = min(ans, summ-dice[i])
    print(ans)
else:
    center = 999
    edge = 999
    corner = 999

    center = min(dice)
    edge = min(min(af_round), min(be_round), min(cd_round))
    for i in range(6):
        if i == 0 or i == 5:
            for af_round_n in af_round:
                corner = min(corner, af_round_n+dice[i])
        if i == 1 or i == 4:
            for be_round_n in be_round:
                corner = min(corner, be_round_n+dice[i])
        if i == 2 or i == 3:
            for cd_round_n in cd_round:
                corner = min(corner, cd_round_n+dice[i])

    # print(center, '*', (((n-2) ** 2)+((n-2)*(n-1))*4),
    #     edge, '*', ((n-2)*4 + (n-1)*4), corner, '*', 4)
    print(center*(((n-2) ** 2)+((n-2)*(n-1))*4) +
          edge*((n-2)*4 + (n-1)*4)+corner*4)
