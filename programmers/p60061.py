def check(building):
    for b in building:
        if b[2] == 0:  # 기둥
            if (b[1] == 0) or ([b[0], b[1]-1, 0] in building) or ([b[0], b[1], 1] in building) or ([b[0]-1, b[1], 1] in building):
                continue
            else:
                print([b[0], b[1], b[2]], "기둥 문제")
                return False
        else:  # b[2] == 1 보
            if ([b[0], b[1]-1, 0] in building) or ([b[0]+1, b[1]-1, 0] in building) or (([b[0]-1, b[1], 1] in building) and ([b[0]+1, b[1], 1] in building)):
                continue
            else:
                print([b[0], b[1], b[2]], "보 문제")
                return False
    return True


def solution(n, build_frame):
    answer = []

    for build in build_frame:
        flag = False
        # if build[3] == 1:
        #     answer.append([build[0], build[1], build[2]])
        # else:
        #     answer.remove([build[0], build[1], build[2]])

        if build[3] == 1:  # 짓기
            if build[2] == 0:  # 기둥
                if (build[1] == 0) or ([build[0], build[1]-1, 0] in answer) or ([build[0], build[1], 1] in answer) or ([build[0]-1, build[1], 1] in answer):
                    flag = True
            else:  # build[2] == 1 보
                if ([build[0], build[1]-1, 0] in answer) or ([build[0]+1, build[1]-1, 0] in answer) or (([build[0]-1, build[1], 1] in answer) and ([build[0]+1, build[1], 1] in answer)):
                    flag = True
            if flag:
                answer.append([build[0], build[1], build[2]])

        else:  # build[3] == 0 뿌수기
            answer.remove([build[0], build[1], build[2]])
            if not check(answer):
                print([build[0], build[1], build[2]], "는 뿌수면안됨")
                answer.append([build[0], build[1], build[2]])

    answer.sort()

    return answer


print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [
      5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [
      1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))


'''
기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.

'''
