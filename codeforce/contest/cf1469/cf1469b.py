t = int(input())

for tc in range(t):
    len_a = int(input())
    a = list(map(int, input().split()))
    len_b = int(input())
    b = list(map(int, input().split()))
    max_a = 0
    max_b = 0
    sum_n = 0
    for n in a:
        sum_n += n
        max_a = max(max_a, sum_n)
    sum_n = 0
    for n in b:
        sum_n += n
        max_b = max(max_b, sum_n)
    print(max_a+max_b)
