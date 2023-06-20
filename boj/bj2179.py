n = int(input())
word_idx_dict = dict()

for i in range(n):
    w = input()
    if w not in word_idx_dict:
        word_idx_dict[w] = i

words = sorted(list(word_idx_dict.keys()))

max_match = -1
ans_dict = dict()
for i in range(len(words)-1):
    a = words[i]
    b = words[i+1]
    if word_idx_dict[a] > word_idx_dict[b]:
        a, b = b, a
    minlen = min(len(a), len(b))
    cnt = 0
    for j in range(minlen):
        if a[j] != b[j]:
            break
        cnt += 1

    if cnt > max_match:
        max_match = cnt
        ans_dict = dict()

    if cnt == max_match:
        p = a[:cnt]
        ans_dict.setdefault(p, set())
        ans_dict[p].add(word_idx_dict[a])
        ans_dict[p].add(word_idx_dict[b])

ans = list()
for k in ans_dict:
    tmp = sorted(list(ans_dict[k]))
    ans.append((tmp[0], tmp[1]))
ans.sort()

idx_word_dict = {word_idx_dict[w]: w for w in word_idx_dict}
print(idx_word_dict[ans[0][0]])
print(idx_word_dict[ans[0][1]])
