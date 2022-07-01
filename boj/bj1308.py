import datetime
start = list(map(int, input().split()))
end = list(map(int, input().split()))
ans = 'gg'
if end[0]-start[0] > 1000:
    pass
elif end[0]-start[0] == 1000 and end[1] > start[1]:
    pass
elif end[0]-start[0] == 1000 and end[1] == start[1] and end[2] >= start[2]:
    pass
else:
    ans = 'D-'+str((datetime.date(end[0], end[1], end[2]) -
                    datetime.date(start[0], start[1], start[2])).days)
print(ans)
