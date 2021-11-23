s = input()
for c in s:
    code = ord(c)-3
    if code < 65:
        code += 26
    print(chr(code), end='')
