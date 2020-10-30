# 어렵구만..
# (부위별 옷 수+1)끼리 전부 곱하고 -1
# +1은 그 부위에 옷을 입지 않는 경우의 수, -1은 아무것도 입지 않은 경우의 수

def solution(clothes):
    answer = 1
    d = dict()
    for c in clothes:
        if not d.get(c[1]):
            d[c[1]] = list()
            d[c[1]].append(c[0])
        else:
            d[c[1]].append(c[0])
    for k in d:
        answer *= len(d[k])+1

    return answer-1


print(solution(	[["yellow_hat", "headgear"], [
      "blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
