//Main
import java.util.*;
public class bj1743 {
	static int n,m;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		n = sc.nextInt();
		m = sc.nextInt();
		int t = sc.nextInt();

		int[][] map = new int[n+1][m+1];

		int i,j,k;

		for(i=0;i<t;i++) {
			j=sc.nextInt();
			k=sc.nextInt();
			map[j][k]=1;
		}

		int max = 0;
		for(i=1;i<=n;i++) {
			for(j=1;j<=m;j++) {
				if(map[i][j]==1) max=Math.max(dfs(map,i,j), max);
			}
		}
		System.out.println(max);

		sc.close();
	}

	static boolean isIn(int i, int j, int y, int x) {
		if(i>0 && j>0 && i<=y && j<=x) {return true;}
		return false;
	}

	static int[][] d= {
			{0,1},
			{0,-1},
			{1,0},
			{-1,0}
	};

	static int dfs(int[][] map, int i, int j) {
		map[i][j]=0;
		int k,ni,nj,sum=1;
		for(k=0;k<4;k++) {
			ni=i+d[k][0];
			nj=j+d[k][1];
			//System.out.println(ni+" "+nj+" "+map.length+" "+map[i].length);
			if(isIn(ni,nj,n,m) && map[ni][nj]==1) sum+=dfs(map,ni,nj);
		}
		return sum;
	}
}