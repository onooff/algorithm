//Main
import java.util.*;
public class bj15686 {
	static int[][] chickLength;
	static boolean[] chk;
	static List<v> homeList;
	static List<v> chickList;
	static int n,m,hl,cl;
	static int min = Integer.MAX_VALUE;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		n = sc.nextInt();
		m = sc.nextInt();
		homeList = new ArrayList<v>();
		chickList = new ArrayList<v>();


		int tmp = 0;
		for(int i=0; i<n; i++) {
			for(int j=0; j<n; j++) {
				tmp = sc.nextInt();
				if(tmp==1) homeList.add(new v(i,j));
				else if(tmp==2) chickList.add(new v(i,j));
			}
		}

		hl=homeList.size();
		cl=chickList.size();

		chickLength = new int[hl][cl];	
		chk = new boolean[cl];

		v tmpHome, tmpChick;
		for(int i=0; i<hl; i++) {
			for(int j=0; j<cl; j++) {
				tmpHome = homeList.get(i);
				tmpChick = chickList.get(j);
				chickLength[i][j] = Math.abs(tmpHome.y-tmpChick.y)+Math.abs(tmpHome.x-tmpChick.x);
			}
		}

		dfs(0,0);

		System.out.println(min);
		sc.close();
	}
	private static void dfs(int idx, int num) {
		if(num==m) {
			int result = 0;
			for(int i=0; i<hl; i++) {
				int minTmp = Integer.MAX_VALUE;
				for(int j=0; j<cl; j++) {
					if(chk[j]) {
						minTmp = Math.min(minTmp, chickLength[i][j]);
					}
				}
				result+=minTmp;
			}
			min = Math.min(result, min);
			return;
		}

		for(int i=idx; i<cl; i++) {
			if(!chk[i]) {
				chk[i]=true;
				dfs(i+1, num+1);
				chk[i]=false;
			}
		}
	}
	static class v{
		int y;
		int x;
		public v(int y, int x) {
			super();
			this.y = y;
			this.x = x;
		}
	}
}

/*
치킨거리는 x차절대값+y차절대값

 */