//Main
import java.util.*;
public class bj1926 {
	static int[][] map;
	static boolean[][] chk;
	static int y,x,size,max=Integer.MIN_VALUE,cnt=0;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		y = sc.nextInt();
		x = sc.nextInt();
		map = new int[y][x];
		chk = new boolean[y][x];

		for(int i=0;i<y;i++) {
			for(int j=0;j<x;j++) {
				map[i][j]=sc.nextInt();
			}
		}
		for(int i=0;i<y;i++) {
			for(int j=0;j<x;j++) {
				if(map[i][j]==1 && !chk[i][j]) {
					size=0;
					chk[i][j]=true;
					dfs(i,j);
					
					cnt++;
					max = Math.max(size, max);
				}
			}
		}
		if(max==Integer.MIN_VALUE) max=0;
		System.out.println(cnt);
		System.out.println(max);
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

	static void dfs(int i, int j) {
		size++;
		int ni, nj;
		for(int k=0; k<4; k++) {
			ni = i+d[k][0];
			nj = j+d[k][1];

			if(isIn(ni,nj,y,x) && !chk[ni][nj] && map[ni][nj]==1) {chk[ni][nj]=true; dfs(ni,nj);}
		}
	}
}