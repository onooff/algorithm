main(){
    int t,tc,sign,l1,l2,i,j,up,calc,cnt;
    char n1[13], n2[13], result[20]={0,};
    scanf("%d",&t);
    
    for(tc=0;tc<t;tc++){
        l1=11;
        l2=11;
        sign=1;
        scanf("%s %s",n1,n2);
        if(n1[0]=='-') {
            sign*=-1;
            l1++;
        }
        if(n2[0]=='-'){
            sign*=-1;
            l2++;
        }
        for(i=1;i<=11;i++){
            if(i==10) continue;
            up=0;
            cnt=i-1;
            if(cnt>=10) cnt--;
            for(j=1;j<=11;j++){
                if(j==10) continue;
                calc = (n1[l1-j]-'0')*(n2[l2-i]-'0');
                calc += up;
                up = calc/10;
                result[cnt]+=calc%10;
                cnt++;
            }
            result[cnt]+=up;
        }
        up=0;
        for(i=0;i<20;i++){
            result[i]+=up;
            up=result[i]/10;
            result[i]=result[i]%10;
        }
        
        if(sign==-1) printf("-");
        cnt=19;
        for(i=0;i<21;i++){
            if(i==0 && result[cnt]==0){cnt--; continue;}
            if(i==2){printf("."); continue;}
            printf("%d",result[cnt]);
            result[cnt]=0;
            cnt--;
        } 
        printf("\n");
    }
}
