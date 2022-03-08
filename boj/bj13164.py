n, k = map(int, input().split())
l = list(map(int, input().split()))
gap = list()
for i in range(n-1):
    gap.append(l[i+1]-l[i])
gap.sort(key=lambda x: -x)
print(gap)
print(l[-1]-l[0]-sum(gap[:k-1]))
