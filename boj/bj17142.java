//Main
import java.util.*;
public class bj17142 {
	static int n,m,min;
	static int[][] map;
	static class virus{
		int i;
		int j;
		public virus(int i, int j) {
			super();
			this.i = i;
			this.j = j;
		}
	}
	static List<virus> vList = new ArrayList<>();
	static virus[] vArr;
	static boolean[] chk;

	static void dfs(int cnt) {
		if(cnt==m) {
			
		}
		for(int i=cnt;i<vList.size();i++) {
			dfs(cnt+1);
		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		n=sc.nextInt();
		m=sc.nextInt();

		map=new int[n][n];

		for(int i=0;i<n;i++) {
			for(int j=0;j<n;j++) {
				map[i][j]=sc.nextInt();
				if(map[i][j]==2) vList.add(new virus(i, j));
			}
		}

		vArr = (virus[]) vList.toArray();
		chk = new boolean[vArr.length];

		dfs(0);

		sc.close();
	}
}