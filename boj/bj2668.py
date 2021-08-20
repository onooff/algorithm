'''
7
3
1
1
5
5
4
6
'''

n = int(input())
nums = [-1]
num_set = set()
for i in range(n):
    nums.append(int(input()))
    num_set.add(nums[i+1])
ans = []
chk = [False for i in range(n+1)]
for i in range(1, n+1):
    if not chk[i]:
        val_set = {nums[i]}
        idx_set = {i}
        nxt = nums[i]
        while nxt not in idx_set:
            val_set.add(nums[nxt])
            idx_set.add(nxt)
            nxt = nums[nxt]
        if idx_set == val_set:
            for idx in idx_set:
                chk[idx] = True
            ans.append(i)
    else:
        ans.append(i)
print(len(ans))
for a in ans:
    print(a)
