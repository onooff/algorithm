import sys

inputs = sys.stdin.readlines()
inputs.pop()

answer = list()
for board in inputs:
    board = board.rstrip()

    v = [
        set(),
        set(),
        set(),
    ]
    h = [
        set(),
        set(),
        set(),
    ]
    cnt = {"O": 0, "X": 0, ".": 0}
    for i in range(9):
        c = board[i]
        cnt[c] += 1
        v[i % 3].add(c)
        h[i // 3].add(c)
    x = [{board[0], board[4], board[8]}, {board[2], board[4], board[6]}]
    winner = set()
    for t in [v, h, x]:
        for i in range(len(t)):
            c = t[i].pop()
            if c != "." and len(t[i]) == 0:
                t[i] = c
                winner.add(c)
            else:
                t[i] = None
    # print(cnt, v, h, x)
    if (
        len(winner) > 1
        or (len(winner) == 0 and cnt["."] > 0)
        or cnt["X"] > 5
        or cnt["O"] > 4
        or cnt["X"] - cnt["O"] not in (0, 1)
        or ("O" in winner and cnt["X"] > cnt["O"])
        or ("X" in winner and cnt["X"] == cnt["O"])
    ):
        answer.append("invalid")
    else:
        answer.append("valid")

print("\n".join(answer))
