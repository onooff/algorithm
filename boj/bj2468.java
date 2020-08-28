//Main
import java.util.*;
public class bj2468 {
	static int n,cnt,max=1;
	static int[][] map;
	static boolean[][] chk;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		n = sc.nextInt();
		map = new int[n][n];
		Set<Integer> set = new TreeSet<Integer>();

		for(int i=0;i<n;i++) {
			for(int j=0;j<n;j++) {
				map[i][j] = sc.nextInt();
				set.add(map[i][j]);
			}
		}

		for(int flood : set) {
			cnt=0;
			chk = new boolean[n][n];
			for(int i=0;i<n;i++) {
				for(int j=0;j<n;j++) {
					if(flood==map[i][j]) map[i][j]=0;
					if(map[i][j]==0) chk[i][j]=true;
				}
			}
			for(int i=0;i<n;i++) {
				for(int j=0;j<n;j++) {
					if(!chk[i][j]) {chk[i][j]=true; dfs(i,j); cnt++;}
				}
			}
			max=Math.max(max, cnt);
		}

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
		int ni, nj;
		for(int k=0; k<4; k++) {
			ni = i+d[k][0];
			nj = j+d[k][1];
			if(isIn(ni,nj,n,n) && !chk[ni][nj]) {chk[ni][nj]=true; dfs(ni,nj);}
		}
	}
}