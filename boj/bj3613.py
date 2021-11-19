# 정규식 풀이 생각해보기
s = input()
snake = False
camel = False
is_error = False
if s[0].isupper() or s[0] == '_' or s[-1] == "_":
    is_error = True
else:
    for c in s:
        if c.isupper():
            camel = True
        if c == '_':
            if last:
                is_error = True
                break
            else:
                snake = True
                last = True
        else:
            last = False

        if snake and camel:
            is_error = True
            break

if is_error:
    print("Error!")
else:
    if snake:
        up = False
        for c in s:
            if c == '_':
                up = True
            else:
                if up:
                    print(c.upper(), end='')
                    up = False
                else:
                    print(c, end='')
    else:
        for c in s:
            if c.isupper():
                print('_', end='')
                print(c.lower(), end='')
            else:
                print(c, end='')
