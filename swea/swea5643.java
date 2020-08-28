import java.util.*;
public class swea5643 {
	static int[] p;
	static int[] c;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		for(int tc=1;tc<=t;tc++) {
			int n = sc.nextInt();
			int m = sc.nextInt();
			c = new int[n+1];
			p = new int[n+1];
			ArrayList<ArrayList<Integer>> graphDown = new ArrayList<>();
			ArrayList<ArrayList<Integer>> graphUp = new ArrayList<>();
			for(int i=0;i<=n;i++) {
				graphDown.add(new ArrayList<Integer>());
				graphUp.add(new ArrayList<Integer>());
			}

			int v1,v2;
			for(int i=0;i<m;i++) {
				v1=sc.nextInt();
				v2=sc.nextInt();
				graphDown.get(v1).add(v2);
				graphUp.get(v2).add(v1);
			}

			int result = 0;
			for(int i=1;i<=n;i++) {
				c[i]=dfs(graphDown,i,new boolean[n+1]);
				p[i]=dfs(graphUp,i,new boolean[n+1]);
				if(c[i]+p[i]==n-1) result++;
			}
			System.out.printf("#%d %d\n",tc,result);
		}
		sc.close();
	}

	static int dfs(ArrayList<ArrayList<Integer>> graph, int n, boolean[] chk){
		int sum=0;
		ArrayList<Integer> list = graph.get(n);
		if(!list.isEmpty()) {
			for(int nv:list) {
				if(!chk[nv]) {chk[nv]=true; sum++; sum+=dfs(graph,nv,chk);}
			}
		}
		return sum;
	}
}