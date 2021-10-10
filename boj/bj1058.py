'''
3
NYY
YNY
YYN
'''

import sys
inputs = sys.stdin.readlines()
graph = dict()
n = int(inputs[0])
for i in range(n):
    graph.setdefault(i, set())
    for j in range(len(inputs[i+1])):
        c = inputs[i+1][j]
        if c == 'Y':
            graph[i].add(j)
# print(graph)

ans = -1
for i in range(n):
    tf = set()
    tf = tf | graph[i]
    for f in graph[i]:
        tf = tf | graph[f]
    tf.discard(i)
    ans = max(ans, len(tf))
    # print(tf)

print(ans)
