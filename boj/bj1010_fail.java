import java.util.*;
public class bj1010_fail {
	static int n,m,cnt;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();

		for(int tc=1;tc<=t;tc++) {
			n=sc.nextInt();
			m=sc.nextInt();
			cnt=0;
			
			dfs(0,0);
			
			System.out.printf("%d%n",cnt);
		}
		
		sc.close();
	}
	private static void dfs(int nn, int mm) {
		int l = m-n+nn+1;
		for(int i=mm;i<l;i++) {
			if(nn+1==n) {cnt++; continue;}
			else dfs(nn+1, i+1);
		}
	}
}