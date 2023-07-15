while True:
    v = list(map(int, input().split()))
    s = set(v)
    maxx = max(v)
    if maxx == 0:
        break

    if sum(v) - maxx <= maxx:
        print("Invalid")
    elif len(s) == 1:
        print("Equilateral")
    elif len(s) == 2:
        print("Isosceles")
    elif len(s) == 3:
        print("Scalene")
