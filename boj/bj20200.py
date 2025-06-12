n = int(input())
s = input()

pos = 0
maxx = 1
minn = 0
if s[0] == "-":
    maxx = 0
    minn = -1
for c in s:
    if c == "+":
        pos += 1
        maxx = max(maxx, pos)
    elif c == "-":
        pos -= 1
        minn = min(minn, pos)
    elif c == "=":
        maxx = max(maxx, pos + 1)

board = [["." for _ in range(n)] for _ in range(abs(maxx - minn))]
y = maxx - 1
x = 0
for c in s:
    if c == "+":
        board[y][x] = "/"
        y -= 1
    if c == "-":
        y += 1
        board[y][x] = "\\"
    if c == "=":
        board[y][x] = "_"
    x += 1

for b in board:
    print("".join(b))
