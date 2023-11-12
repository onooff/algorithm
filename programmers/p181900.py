def solution(my_string, indices):
    l = list(my_string)
    for i in indices:
        l[i] = ""
    return "".join(l)
