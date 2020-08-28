//Main
import java.util.*;
public class bj16236 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int[][] map = new int[n][n];
		boolean[][] chk = new boolean[n][n];
		int babyShark = 2;
		Queue<v> q = new LinkedList<v>();
		int[] fish = new int[6+1];

		for(int i=0;i<n;i++) {
			for(int j=0;j<n;j++) {
				map[i][j] = sc.nextInt();
				if(map[i][j]==9) {chk[i][j]=true; q.offer(new v(i,j,0)); map[i][j]=0;}
				else if(map[i][j]!=0) fish[map[i][j]]++;
			}
		}

		if(fish[1]==0) {System.out.println('0'); sc.close(); return;}

		v tmp;
		int ni,nj,sum=0,growCnt=2;
		while(!q.isEmpty()) {			
			tmp = q.poll();
			if(map[tmp.i][tmp.j]!=0 && babyShark>map[tmp.i][tmp.j]) {
				System.out.println("옴뇸뇸 i="+tmp.i+" j="+tmp.j+" d="+tmp.d+" sum="+sum+" shark="+babyShark+" getFish="+map[tmp.i][tmp.j]);
				fish[map[tmp.i][tmp.j]]--;
				map[tmp.i][tmp.j]=0;
				sum+=tmp.d;
				growCnt--;
				if(growCnt==0) {babyShark++; growCnt=babyShark;}

				boolean flag=false;
				for(int i=1;i<(babyShark>7? 7:babyShark);i++) {
					if(fish[i]>0) {flag=true; break;}
				}

				if(flag) {
					q.clear();
					chk = new boolean[n][n];
					chk[tmp.i][tmp.j]=true;
					q.offer(new v(tmp.i,tmp.j,0));
					continue;
				}
				else break;
			}

			for(int i=0;i<4;i++) {
				ni=tmp.i+d[i][0];
				nj=tmp.j+d[i][1];
				if(isIn(ni,nj,n,n)&&babyShark>=map[ni][nj]&&!chk[ni][nj]) {
					chk[ni][nj]=true;
					q.offer(new v(ni,nj,tmp.d+1));
				}
			}
		}

		System.out.println(sum);

		sc.close();
	}
	static class v{
		int i;
		int j;
		int d;
		public v(int i, int j, int d) {
			super();
			this.i = i;
			this.j = j;
			this.d = d;
		}
	}
	static boolean isIn(int i, int j, int y, int x) {
		if(i>=0 && j>=0 && i<y && j<x) {return true;}
		return false;
	}

	static int[][] d= {
			{-1,0},
			{0,-1},
			{0,1},
			{1,0}
	};
}