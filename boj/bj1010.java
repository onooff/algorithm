import java.util.*;
public class bj1010 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int t = sc.nextInt();

		int i,j,k,n,m;
		int [][] dp = new int[31][31];
		for(i=0;i<=30;i++) dp[1][i] = i;
		for(i=2;i<=30;i++){
			for(j=i;j<=30;j++){
				for(k=j;k>=i;k--){
					dp[i][j]+=dp[i-1][k-1];
				}
			}        
		}

		for(int tc=1;tc<=t;tc++) {
			n=sc.nextInt();
			m=sc.nextInt();
			System.out.println(dp[n][m]);
		}

		sc.close();
	}
}