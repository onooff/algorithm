s = input()
ucpc = ['U', 'C', 'P', 'C']
cur = 0
answer = "I hate UCPC"
for c in s:
    if c == ucpc[cur]:
        cur += 1
        if cur >= 4:
            answer = "I love UCPC"
            break
print(answer)
