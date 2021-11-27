n = int(input())
for _ in range(n):
    a, b = input().split()
    aa = {c: a.count(c) for c in a}
    bb = {c: b.count(c) for c in b}
    if aa == bb:
        print(a, '&', b, "are anagrams.")
    else:
        print(a, '&', b, "are NOT anagrams.")
