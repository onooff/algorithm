import copy

t = int(input())
for tc in range(t):
    n, k = map(int, input().split())
    time = list(map(int, input().split()))
    time.insert(0, 0)
    g1 = {}  # key를 지으려면 v들이 필요
    g2 = {}  # key를 지으면 v들을 지을 수 있음
    for i in range(k):
        tmp = tuple(map(int, input().split()))
        if not g1.get(tmp[1]):
            g1[tmp[1]] = list()
        if not g2.get(tmp[0]):
            g2[tmp[0]] = list()
        g1[tmp[1]].append(tmp[0])
        g2[tmp[0]].append(tmp[1])
    end = int(input())
    g = copy.deepcopy(g1)

    ans = 0

    go = list()
    find = [-1]*(n+1)
    for i in range(1, n+1):
        if i not in g.keys():
            find[i] = time[i]
            go.append(i)

    while len(go) > 0:
        tmp = go.pop(0)  # tmp는 지어진 건물 번호
        if tmp in g2.keys():
            for i in g2[tmp]:  # tmp를 지으면 지을 수 있는 건물들 i에 대해서
                g1[i].remove(tmp)  # i를 지을 때 tmp가 필요하다는 정보를 삭제해준다 왜냐면 지었으니까
                if len(g1[i]) == 0:  # 그리고 i를 지을때 필요한 건물이 더이상 없다면 당장 지을 수 있기 때문에
                    go.append(i)  # i를 지은것으로 처리
                    m = 0
                    for j in g[i]:  # i를 짓는데 필요한 j들 중
                        m = max(m, find[j])  # 가장 오래걸린 거 + 자기자신 짓는 시간이 최종걸린시간
                    find[i] = m+time[i]
        # print(find)

    print(find[end])
    # print('ans=', find[end])
