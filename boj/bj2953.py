maxx_num = -1
maxx = -1
for i in range(1, 6):
    cur_summ = sum(map(int, input().split()))
    if maxx < cur_summ:
        maxx_num = i
        maxx = cur_summ
print(f"{maxx_num} {maxx}")
