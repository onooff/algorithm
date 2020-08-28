import java.util.*;
public class swea2814 {
	static boolean[] CHK = null;
	static int BEST = 0;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int t = sc.nextInt();

		for(int tc=1;tc<=t;tc++) {
			int n = sc.nextInt();
			int m = sc.nextInt();

			boolean[][] g = new boolean[n+1][n+1];
			CHK = new boolean[n+1];

			int a,b;
			for(int i=0;i<m;i++) {
				a = sc.nextInt();
				b = sc.nextInt();

				g[a][b]=true;
				g[b][a]=true;
			}

			for(int i=1;i<=n;i++) {
				CHK[i]=true;
				dfs(g,i,1);
				CHK[i]=false;
			}
			System.out.printf("#%d %d%n",tc,BEST); BEST = 0;
		}

		sc.close();
	}

	private static void dfs(boolean[][] g, int idx, int l) {
		for(int i=1;i<g[idx].length;i++) {
			if(!CHK[i] && g[idx][i]) {
				CHK[i]=true;
				dfs(g,i,l+1);
				CHK[i]=false;
			}
		}
		if (l>BEST) BEST=l;
	}
}