#include <stdio.h>
int main(){
    int n,i,j,tmp;
    char cnt[10001]={0,};
    scanf("%d",&n);
    for(i=0;i<n;i++){
        scanf("%d",&tmp);
        cnt[tmp]++;
    }
    for(i=1;i<10001;i++){
        for(j=0;j<cnt[i];j++) printf("%d\n",i);
    }
}
