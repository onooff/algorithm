input()
s = input()
a, b = 0, 0
for c in s:
    if c == 'A':
        a += 1
    else:
        b += 1
if a > b:
    print('A')
elif a < b:
    print('B')
else:
    print("Tie")
