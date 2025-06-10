n = int(input())
weight = 0
value = 0
for _ in range(n):
    t, w, h, l = input().split()
    w, h, l = int(w), int(h), int(l)
    if t == "B":
        weight += 6000
        continue
    # t=="A"
    weight += 1000
    v = (w // 12) * (h // 12) * (l // 12)
    weight += v * 500
    value += v * 4000
print(weight)
print(value)
