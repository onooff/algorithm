s = {str(i) for i in range(1, 31)}
for _ in range(28):
    s.discard(input())
ans = sorted(list(s), key=lambda x: int(x))
print("\n".join(ans))
