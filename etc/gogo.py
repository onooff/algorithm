answer = 0


def solution(depar, hub, dest, roads):
    global answer
    answer = 0
    loadMap = dict()
    for road in roads:
        if loadMap.get(road[0]) == None:
            loadMap[road[0]] = list()
            loadMap[road[0]].append(road[1])
        else:
            loadMap[road[0]].append(road[1])
    go(depar, hub, dest, loadMap, list())
    return answer


def go(now, hub, dest, loadMap, course):
    global answer
    course.append(now)
    # print(course)
    if not loadMap.get(now):
        if (hub in course) and (dest in course):
            answer += 1
        course.pop()
        return
    for next in loadMap[now]:
        go(next, hub, dest, loadMap, course)
    course.pop()


print(solution("SEOUL", "DAEGU", "YEOSU", [["ULSAN", "BUSAN"], ["DAEJEON", "ULSAN"], ["DAEJEON", "GWANGJU"], ["SEOUL", "DAEJEON"], ["SEOUL", "ULSAN"], [
      "DAEJEON", "DAEGU"], ["GWANGJU", "BUSAN"], ["DAEGU", "GWANGJU"], ["DAEGU", "BUSAN"], ["ULSAN", "DAEGU"], ["GWANGJU", "YEOSU"], ["BUSAN", "YEOSU"]]))
print(solution("ULSAN", "SEOUL",   "BUSAN", [["SEOUL", "DAEJEON"], ["ULSAN", "BUSAN"], ["DAEJEON", "ULSAN"], [
      "DAEJEON", "GWANGJU"], ["SEOUL", "ULSAN"], ["DAEJEON", "BUSAN"], ["GWANGJU", "BUSAN"]]))
