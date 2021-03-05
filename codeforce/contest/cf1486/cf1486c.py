import sys

n = int(input())
low = 1
high = n
print('?'+str(low)+str(high))
response = int(input())

while True:
    mid = (low+high) //

    print('?'+str(low)+str(mid))
    sys.stdout.flush()
    l_res = int(input())

    print('?'+str(mid+1)+str(mid))
    h_res = int(input())
    sys.stdout.flush()

    if l_res == response:
        high = mid
    elif h_res == response:
        low = mid+1
    else:
        print('?'+str()+str(mid))
