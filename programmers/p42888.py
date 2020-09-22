def solution(record):

    answer = []
    user = {}
    log = []

    for r in record:
        index = r.find(" ")
        next_index = r.find(" ", index+1)
        uid = r[index+1:next_index]

        if r[0] == "E":  # 들어왔슴다
            nickname = r[next_index+1:]
            log.append((uid, "님이 들어왔습니다."))
            user[uid] = nickname
        elif r[0] == "L":  # 나갔슴다
            uid = r[index+1:]
            log.append((uid, "님이 나갔습니다."))
        else:  # r[0] == "C" 이름바꿧슴
            nickname = r[next_index+1:]
            user[uid] = nickname

    for l in log:
        answer.append(user[l[0]]+l[1])
        # print(l[0], l[1])

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
                "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
