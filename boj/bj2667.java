//Main
import java.util.*;
public class bj2667 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		char[][] arr = new char[n][n];
		boolean[][] chk = new boolean[n][n];
		for(int i=0;i<n;i++) arr[i]=sc.next().toCharArray();

		Queue<v> q = new LinkedList<v>();
		List<Integer> apt = new ArrayList<Integer>();
		v tmp;
		int ni,nj,sum;
		for(int i=0;i<n;i++) {
			for(int j=0;j<n;j++) {
				if(arr[i][j]!='0' && !chk[i][j]) {
					sum=1;
					chk[i][j]=true;
					q.offer(new v(i,j));
					while(!q.isEmpty()) {
						tmp=q.poll();
						for(int k=0;k<4;k++) {
							ni=tmp.i+d[k][0];
							nj=tmp.j+d[k][1];
							if(isIn(ni,nj,n,n) && arr[ni][nj]!='0' && !chk[ni][nj]) {
								chk[ni][nj]=true;
								q.offer(new v(ni,nj));
								sum++;
							}
						}
					}
					apt.add(sum);
				}
			}
		}
		Collections.sort(apt);
		System.out.println(apt.size());
		for(int i:apt) System.out.println(i);
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
		public v(int i, int j) {
			super();
			this.i = i;
			this.j = j;
		}
	}
}