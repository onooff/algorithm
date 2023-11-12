def solution(my_string, m, c):
    return "".join([my_string[m * i + c - 1] for i in range(len(my_string) // m)])
