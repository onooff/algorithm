import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class swea4534_ans {
	static final int MOD = 1000000007;
	static int N;
	static List[] adj;
	static long[][] memo; //색상, 정점 번호

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T= sc.nextInt();
		for(int tc = 1; tc <= T; tc++) {
			N = sc.nextInt();
			adj = new ArrayList[N+1];
			for(int i = 1; i <= N; i++)
				adj[i] = new ArrayList<>();
			memo = new long[2][N+1];
			for(int i = 1; i < N; i++) {
				int a = sc.nextInt();
				int b = sc.nextInt();
				adj[a].add(b);
				adj[b].add(a);
			}
			long ans = ( dfs(1, 0, -1) + dfs(1, 1, -1) ) % MOD;
			System.out.println("#" + tc + " " + ans);
		}
	}


	static long dfs(int v, int color, int parent) {
		if(memo[color][v] != 0)
			return memo[color][v];
		long ret = 1;

		if( color == 0 ) {
			for(int i = 0; i < adj[v].size(); i++) {
				if( (int)adj[v].get(i) != parent ) {
					ret *= dfs((int)adj[v].get(i), 1, v);
					ret %= MOD;
				}
			}
		}
		else {
			for(int i = 0; i < adj[v].size(); i++) {
				if( (int)adj[v].get(i) != parent ) {
					ret *= ( dfs((int)adj[v].get(i), 1, v) + dfs((int)adj[v].get(i), 0, v)  );
					ret %= MOD;
				}
			}
		}
		memo[color][v] = ret;
		return ret;
	}
}