w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

a = ((t+p) % (w*2))
b = ((t+q) % (h*2))
if a > w:
    a = 2*w-a
if b > h:
    b = 2*h-b

print(a, b)
