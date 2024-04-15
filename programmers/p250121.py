def solution(data, ext, val_ext, sort_by):
    answer = []
    di = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    ext = di[ext]
    sort_by = di[sort_by]
    for d in data:
        if d[ext] < val_ext:
            answer.append(d)
    answer.sort(key=lambda x: x[sort_by])
    return answer
