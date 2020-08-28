//Main
import java.util.*;
public class bj2665 {
	static int[][] d= {
			{0,1},
			{0,-1},
			{1,0},
			{-1,0}
	};
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int[][] map = new int[n][n];
		int[][] cnt = new int[n][n];
		boolean[][] chk = new boolean[n][n];
		
		sc.nextLine();
		for(int i=0; i<n; i++) {
			String tmp = sc.nextLine();
			for(int j=0; j<n; j++) {
				map[i][j] = tmp.charAt(j)-'0';
			}
		}
		for(int i=0; i<n; i++) {
			Arrays.fill(cnt[i], Integer.MAX_VALUE);
		}

		Queue<Room> q = new LinkedList<Room>();
		chk[0][0] = true;
		q.offer(new Room(0,0,0));
		
		int ni,nj;
		Room now = null;
		while(!q.isEmpty()) {
			now = q.poll();
			if(now.i==n-1 && now.j==n-1) break;
			for(int k=0; k<4; k++) {
				ni = now.i+d[k][0];
				nj = now.j+d[k][1];
				if(isIn(ni,nj,n,n) && !chk[ni][nj]) {
					chk[ni][nj] = true;
					if(map[ni][nj]==0) q.offer(new Room(ni,nj,now.openCnt+1));
					else q.offer(new Room(ni,nj,now.openCnt));
					
				}
			}
		}
		System.out.println(now.openCnt);

		sc.close();
	}
	
	static boolean isIn(int i, int j, int y, int x) {
		if(i>=0 && j>=0 && i<y && j<x) {return true;}
		return false;
	}
	
	static class Room{
		int i;
		int j;
		int openCnt;
		public Room(int i, int j, int openCnt) {
			super();
			this.i = i;
			this.j = j;
			this.openCnt = openCnt;
		}
	}
}