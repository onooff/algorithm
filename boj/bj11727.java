//Main
import java.util.*;
public class bj11727 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		
		int[][] dp = new int [2][n+1];
		dp[0][0]=1;
	    dp[0][1]=2;
	    dp[0][2]=7;
		
		for(int i=3;i<=n; i++) {
			dp[1][i] = (dp[1][i - 1] + dp[0][i - 3])%1000000007;
			dp[0][i] = (3 * dp[0][i - 2] + 2 * dp[0][i - 1] + 2 * dp[1][i])%1000000007;
		}
		
		System.out.println(dp[0][n]);
		
		sc.close();
	}
}
