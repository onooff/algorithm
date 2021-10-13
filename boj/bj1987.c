#include <stdio.h>
int n,m;
int cnt=1,ans=1;
int board[20][20];
int chk[26]={0,};
int d[4][2] = {{0,1},{0,-1},{1,0},{-1,0}};
void dfs(int y,int x);
int main(){
    char tmp[21];
    scanf("%d %d",&n,&m);
    for(int i=0;i<n;i++){
        scanf("%s",tmp);
        for(int j=0;j<m;j++){
            board[i][j]=tmp[j]-65;
        }
    }
    
    dfs(0,0);
    printf("%d",ans);
    
    return 0;
}
void dfs(int y,int x){
    int ny,nx;
    chk[board[y][x]]=1;
    for(int nd=0;nd<4;nd++){
        ny=y+d[nd][0];
        nx=x+d[nd][1];
        if(ny>=0 && nx>=0 && ny<n && nx<m && !chk[board[ny][nx]]){
            cnt++;
            if(ans<cnt){
                ans=cnt;
            }
            dfs(ny,nx);
        }
    }
    cnt--;
    chk[board[y][x]]=0;
}