from itertools import combinations


def solution(numbers):
    # answer = []
    # print(type(answer))
    answer = set()  # 중복이 없는 형태로 답이 리턴되어야 하므로 answer를 set으로 선언
    comb = list(combinations(numbers, 2))  # numbers의 원소를 2개씩 골라낸 조합 생성
    for nums in comb:  # 각 조합에 대해서
        answer.add(sum(nums))  # 합을 구해서 answer에 넣는다. set이기 때문에 중복 제거됨
    answer = list(answer)  # answer를 정렬하기 위해 list로 변환
    answer.sort()  # answer 정렬
    return answer  # answer 리턴


print(solution(	[2, 1, 3, 4, 1]))
