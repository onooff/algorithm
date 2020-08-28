import java.util.*;

public class swea7699 {
	static boolean[] CHK = new boolean[26];
	static boolean[][] CHKMAP = null;
	static char[][] MAP = null;
	static int BEST = Integer.MIN_VALUE;
	static int[] dy = {-1,0,1,0};
	static int[] dx = {0,1,0,-1};

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int t = sc.nextInt();
		int r,c;

		for(int tc=1;tc<=t;tc++) {
			r = sc.nextInt();
			c = sc.nextInt();
			MAP = new char[r+2][c+2];
			CHKMAP = new boolean[r+2][c+2];
			Arrays.fill(CHK, false);
			sc.nextLine();

			for(int i=1;i<=r;i++) {
				String s = sc.nextLine();
				for(int j=1;j<=c;j++) {
					MAP[i][j]=s.charAt(j-1);
				}
				//System.out.println(Arrays.toString(MAP[i]));//debug
			}

			CHK[MAP[1][1]-'A']=true;
			CHKMAP[1][1]=true;
			tour(1,1,1);

			System.out.printf("#%d %d%n",tc,BEST); 
			BEST = Integer.MIN_VALUE;
		}

		sc.close();
	}

	//	static void tour(int y, int x, int result) {
	//		int idx=MAP[y][x]-'A';
	//		if(!CHK[idx]) {
	//			//System.out.println(y+" - "+x);//debug
	//			System.out.print(MAP[y][x]+" ");//debug
	//			result++;
	//			CHK[idx]=true;
	//			CHKMAP[y][x]=true;
	//
	//			int ny,nx;
	//			for(int i=0;i<4;i++) {
	//				ny=y+dy[i];
	//				nx=x+dx[i];
	//
	//				if(isAlphabet(MAP[ny][nx]) && !CHKMAP[ny][nx]) {
	//					tour(ny,nx,result);
	//				}
	//			}
	//		}
	//		System.out.println();//debug
	//
	//		if(result>BEST) BEST = result;
	//		CHK[idx]=false;
	//		return;
	//	}

	static void tour(int y, int x, int result) {

		int ny,nx,idx;
		for(int i=0;i<4;i++) {
			ny=y+dy[i];
			nx=x+dx[i];

			if(isAlphabet(MAP[ny][nx]) && !CHKMAP[ny][nx]) {
				idx = MAP[ny][nx]-'A';

				if(!CHK[idx]) {
					CHK[idx]=true;
					CHKMAP[ny][nx]=true;
					tour(ny,nx,result+1);
					CHK[idx]=false;
					CHKMAP[ny][nx]=false;
				}
			}
		}

		if(result>BEST) BEST = result;
		return;
	}

	static boolean isAlphabet(char c) {
		if(c>='A' && c<='Z') return true;
		return false;		
	}
}