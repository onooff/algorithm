def solution(files):
    answer = []
    file = ""
    new_files = list()
    for file in files:
        ds = 0
        head = ""
        number = 0
        now_digit = False
        for i in range(len(file)+1):
            if i == len(file):
                number = int(file[ds:i])
                break

            if not now_digit and str.isdigit(file[i]):
                head = file[:i]
                ds = i
                now_digit = True
            elif now_digit and not str.isdigit(file[i]):
                number = int(file[ds:i])
                break
        new_files.append((head, number, file))

    new_files.sort(key=lambda x: (str.lower(x[0]), x[1]))
    # print(new_files)

    for f in new_files:
        answer.append(f[2])

    return answer


# print(solution(["img12.png", "img10.png", "img02.png",
#                 "img1.png", "IMG01.GIF", "img2.JPG"]))
# print(["img1.png", "IMG01.GIF", "img02.png",
#        "img2.JPG", "img10.png", "img12.png"])
# print(solution(	["F-5 Freedom Fighter", "B-50 Superfortress",
#                  "A-10 Thunderbolt II", "F-14 Tomcat"]))


# test = ['a', 'a', 'A', 'a', 'a', 'A', 'a', 'a', 'a', 'A']
# test.sort(key=str.lower)
# print(test)
