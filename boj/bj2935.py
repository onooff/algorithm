a, op, b = input(), input(), input()
if op == '*':
    print('1'+a[1:]+b[1:])
else:
    if len(a) != len(b):
        if len(a) < len(b):
            a, b = b, a
        a = a[:-len(b)]+b
    else:
        a = '2'+a[1:]
    print(a)
