import sys
inputs = sys.stdin.readlines()

n, m = map(int, inputs[0].rstrip().split())
royal = inputs[1].rstrip()
children = dict()
blood = dict()
parents = dict()
for i in range(2, n+2):
    child, p1, p2 = inputs[i].rstrip().split()
    children.setdefault(p1, set())
    children.setdefault(p2, set())
    children.setdefault(child, set())
    blood.setdefault(p1, 0)
    blood.setdefault(p2, 0)
    blood.setdefault(child, 0)
    parents.setdefault(child, {p1: p2, p2: p1})
    children[p1].add(child)
    children[p2].add(child)
blood[royal] = 100

q = [royal]
idx = 0
while idx < len(q):
    cur = q[idx]
    idx += 1
    for child in children[cur]:
        blood[child] = (blood[cur]+blood[parents[child][cur]])/2
        q.append(child)

best_royal_blood = -1
next_throne_owner = "who?"

for i in range(n+2, n+m+2):
    challenger = inputs[i].rstrip()
    blood_chk = 0
    if challenger in blood:
        blood_chk = blood[challenger]
    if best_royal_blood < blood_chk:
        best_royal_blood = blood_chk
        next_throne_owner = challenger
print(next_throne_owner)
