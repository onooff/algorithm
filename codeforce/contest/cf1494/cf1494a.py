t = int(input())

for tc in range(t):
    s = input()
    is_yes = False
    for a in ['(', ')']:
        for b in ['(', ')']:
            for c in ['(', ')']:
                if (a == b == c) or is_yes:
                    continue
                stack = list()
                is_not_answer = False
                for ch in s:
                    ccc = ''
                    if ch == 'A':
                        ccc = a
                    elif ch == 'B':
                        ccc = b
                    elif ch == 'C':
                        ccc = c
                    # print(ccc, end='')
                    if ccc == '(':
                        stack.append(ccc)
                    elif ccc == ')':
                        if len(stack) == 0 or stack[len(stack)-1] != '(':
                            is_not_answer = True
                            break
                        else:
                            stack.pop()
                    # print()
                if len(stack) == 0 and not is_not_answer:
                    is_yes = True
    if is_yes:
        print('yes')
    else:
        print('no')
