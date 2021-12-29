import sys

input = sys.stdin.readline

t_nums = list()
num = 1
d = 2
while num <= 1000:
    t_nums.append(num)
    num += d
    d += 1

answers = set()
for a in range(len(t_nums)):
    for b in range(a, len(t_nums)):
        for c in range(b, len(t_nums)):
            summ = t_nums[a] + t_nums[b] + t_nums[c]
            if summ > 1000:
                break
            answers.add(summ)

t = int(input())
for _ in range(t):
    if int(input()) in answers:
        print(1)
    else:
        print(0)
