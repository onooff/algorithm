n = int(input())
e = input().count('e')
two = n-e
if two > e:
    print(2)
elif e > two:
    print('e')
else:
    print("yee")
