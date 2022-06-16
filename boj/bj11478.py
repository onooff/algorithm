s = input()

sub = set()

for i in range(1, len(s)+1):
    for j in range(0, len(s)-i+1, 1):
        sub.add(s[j:j+i])
print(len(sub))
