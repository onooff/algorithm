'''
abcdabcabb
'''

# ans = 0
# s = input()
# d = dict()
# for i in range(len(s)):
#     d.setdefault(s[i], set())
#     d[s[i]].add(i)
# for c in d:
#     cnt = 0
#     while len(d[c]) > 1:
#         cnt += 1
#         chk = dict()
#         new_set = set()
#         for i in d[c]:
#             if i+cnt < len(s):
#                 if s[i+cnt] in chk:
#                     if chk[s[i+cnt]] == -1:
#                         new_set.add(i)
#                     else:
#                         new_set.add(chk[s[i+cnt]])
#                         chk[s[i+cnt]] = -1
#                         new_set.add(i)
#                 else:
#                     chk.setdefault(s[i+cnt], i)
#         d[c] = new_set
#     ans = max(ans, cnt)
# print(ans)

# abcabczzabcdxbabcd
ans = 0
ss = input()

for k in range(len(ss)):
    s = ss[k:]
    kmp = [0 for i in range(len(s))]
    j = 0
    for i in range(1, len(s)):
        while j > 0 and s[i] != s[j]:
            j = kmp[j-1]
        if s[i] == s[j]:
            j += 1
            kmp[i] = j
        ans = max(ans, j)
print(ans)
