a, b = input(), input()
b = list(b)
is_revered = False
ans = 0
while len(b) > len(a):
    if is_revered:
        if b[0] == 'B':
            is_revered = not is_revered
        b = b[1:]
    else:
        if b[-1] == 'B':
            is_revered = not is_revered
        b = b[:-1]
if is_revered:
    b.reverse()
if a == ''.join(b):
    print(1)
else:
    print(0)
