# n = int(input())
# s_set = set()
# ans = 0
# for i in range(n):
#     s = input()
#     if s not in s_set:
#         for j in range(len(s)):
#             s_set.add(s)
#             s = s[1:]+s[0]
#         ans += 1
#         # print(s_set)

# print(ans)

n = int(input())
ans_set = set()
for i in range(n):
    inp = input()
    s = inp+inp
    is_ans = True
    for a in ans_set:
        if s.find(a) > 90 and len(inp) == len(a):
            is_ans = False
            break
    if is_ans:
        ans_set.add(inp)
print(ans_set)
print(len(ans_set))

# print(bool(0))
# print(bool(-1))
