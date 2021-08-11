n, m = map(int, input().split())
board = list()
for i in range(n):
    board.append(list(input()))
ans = 0


def dfs(y, x):
    global board, n, m
    if x == m-1:
        return 1
    nx = x+1
    for i in range(-1, 2, 1):
        ny = y+i
        if 0 <= ny < n and board[ny][nx] == '.':
            board[ny][nx] = 'p'
            if dfs(ny, nx) == 1:
                return 1
    return 0


for i in range(n):
    ans += dfs(i, 0)
print(ans)


'''
//c코드
#include <stdio.h>
char board[10000][500];
int n,m;
int dfs(y,x){
    int i,ny,nx;
    nx=x+1;
    if(nx==m-1) return 1;
    for(i=-1;i<2;i++){
        ny=y+i;
        if(ny>=0 && ny<n && board[ny][nx]=='.'){
            board[ny][nx]='p';
            if(dfs(ny,nx)==1) return 1;
        }
    }
    return 0;
}

int main(){
    int i,j,ans;
    ans=0;
    scanf("%d %d",&n,&m);
    for(i=0;i<n;i++){
        scanf("%s",board[i]);
    }
    for(i=0;i<n;i++) ans+=dfs(i,0);
    printf("%d\n",ans);
}
'''
