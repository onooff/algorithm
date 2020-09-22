def reverse(text):
    if len(text) <= 1:
        return text

    return reverse(text[1:]) + text[0]


def solution(m, n, board):
    answer = 0
    flag = True
    nBoard = [""]*n
    remove = set()

    for j in range(0, n):
        for i in range(0, m):
            # print(board[j][i])
            nBoard[j] += board[i][j]
        nBoard[j] = reverse(nBoard[j])

    # print(nBoard)

    while flag:
        flag = False
        for i in range(0, len(nBoard)-1):
            for j in range(0, len(nBoard[i])-1):
                if len(nBoard[i+1]) >= j+2:
                    if nBoard[i][j] == nBoard[i][j+1] == nBoard[i+1][j] == nBoard[i+1][j+1]:
                        flag = True
                        remove.add((i, j))
                        remove.add((i, j+1))
                        remove.add((i+1, j))
                        remove.add((i+1, j+1))
        for i in range(0, len(nBoard)):
            for j in range(len(nBoard[i])-1, -1, -1):
                if (i, j) in remove:
                    remove.remove((i, j))
                    nBoard[i] = nBoard[i][:j]+nBoard[i][j+1:]
                    answer += 1
        # print(nBoard, answer)

    return answer


# print(solution(4, 5, ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']))
print(solution(6, 6, ["TTTANT", "RRFACC",
                      "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))


'''

CCBDE
AAADE
AAABF
CCBBF

'''
