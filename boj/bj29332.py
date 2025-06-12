import sys

inputs = sys.stdin.readlines()
inputs = inputs[1:]

dd = {"L": None, "R": None, "U": None, "D": None}
for line in inputs:
    x, y, d = line.split()
    x, y = int(x), int(y)
    if d == "L":
        dd[d] = x if dd[d] == None else min(dd[d], x)
    elif d == "R":
        dd[d] = x if dd[d] == None else max(dd[d], x)
    elif d == "U":
        dd[d] = y if dd[d] == None else max(dd[d], y)
    elif d == "D":
        dd[d] = y if dd[d] == None else min(dd[d], y)

if None in dd.values():
    print("Infinity")
else:
    y = dd["D"] - dd["U"] - 1
    x = dd["L"] - dd["R"] - 1
    print(0 if (y <= 0 or x <= 0) else y * x)
