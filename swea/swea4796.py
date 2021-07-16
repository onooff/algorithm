'''
3
3
1 3 2
3
3 2 1
9
1 4 6 5 3 7 9 2 8
'''

t = int(input())

for tc in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    ans = 0
    for i in range(len(l)):
        if (i != 0 and i != len(l)-1) and (l[i-1] < l[i] > l[i+1]):
            left = 0
            right = 0
            while i-left >= 0 and l[i-left] > l[i-(left+1)]:
                left += 1
            while i+right < len(l)-1 and l[i+right] > l[i+(right+1)]:
                right += 1
            print(">>", left, right, i)
            ans += left*right
    print(ans)
