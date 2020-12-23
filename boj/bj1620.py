n, m = map(int, input().split())

name_to_num = dict()
num_to_name = dict()
for i in range(1, n+1):
    name = input()
    name_to_num.setdefault(name, i)
    num_to_name.setdefault(i, name)
for i in range(m):
    get = input()
    if get[0].isdigit():
        print(num_to_name[int(get)])
    else:
        print(name_to_num[get])
