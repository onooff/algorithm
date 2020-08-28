//Main
import java.util.*;
public class bj1325 {
	//static boolean[][] graph;
	static List<Integer>[] graph;
	static int[] hackable;
	static int n,m,max=Integer.MIN_VALUE;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		n = sc.nextInt();
		m = sc.nextInt();
		graph = new List[n+1];
		for(int i=0;i<=n;i++) {
			graph[i] = new ArrayList<Integer>();
		}
		
		hackable = new int[n+1];
		Arrays.fill(hackable, 1);

		int a,b;
		for(int i=0;i<m;i++) {
			a=sc.nextInt();
			b=sc.nextInt();
			graph[b].add(a);
		}

		for(int i=1;i<=n;i++) {
			dfs(i,i);
			max = Math.max(max, hackable[i]);
		}
		StringBuilder sb = new StringBuilder();
		for(int i=1;i<=n;i++) {
			if(max==hackable[i]) {sb.append(i); sb.append(" ");}
		}
		System.out.println(sb.toString());

		sc.close();
	}

	static void dfs(int idx, int now) {
		int size = graph[now].size();
		for(int i=0;i<size;i++) {
			hackable[idx]++;
			dfs(idx,graph[now].get(i));
		}
	}
}