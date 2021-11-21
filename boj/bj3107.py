'''
1:2:3:4:5:6:7::
0001:0002:0003:0004:0005:0006:0007:0000
'''

s = input()
cnt = s.count(':')
if cnt != 7:
    idx = s.index('::')
    s = s[:idx]+(':'*(7-cnt+2))+s[idx+2:]
s = s.split(':')
for i in range(len(s)):
    s[i] = '0'*(4-len(s[i]))+s[i]
print(':'.join(s))
