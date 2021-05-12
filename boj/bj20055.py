n, k = map(int, input().split())
belt = list(map(int, input().split()))
for i in belt:
    if i == 0:
        k -= 1
robots = list()
robots_set = set()
end = n-2
n2 = n*2
cnt = 0
while k > 0:
    cnt += 1
    start = (end-n+1) % n2
    nr = list()
    while len(robots) > 0:
        tmp = robots.pop(0)
        robots_set.discard(tmp)
        if tmp == end:
            continue
        next_b = (tmp+1) % n2
        if next_b not in robots_set:
            if belt[next_b] == 0:
                nr.append(tmp)
                robots_set.add(tmp)
            else:
                belt[next_b] -= 1
                if belt[next_b] == 0:
                    k -= 1
                if next_b != end:
                    nr.append(next_b)
                    robots_set.add(next_b)
        else:
            nr.append(tmp)
            robots_set.add(tmp)

    robots = nr
    if belt[start] > 0:
        belt[start] -= 1
        robots.append(start)
        robots_set.add(start)
        if belt[start] == 0:
            k -= 1
    # print(start, end, robots, k, belt)
    end = (end-1) % n2
print(cnt)
