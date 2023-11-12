def solution(my_string):
    chars = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
    d = {c: 0 for c in chars}
    for c in my_string:
        d[c] += 1
    return [d[c] for c in chars]
