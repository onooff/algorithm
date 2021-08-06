# 똑같은 로직인데 C는 되고 파이싼은 안되노?????????

'''
5 3
5 4 3 2 1
1 3
2 4
5 5

main(){
    int n,m,i,a,b;
    int l[100001]={0,};
    int s[100001]={0,};
    scanf("%d %d",&n,&m);
    for(i=1;i<n+1;i++){
        scanf("%d",&l[i]);
    }
    for(i=1;i<n+1;i++){
        s[i]=s[i-1]+l[i];
    }
    for(i=0;i<m;i++){
        scanf("%d %d",&a,&b);
        printf("%d\n",s[b]-s[a-1]);
    }
}
'''

n, m = map(int, input().split())
l = list(map(int, input().split()))
l.insert(0, 0)
sum_l = [0 for i in range(n+1)]
for i in range(1, n+1):
    sum_l[i] = sum_l[i-1]+l[i]
for i in range(m):
    a, b = map(int, input().split())
    print(sum_l[b]-sum_l[a-1])
