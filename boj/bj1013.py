import re

regex = "((100+1+)|(01))+"
r = re.compile(regex)
t = int(input())
for _ in range(t):
    s = input()
    if r.fullmatch(s):
        print("YES")
    else:
        print("NO")
