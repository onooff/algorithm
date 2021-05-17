def solution(numbers):
    answer = []
    for n in numbers:
        bn = list(str(bin(n))[2:])
        is_answer = False
        for i in range(len(bn)-1, -1, -1):
            if bn[i] == '0':
                bn[i] = '1'
                if i != len(bn)-1:
                    bn[i+1] = '0'
                is_answer = True
                break
        if not is_answer:
            bn.insert(0, '1')
            bn[1] = '0'
        answer.append(int(''.join(bn), 2))
    return answer


print(solution([2, 7]))
