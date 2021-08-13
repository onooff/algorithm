n = int(input())
monkeys = dict()
ans = 0
for i in range(n):
    command = input().split()
    name = command[1]
    if command[0] == '1':
        monkeys.setdefault(name, list())
        for j in range(3, len(command)):
            monkeys[name].append(int(command[j]))
        monkeys[name].sort()
        # print(name, monkeys[name])
    else:
        buy = int(command[2])
        if name in monkeys:
            while buy > 0 and len(monkeys[name]) > 0:
                ans += monkeys[name].pop()
                buy -= 1
print(ans)
