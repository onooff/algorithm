def solution(sizes):
    l = list()
    s = list()
    for size in sizes:
        if size[0] > size[1]:
            l.append(size[0])
            s.append(size[1])
        else:
            l.append(size[1])
            s.append(size[0])
    return max(l)*max(s)
