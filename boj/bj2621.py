import sys

inputs = sys.stdin.readlines()

color_idx = {"R": 0, "B": 1, "Y": 2, "G": 3}
color_cnt = [0 for i in range(4)]
num_cnt = [0 for i in range(10)]
nums = []

for inp in inputs:
    color, num = inp.split()
    num = int(num)
    nums.append(num)
    color = color_idx[color]
    color_cnt[color] += 1
    num_cnt[num] += 1
nums.sort()

is_straight = False
cnt = 5
for i in range(len(num_cnt)):
    if num_cnt[i] != 1 and cnt != 5:
        break
    elif num_cnt[i] == 1:
        cnt -= 1
        if cnt == 0:
            is_straight = True
            break

p = 0
if 5 in color_cnt and is_straight:
    p = 900 + max(nums)
elif max(num_cnt) >= 4:
    p = 800 + num_cnt.index(max(num_cnt))
elif 3 in num_cnt and 2 in num_cnt:
    p = 700 + (num_cnt.index(3) * 10) + num_cnt.index(2)
elif 5 in color_cnt:
    p = 600 + max(nums)
elif is_straight:
    p = 500 + max(nums)
elif 3 in num_cnt:
    p = 400 + num_cnt.index(3)
elif num_cnt.count(2) == 2:
    p += 300
    d = 1
    for i in range(len(num_cnt)):
        if num_cnt[i] == 2:
            p += i * d
            d *= 10
elif 2 in num_cnt:
    p = 200 + num_cnt.index(2)
else:
    p = 100 + max(nums)

print(p)
