channel = list()
for i in range(int(input())):
    channel.append(input())

ans = list()
if channel[0] != "KBS1":
    idx = channel.index("KBS1")
    for _ in range(idx):
        ans.append("1")
    for _ in range(idx):
        ans.append("4")
    channel.insert(0, channel.pop(idx))
if channel[1] != "KBS2":
    idx = channel.index("KBS2")
    for _ in range(idx):
        ans.append("1")
    for _ in range(idx - 1):
        ans.append("4")

print("".join(ans))
