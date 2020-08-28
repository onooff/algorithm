//Main
import java.util.*;
public class bj16234 {

	static int n,l,r,  group,sum,avg;
	static boolean flag;
	static int[][] map;
	static boolean[][] chk;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		n = sc.nextInt();
		l = sc.nextInt();
		r = sc.nextInt();

		map = new int[n][n];

		for(int i=0;i<n;i++) {
			for(int j=0;j<n;j++) {
				map[i][j] = sc.nextInt();
			}
		}

		flag = true;
		int cnt = 0;
		while(flag) {
			flag = false;
			cnt++;
			chk = new boolean[n][n];
			for(int i=0;i<n;i++) {
				for(int j=0;j<n;j++) {
					sum=0; group=0;
					if(!chk[i][j]) {
						chk[i][j]=true;
						dfs(i,j);
					}
				}
			}
		}

		System.out.println(cnt-1);

		sc.close();
	}
	static int[][] d= {
			{0,1},
			{0,-1},
			{1,0},
			{-1,0}
	};

	static void dfs(int i, int j) {
		group++;
		sum += map[i][j];

		int ni, nj, gap;
		for(int k=0; k<4; k++) {
			ni = i+d[k][0];
			nj = j+d[k][1];
			if(isIn(ni,nj,n,n) && !chk[ni][nj]) {
				gap = Math.abs(map[i][j] - map[ni][nj]);
				if(l <= gap && gap <= r){
					flag = true;
					chk[ni][nj]=true;
					dfs(ni,nj);
				}
			}
		}
		map[i][j] = sum/group;
	}
	static boolean isIn(int i, int j, int y, int x) {
		if(i>=0 && j>=0 && i<y && j<x) {return true;}
		return false;
	}
}