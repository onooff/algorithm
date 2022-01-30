import sys
inputs = sys.stdin.readlines()
maxx = -1
target_words = ["for", "while"]
for i in range(1, len(inputs)):
    cnt = 0
    for tw in target_words:
        cnt += inputs[i].count(tw)
    maxx = max(maxx, cnt)
print(maxx)
