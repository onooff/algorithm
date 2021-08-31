'''
3
2 B A
4 A B C D
2 A C
'''
import sys
input = sys.stdin.readline

bar = ['', '--', '----', '------', '--------', '----------', '------------', '--------------', '----------------', '------------------', '--------------------',
       '----------------------', '------------------------', '--------------------------', '----------------------------', '------------------------------']

n = int(input())
sl = list()
for _ in range(n):
    sl.append(list(input().split())[1:])
sl.sort()

last = list()
for i in range(len(sl)):
    flag = True
    for j in range(len(sl[i])):
        if flag and j < len(last) and last[j] == sl[i][j]:
            continue
        flag = False
        print(bar[j], sl[i][j], sep='')
    last = sl[i]
