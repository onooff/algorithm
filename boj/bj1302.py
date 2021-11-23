n = int(input())
d = dict()

for i in range(n):
    book = input()
    d.setdefault(book, 0)
    d[book] += 1

answer = list(d.keys())
answer.sort(key=lambda x: (-d[x], x))
print(answer[0])
