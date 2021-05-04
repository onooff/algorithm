'''
순위	당첨 내용
1	6개 번호가 모두 일치
2	5개 번호가 일치
3	4개 번호가 일치
4	3개 번호가 일치
5	2개 번호가 일치
6(낙첨)	그 외
'''


def solution(lottos, win_nums):
    answer = []
    s_lottos = set(lottos)
    s_win_nums = set(win_nums)
    s_lottos.discard(0)
    for n in s_lottos:
        s_win_nums.discard(n)
    answer.append(min(1+len(s_win_nums)-(len(lottos)-len(s_lottos)), 6))
    answer.append(min(1+len(s_win_nums), 6))
    return answer


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
