//Main
import java.util.*;

public class bj2178 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n=sc.nextInt();
		int m=sc.nextInt();

		char[][] map = new char[n][];
		boolean[][] chk = new boolean[n][m];

		for(int i=0;i<n;i++) {
			map[i]=sc.next().toCharArray();
		}

		Queue<v> q = new LinkedList<v>();
		chk[0][0]=true;
		q.offer(new v(0,0,1));

		int ni,nj; 
		while(!q.isEmpty()) {
			v tmp = q.poll();

			for(int i=0;i<4;i++) {
				ni=tmp.i+d[i][0];
				nj=tmp.j+d[i][1];
				if(ni==n-1 && nj==m-1) {System.out.println(tmp.cnt+1); sc.close(); return;}

				if(isIn(ni,nj,n,m) && !chk[ni][nj]) {
					//System.out.println(ni+" "+nj);
					chk[ni][nj]=true;
					if(map[ni][nj]=='1') q.offer(new v(ni,nj,tmp.cnt+1));
				}
			}
		}

		sc.close();
	}
	static boolean isIn(int i, int j, int y, int x) {
		if(i>=0 && j>=0 && i<y && j<x) {return true;}
		return false;
	}
	static class v{
		int i;
		int j;
		int cnt;
		public v(int i, int j, int cnt) {
			super();
			this.i = i;
			this.j = j;
			this.cnt = cnt;
		}
	}
	static int[][] d= {
			{0,1},
			{0,-1},
			{1,0},
			{-1,0}
	};
}