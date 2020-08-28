//Main
import java.util.*;
public class bj2210 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = 5;
		int[][] arr = new int[N][N];
		Set<String> set = new TreeSet<String>();

		for(int i=0;i<N;i++) {
			for(int j=0;j<N;j++) {
				arr[i][j]=sc.nextInt();
			}
		}

		Queue<v> q = new LinkedList<v>();
		v tmp;
		int ni,nj;
		for(int i=0;i<N;i++) {
			for(int j=0;j<N;j++) {

				q.offer(new v(i,j,new StringBuilder(arr[i][j])));
				while(!q.isEmpty()) {
					tmp = q.poll();
					if(tmp.sb.length()>=6) {
						//if(set.add(tmp.sb.toString()))System.out.println(tmp.sb);
						set.add(tmp.sb.toString());
						continue;
					}

					for(int k=0;k<4;k++) {
						ni=tmp.i+d[k][0];
						nj=tmp.j+d[k][1];
						if(isIn(ni,nj,N,N)) q.offer(new v(ni,nj,new StringBuilder(tmp.sb.toString()).append(arr[ni][nj])));
					}
				}

			}
		}
		System.out.println(set.size());
		sc.close();
	}
	static boolean isIn(int i, int j, int y, int x) {
		if(i>=0 && j>=0 && i<y && j<x) {return true;}
		return false;
	}

	static int[][] d= {
			{0,1},
			{0,-1},
			{1,0},
			{-1,0}
	};
	static class v{
		int i;
		int j;
		StringBuilder sb;
		public v(int i, int j, StringBuilder sb) {
			super();
			this.i = i;
			this.j = j;
			this.sb = sb;
		}
	}
}