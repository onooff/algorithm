def solution(enter, leave):
    answer = [set() for i in range(len(enter))]
    room = set()
    for e in enter:
        room.add(e)
        for mem in room:
            answer[mem-1].add(e)
            answer[e-1].add(mem)
        while len(leave) > 0 and leave[0] in room:
            l = leave.pop(0)
            room.discard(l)
    return list(map(lambda x: len(x)-1, answer))
