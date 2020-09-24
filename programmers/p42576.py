# 시간초과 코드
# def solution(participant, completion):
#     for i in range(len(completion)):
#         participant.remove(completion.pop())
#     answer = participant.pop()
#     return answer

# 시간 안초과 코드
def solution(participant, completion):
    d = dict()  # 자바면 맵쓰면 되겠지
    for p in participant:  # 참가자 명단을 키로 쓰고 그 이름이 몇명 있는지 카운트 동명이인 있기 때문
        if d.get(p) != None:
            d[p] += 1
        else:
            d[p] = 1
    for c in completion:  # 완주자 명단 이름을 키로 찾아서 참가자 카운트 하나씩 뺸다
        d[c] -= 1

    for i in d:  # 그러면 완주 못한 한명을 찾을 수 이씀~
        if d[i] == 1:
            return i

    return 0


print(solution(	["leo", "kiki", "eden"], ["eden", "kiki"]))
