t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a_dict = dict()
b_dict = dict()

for i in range(n):
    sum_a = 0
    for j in range(i, n):
        sum_a += a[j]
        if sum_a not in a_dict.keys():
            a_dict.setdefault(sum_a, 0)
        a_dict[sum_a] += 1

for i in range(m):
    sum_b = 0
    for j in range(i, m):
        sum_b += b[j]
        if sum_b not in b_dict.keys():
            b_dict.setdefault(sum_b, 0)
        b_dict[sum_b] += 1

ans = 0
keys = list(a_dict.keys())
find = set(b_dict.keys())
keys.sort()

for k in keys:
    # if k > t:
    #     break
    if t-k in find:
        ans += a_dict[k]*b_dict[t-k]
        # a_dict.pop(k)
        # b_dict.pop(t-k)

# keys = list(b_dict.keys())
# find = set(a_dict.keys())
# keys.sort()

# for k in keys:
#     if k > t:
#         break
#     if t-k in find:
#         ans += b_dict[k]*a_dict[t-k]
#         b_dict.pop(k)
#         a_dict.pop(t-k)

print(ans)

# print(a_dict)
# print(b_dict)
