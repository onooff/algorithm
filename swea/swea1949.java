//Solution
import java.util.*;
public class swea1949 {
	static int n,k,top,ans;
	static int[][] map;
	static boolean[][] chk;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int t = sc.nextInt();

		for(int tc=1;tc<=t;tc++) {

			top = Integer.MIN_VALUE;
			ans = Integer.MIN_VALUE;
			n = sc.nextInt();
			k = sc.nextInt();
			map = new int[n][n];
			chk = new boolean[n][n];

			for(int i=0;i<n;i++) {
				for(int j=0;j<n;j++) {
					map[i][j] = sc.nextInt();
					top = Math.max(top, map[i][j]);
				}
			}
			for(int i=0;i<n;i++) {
				for(int j=0;j<n;j++) {
					if(map[i][j]==top) {
						chk[i][j]=true;
						dfs(i,j,map[i][j],false,0);
						chk[i][j]=false;
					}
				}
			}
			System.out.printf("#%d %d%n",tc,ans);
		}
		sc.close();
	}
	static int[][] d= {{0,1},{0,-1},{1,0},{-1,0}};
	static boolean isIn(int i, int j, int y, int x) {
		if(i>=0 && j>=0 && i<y && j<x) return true;
		return false;
	}
	static void dfs(int i, int j, int mapIJ, boolean usedK, int length) {

		length++;
		int ni, nj;
		boolean isEnd = true;

		for(int a=0; a<4; a++) {
			ni = i+d[a][0];
			nj = j+d[a][1];
			if(isIn(ni,nj,n,n) && !chk[ni][nj]) {
				chk[i][j]=true;
				if(map[ni][nj]<mapIJ){
					dfs(ni,nj,map[ni][nj]  ,usedK,length); isEnd=false;
				}
				else if( (map[ni][nj]-k)<mapIJ && !usedK ){
					dfs(ni,nj,mapIJ-1,true ,length); isEnd=false;
				}
				chk[i][j]=false;
			}
		}
		if(isEnd) {
			ans = Math.max(ans, length);
			return;
		}
	}
}

/*
#1 6
#2 3
#3 7
#4 4
#5 2
#6 12
#7 6
#8 7
#9 10
#10 19

#1 7
#2 3
#3 7
#4 4
#5 3
#6 12
#7 6
#8 7
#9 10
#10 15
 */