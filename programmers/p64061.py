# 크레인 인형뽑기 게임 https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0  # 답(사라진 인형 수) 저장할 변수
    stack = list()  # 뽑은 인형을 넣는 스택처럼 활용할 리스트
    for pick in moves:  # moves에서 인형을 뽑을 위치를 하나씩 가져오면서 반복한다
        pick = pick-1  # moves는 1부터 시작하는 인덱스이므로 -1 해서 0부터 시작하는 인덱스로 만듬
        for i in range(len(board)):  # 인형크레인이 내려가는 모습 반복문으로 표현 각 높이에서 인형이 존재하는지 확인
            if board[i][pick] != 0:  # 인형이 있으면
                stack.append(board[i][pick])  # 그 인형을 스택에 넣어주고
                board[i][pick] = 0  # 인형이 있던 board 좌표에 0 넣어줘서 인형 없어짐 표현
                # print(stack)

                # 최근 넣은 두 인형이 같은 인형이면
                if (len(stack) >= 2) & (stack[len(stack)-1] == stack[len(stack)-2]):
                    stack.pop()
                    stack.pop()  # 인형 두개를 스택에서 제거하고
                    answer += 2  # 제거된 인형수를 answer에 더해줌
                break  # 인형이 발견된 후 하는 모든 동작을 수행했으므로 다음 pick으로

    return answer  # 답 리턴


print(solution(	[[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [
      4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]))
