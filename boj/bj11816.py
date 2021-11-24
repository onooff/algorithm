s = input()
d = 10
if s[:2] == "0x":
    d = 16
    s = s[2:]
elif s[0] == '0':
    d = 8
    s = s[1:]
print(int(s, d))
