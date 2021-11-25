s = input()
cnt = [0, 0]
idx = 0
for i in range(2):
    for _ in range(len(s)//2):
        cnt[i] += int(s[idx])
        idx += 1
if cnt[0] == cnt[1]:
    print("LUCKY")
else:
    print("READY")
