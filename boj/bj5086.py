a, b = map(int, input().split())
while not(a == 0 and b == 0):
    if b > a and b % a == 0:
        print("factor")
    elif a > b and a % b == 0:
        print("multiple")
    else:
        print("neither")
    a, b = map(int, input().split())
