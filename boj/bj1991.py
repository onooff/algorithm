import sys

inputs = sys.stdin.readlines()
graph = dict()
for line in inputs[1:]:
    cur, left, right = line.split()
    graph.setdefault(cur, (left, right))

# for k in graph:
#     print(k, graph[k])


def go_pre(graph, cur, o):
    if cur == ".":
        return
    o.append(cur)
    go_pre(graph, graph[cur][0], o)
    go_pre(graph, graph[cur][1], o)


def go_in(graph, cur, o):
    if cur == ".":
        return
    go_in(graph, graph[cur][0], o)
    o.append(cur)
    go_in(graph, graph[cur][1], o)


def go_post(graph, cur, o):
    if cur == ".":
        return

    go_post(graph, graph[cur][0], o)
    go_post(graph, graph[cur][1], o)
    o.append(cur)


preo = []
ino = []
posto = []
go_pre(graph, "A", preo)
go_in(graph, "A", ino)
go_post(graph, "A", posto)

print("".join(preo))
print("".join(ino))
print("".join(posto))
