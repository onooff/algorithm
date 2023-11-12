def solution(q, r, code):
    return "".join(
        [
            code[i * q + r] if (i * q + r) < len(code) else ""
            for i in range(len(code) // q + 1)
        ]
    )
