//Solution
import java.util.*;
public class swea9659 {
	
	static int mod = 998244353;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();

		for(int tc=1;tc<=T;tc++) {
			int n = sc.nextInt();
			
			int[] t = new int[n+1];
			int[] a = new int[n+1];
			int[] b = new int[n+1];
			for(int i=2;i<=n;i++) {
				t[i] = sc.nextInt();
				a[i] = sc.nextInt();
				b[i] = sc.nextInt();
			}
			
			int m = sc.nextInt();
			
			StringBuilder sb = new StringBuilder();
			sb.append("#"+tc);
			
			long x;
			long result;
			for(int i=0;i<m;i++) {
				x = sc.nextLong();
				result=0;
				
				//크흠...
				
				sb.append(" "+result);
			}
			System.out.println(sb);
		}
		
		sc.close();
	}
}