'''
black	0	1
brown	1	10
red	2	100
orange	3	1000
yellow	4	10000
green	5	100000
blue	6	1000000
violet	7	10000000
grey	8	100000000
white	9	1000000000
'''
c = [
    ["black", 0, 1],
    ["brown", 1, 10],
    ["red", 2, 100],
    ["orange", 3, 1000],
    ["yellow", 4, 10000],
    ["green", 5, 100000],
    ["blue", 6, 1000000],
    ["violet", 7, 10000000],
    ["grey", 8, 100000000],
    ["white", 9, 1000000000],
]
d = dict()
for color in c:
    d.setdefault(color[0], (color[1], color[2]))
c1 = input()
c2 = input()
c3 = input()
print(((d[c1][0]*10)+d[c2][0])*d[c3][1])
