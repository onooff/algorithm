def solution(queue1, queue2):
    if (sum(queue1)+sum(queue2)) % 2 == 1:
        return -1
    q = queue1+queue2
    head = 0
    tail = len(queue1)
    summ = sum(queue1)
    n = sum(q)//2
    answer = 0
    while summ != n:
        if summ > n:
            summ -= q[head]
            head = next(head, len(q))
            if head==0:
                return -1
        elif summ < n:
            summ += q[tail]
            tail = next(tail, len(q))
            if tail==len(queue1):
                return -1
        answer += 1
    return answer


def next(cur, l):
    return (cur+1) % l


print('>>>', solution(	[11], [13]))
