import java.util.*;
public class bj1260 {
	static int v,e,start;
	static int[][] map;
	static boolean[] dfsChk;
	static boolean[] bfsChk;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		v = sc.nextInt();
		e = sc.nextInt();
		start = sc.nextInt();

		map = new int[v+1][v+1];
		dfsChk = new boolean[v+1]; 
		bfsChk = new boolean[v+1];

		int ti,tj;
		for(int i=0; i<e; i++) {
			ti=sc.nextInt();
			tj=sc.nextInt();

			map[ti][tj]++; map[tj][ti]++;
		}

		dfs(start);
		System.out.println();
		bfs(start);

		sc.close();
	}

	static void dfs(int nowV) {
		dfsChk[nowV]=true;
		System.out.print(nowV+" ");
		for(int i=1;i<=v;i++) {
			if(map[nowV][i]>0 && !dfsChk[i]) dfs(i);
		}
	}
	
	static void bfs(int s) {
		Queue<Integer> q = new LinkedList<Integer>();
		bfsChk[s]=true;
		q.offer(s);
		
		while(!q.isEmpty()) {
			int tmp = q.poll();
			System.out.print(tmp+" ");
			for(int i=1;i<=v;i++) {
				if(map[tmp][i]>0 && !bfsChk[i]) {bfsChk[i]=true; q.offer(i);}
			}
		}
	}
}