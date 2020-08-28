import java.util.Scanner;

public class bj2579 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int[] s = new int[301];
		
		for (int i = 1; i <= n; i++) {
			s[i] = sc.nextInt();
		}

		int[] memo = new int[301];
	
		
		memo[1] = s[1];
		memo[2] = Math.max(s[1]+s[2], s[1]);
		memo[3] = Math.max(s[1]+s[3], s[2]+s[3]);

		for (int i=4; i<=n; i++) {
			memo[i] = Math.max(memo[i-3] + s[i-1]+s[i], memo[i-2] + s[i]);
		}
		
		System.out.println(memo[n]);
	}
}