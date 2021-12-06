convert = {
    "000": '0',
    "001": '1',
    "010": '2',
    "011": '3',
    "100": '4',
    "101": '5',
    "110": '6',
    "111": '7'
}

s = list(input())
for _ in range((3-len(s) % 3) % 3):
    s.insert(0, '0')
ans = list()
for i in range(0, len(s), 3):
    ans.append(convert[''.join(s[i:i+3])])

print(int(''.join(ans)))
