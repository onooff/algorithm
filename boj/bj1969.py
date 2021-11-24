import sys
inputs = sys.stdin.readlines()

ans_s = ""
ans_val = 0
for j in range(len(inputs[1])-1):
    d = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    # 파이썬 3.7 부터 dict 순서 보장
    for i in range(1, len(inputs)):
        d[inputs[i][j]] += 1
    maxx = -1
    max_key = None
    summ = 0
    for k in d:
        if maxx < d[k]:
            maxx = d[k]
            max_key = k
        summ += d[k]
    ans_s += max_key
    ans_val += summ-d[max_key]
print(ans_s, ans_val, sep='\n')
