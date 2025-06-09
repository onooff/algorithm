n = int(input())
opt_short = dict()
short_opt = dict()

for _ in range(n):
    opt = input()
    opt_short.setdefault(opt, None)
    lower_opt = opt.lower()

    for i in range(len(lower_opt)):
        if i == 0 or lower_opt[i - 1] == " ":
            if lower_opt[i] != " " and lower_opt[i] not in short_opt:
                short_opt.setdefault(lower_opt[i], opt)
                opt_short[opt] = i
                break

    if opt_short[opt] == None:
        for i in range(len(lower_opt)):
            if lower_opt[i] != " " and lower_opt[i] not in short_opt:
                short_opt.setdefault(lower_opt[i], opt)
                opt_short[opt] = i
                break

    for i in range(len(opt)):
        if i == opt_short[opt]:
            print(f"[{opt[i]}]", end="")
        else:
            print(opt[i], end="")
    print()
