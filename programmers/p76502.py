def solution(s):
    answer = 0
    for i in range(len(s)):
        stack = list()
        is_ans = True
        for j in range(len(s)):
            c = s[j]
            tmp = ''
            if c == ')':
                if len(stack) == 0 or stack.pop() != '(':
                    is_ans = False
                    break
            elif c == '}':
                if len(stack) == 0 or stack.pop() != '{':
                    is_ans = False
                    break
            elif c == ']':
                if len(stack) == 0 or stack.pop() != '[':
                    is_ans = False
                    break
            else:
                stack.append(c)
        if is_ans and len(stack) == 0:
            answer += 1
        s = s[1:]+s[0]
    return answer


print(solution('('))
