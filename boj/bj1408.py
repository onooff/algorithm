now = list(map(int, input().split(':')))
end = list(map(int, input().split(':')))
now = now[2]+now[1]*60+now[0]*60*60
end = end[2]+end[1]*60+end[0]*60*60

if end < now:
    end += 24*60*60

ans = end-now
s = ans % 60
ans //= 60
m = ans % 60
ans //= 60
h = ans % 60

print(f"{h:02}:{m:02}:{s:02}")
