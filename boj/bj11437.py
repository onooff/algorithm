n = int(input())
tree = {x:set() for x in range(1,n+1)}
parent_and_depth = {x:[-1,-1] for x in range(1,n+1)}
for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].add(b)
    tree[b].add(a)

chk={1}
q=[1]
nq=list()
parent_and_depth[1][1] = 0
idx=0
d=1
while len(q)>0:
    cur=q[idx]
    idx+=1
    for nxt in tree[cur]:
        if nxt not in chk:
            chk.add(nxt)
            nq.append(nxt)
            parent_and_depth[nxt][0]=cur
            parent_and_depth[nxt][1]=d
    if idx==len(q):
        q=nq
        nq=list()
        d+=1
        idx=0

m=int(input())
for _ in range(m):
    a,b = map(int, input().split())
    # if parent_and_depth[a][1]<parent_and_depth[b][1]:
    #     a,b=b,a
    # while parent_and_depth[a][1]!=parent_and_depth[b][1]:
    #     a = parent_and_depth[a][0]
    while a!=b:
        if parent_and_depth[a][1] > parent_and_depth[b][1]:
            a = parent_and_depth[a][0]
        elif parent_and_depth[a][1] < parent_and_depth[b][1]:
            b = parent_and_depth[b][0]    
        else:
            a = parent_and_depth[a][0]
            b = parent_and_depth[b][0]
        # a = parent_and_depth[a][0]
        # b = parent_and_depth[b][0]
    print("<<",a)
