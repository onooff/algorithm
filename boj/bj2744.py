s = input()
for c in s:
    if c.isupper():
        print(c.lower(), end='')
    else:
        print(c.upper(), end='')

# 아스키 풀이
# for c in s:
#     c = ord(c)
#     if c >= 97:
#         print(chr(c-32), end='')
#     else:
#         print(chr(c+32), end='')
