import java.util.*;
public class swea7793 {
	static int[][] d = {
			{-1,0},//상
			{0,1},//우
			{1,0},//하
			{0,-1}//좌
	};
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		//int t = sc.nextInt();
		
		//for(int tc=1;tc<=t;tc++) {
			int n = sc.nextInt();
			int m = sc.nextInt();
			char[][] map = new char[n][m];
			boolean[][] enemyChk = new boolean[n][m];
			boolean[][] playerChk = new boolean[n][m];
			Queue<v> eq = new LinkedList<>();//enemy queue
			Queue<v> pq = new LinkedList<>();//player queue

			String tmp = sc.nextLine();
			for(int i=0;i<n;i++) {
				tmp = sc.nextLine();
				for(int j=0;j<m;j++) {
					map[i][j] = tmp.charAt(j);
					if(map[i][j]=='.') continue;
					if(map[i][j]=='D') {
						enemyChk[i][j]=true;
						continue;
					}
					if(map[i][j]=='X') {
						enemyChk[i][j]=true;
						playerChk[i][j]=true;
						continue;
					}
					if(map[i][j]=='*') {
						playerChk[i][j]=true;
						enemyChk[i][j]=true;
						eq.offer(new v(i,j,0));
						continue;
					}
					if(map[i][j]=='S') {
						playerChk[i][j]=true;
						enemyChk[i][j]=true;
						pq.offer(new v(i,j,0));
						continue;
					}
				}
			}

			v vTmp = null;
			int ny,nx,cnt = 0;
			int result = -1;
			loop:while(!pq.isEmpty()) {
				while(!eq.isEmpty() && eq.peek().t==cnt) {
					vTmp = eq.poll();
					for(int i=0;i<4;i++) {
						ny=vTmp.y+d[i][0];
						nx=vTmp.x+d[i][1];
						if(isIn(ny,nx,n,m)) {
							if(!enemyChk[ny][nx]) {map[ny][nx]='*'; playerChk[ny][nx]=true; enemyChk[ny][nx]=true; eq.offer(new v(ny,nx,cnt+1));}
						}
					}
				}
				
				while(!pq.isEmpty() && pq.peek().t==cnt) {
					vTmp = pq.poll();
					if(map[vTmp.y][vTmp.x]=='*') {continue;}
					for(int i=0;i<4;i++) {
						ny=vTmp.y+d[i][0];
						nx=vTmp.x+d[i][1];
						if(isIn(ny,nx,n,m)) {
							if(map[ny][nx]=='D') {result = cnt+1; break loop;}
							if(!playerChk[ny][nx]) {map[ny][nx]='S'; playerChk[ny][nx]=true; pq.offer(new v(ny,nx,cnt+1));}
						}
					}
				}
				
				cnt++;
			}
			
//			if(result==-1) System.out.printf("#%d GAME OVER%n",tc);
//			else System.out.printf("#%d %d%n",tc,result);
			if(result==-1) System.out.printf("GAME OVER%n");
			else System.out.printf("%d%n",result);
		//}

		sc.close();
	}
	static boolean isIn(int i, int j, int y, int x) {
		if(i>=0 && j>=0 && i<y && j<x) {return true;}
		return false;
	}

	static class v{
		int y;
		int x;
		//char type;
		int t;
		//public v(int y, int x, char type) {
		public v(int y, int x, int t) {
			super();
			this.y = y;
			this.x = x;
			//this.type = type;
			this.t = t;
		}
	}
}

/*
2
5 3
D*S
.X.
.X.
.X.
...
5 3
D*S
...
.X.
.X.
...

5 7
S....X*
.XXX.X.
..X..X.
X.X.XX.
X...DX.
 */