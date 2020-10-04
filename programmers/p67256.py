def solution(numbers, hand):
    answer = ''

    '''
    123
    456
    789
    *0#
    00 01 02
    10 11 12
    20 21 22
    30 31 32
    '''

    pad = [
        [3, 1],
        [0, 0],
        [0, 1],
        [0, 2],
        [1, 0],
        [1, 1],
        [1, 2],
        [2, 0],
        [2, 1],
        [2, 2],
        [3, 0],  # 별
        [3, 2],  # 샵
    ]

    l = 10
    r = 11

    for n in numbers:
        if (n == 1) or (n == 4) or (n == 7):  # 무조건 왼손으로 누르는 애들
            answer += 'L'
            l = n
        elif (n == 3) or (n == 6) or (n == 9):  # 무조건 오른손으로 누르는 애들
            answer += 'R'
            r = n
        else:  # 2,5,8,0 뭘로 누를지 모르는 애들
            # 거리를 구해본다
            ld = abs(pad[l][0]-pad[n][0])+abs(pad[l][1]-pad[n][1])
            rd = abs(pad[r][0]-pad[n][0])+abs(pad[r][1]-pad[n][1])
            if rd > ld:  # 왼손이 더 가까우면
                answer += 'L'
                l = n
            elif ld > rd:  # 오른손이 더 가까우면
                answer += 'R'
                r = n
            else:  # 거리 같은 경우는 자주 쓰는 손으로
                if hand == 'right':
                    answer += 'R'
                    r = n
                else:
                    answer += 'L'
                    l = n
        print(l, r)

    return answer
