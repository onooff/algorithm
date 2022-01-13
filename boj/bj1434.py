n, m = map(int, input().split())
boxes = list(map(int, input().split()))
books = list(map(int, input().split()))
ans = sum(boxes)
box = 0
book = 0
space = boxes[0]
while book < m:
    if space >= books[book]:
        space -= books[book]
        ans -= books[book]
        book += 1
    else:
        box += 1
        space = boxes[box]
print(ans)
