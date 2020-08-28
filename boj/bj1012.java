
import java.util.*;
public class bj1012 {
	static int x,y,n,cnt;
	static boolean[][] map;
	static int[][] d= {
			{0,1},
			{0,-1},
			{1,0},
			{-1,0}
	};
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();

		for(int tc=1;tc<=t;tc++) {
			
			x = sc.nextInt();
			y = sc.nextInt();
			n = sc.nextInt();
			cnt = 0;
			map = new boolean[y][x];
			
			int tmpX,tmpY;
			for(int i=0; i<n; i++) {
				tmpX=sc.nextInt();
				tmpY=sc.nextInt();
				map[tmpY][tmpX]=true;
			}
			
			for(int i=0; i<y; i++) {
				for(int j=0; j<x; j++) {
					if(map[i][j]) {
						dfs(i,j);
						cnt++;
					}
				}
			}
			System.out.printf("%d%n",cnt);			
		}
		
		sc.close();
	}
	static void dfs(int i, int j) {
		map[i][j] = false;
		int ni, nj;
		for(int k=0; k<4; k++) {
			ni = i+d[k][0];
			nj = j+d[k][1];
			
			if(isIn(ni,nj,y,x) && map[ni][nj]) dfs(ni,nj);
		}
	}
	
	static boolean isIn(int i, int j, int y, int x) {
		if(i>=0 && j>=0 && i<y && j<x) {return true;}
		return false;
	}
}
