def solution(new_id):

    new_id = new_id.lower()  # 1단계
    print("1--> "+new_id)

    for c in new_id:  # 2단계
        if not(c.isalpha() or c.isdigit() or (c == '-') or (c == '_') or (c == '.')):
            new_id = new_id.replace(c, "")
    print("2--> "+new_id)

    flag = True  # 3단계
    while flag:
        flag = False
        if new_id.find("..") >= 0:
            new_id = new_id.replace("..", ".")
            flag = True
    print("3--> "+new_id)

    if new_id != "" and new_id[0] == '.':  # 4단계
        new_id = new_id[1:]
    if new_id != "" and new_id[len(new_id)-1] == '.':
        new_id = new_id[:len(new_id)-1]
    print("4--> "+new_id)

    if new_id == "":  # 5단계
        new_id = "a"
    print("5--> "+new_id)

    new_id = new_id[:15]  # 6단계
    if new_id != "" and new_id[len(new_id)-1] == '.':
        new_id = new_id[:len(new_id)-1]
    print("6--> "+new_id)

    while len(new_id) < 3:  # 7단계
        new_id += new_id[len(new_id)-1]
    print("7--> "+new_id)

    answer = new_id
    return answer


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
