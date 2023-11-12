def solution(my_string, queries):
    for q in queries:
        my_string = (
            my_string[: q[0]]
            + my_string[q[1] : q[0] - 1 if (q[0] - 1) >= 0 else None : -1]
            + my_string[q[1] + 1 :]
        )
    return my_string
