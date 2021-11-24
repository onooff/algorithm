s = input()
joi = 0
ioi = 0
for i in range(len(s)-2):
    chk = s[i:i+3]
    if chk == "JOI":
        joi += 1
    elif chk == "IOI":
        ioi += 1
print(joi)
print(ioi)
