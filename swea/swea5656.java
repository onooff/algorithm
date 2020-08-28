import java.util.*;

public class swea5656 {
	static int n,w,h;
	static int[][] map = null;
	static int[][] mapCopy = null;
	static boolean[][] chk = null;
	static int[] ball = null; 
	static int[] cnt = null; 
	static int[] cntCopy = null; 
	static int min = Integer.MAX_VALUE;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int t = sc.nextInt();

		for(int tc=1;tc<=t;tc++) {
			n = sc.nextInt();
			w = sc.nextInt();
			h = sc.nextInt();
			ball = new int[n];
			map = new int[h][w];
			mapCopy = new int[h][w];
			cnt = new int[w];
			cntCopy = new int[w];
			
			for(int i=0;i<h;i++) {
				for(int j=0;j<w;j++) {
					map[i][j]=sc.nextInt();
					if(map[i][j]!=0) cnt[j]++;
				}
			}
			
			shot(0);

			System.out.printf("#%d %d%n",tc,min); min=Integer.MAX_VALUE;
		}

		sc.close();
	}
	
	static void shot(int ballIdx) {
		if(ballIdx==n) {			
			//System.out.print(Arrays.toString(ball));//dbg
			for(int i=0;i<h;i++) {
				System.arraycopy(map[i], 0, mapCopy[i], 0, map[i].length);
			}
			System.arraycopy(cnt, 0, cntCopy, 0, cnt.length);
			shoot(0); 
			return;
		}
		
		for(int i=0;i<w;i++) {
			ball[ballIdx]=i;
			shot(ballIdx+1);
		}
	}
	
	static void shoot(int ballIdx) {
		if(ballIdx==n  || cntCopy[ball[ballIdx]]==0) {
			int tmp = 0;
			for(int i=0;i<w;i++) {
				tmp+=cntCopy[i];
			}
			if(min>tmp) min=tmp;
			//System.out.println("min="+tmp);//dbg
			//System.out.println(Arrays.toString(cntCopy));//dbg
			return;
		}
		
		chk = new boolean[h][w];
		chk[h-cntCopy[ball[ballIdx]]][ball[ballIdx]]=true;
		breakk(h-cntCopy[ball[ballIdx]],ball[ballIdx]);
		int[][] mapTmp = new int[h][w];
		for(int i=0;i<w;i++) {
			int mapTmpId = h-1;
			for(int j=h-1;j>=0;j--) {
				if(mapCopy[j][i]!=0) {
					mapTmp[mapTmpId][i]=mapCopy[j][i];
					mapTmpId--;
				}
			}
		}
		mapCopy=mapTmp;
		shoot(ballIdx+1);
	}
	
	private static void breakk(int y, int x) {
		//System.out.println(y+" "+x+" "+mapCopy[y][x]);//dbg
		for(int i=1; i<mapCopy[y][x]; i++) {
			if(isIn(y,x-i,h,w) && mapCopy[y][x-i]!=0 && !chk[y][x-i]) {chk[y][x-i]=true; breakk(y,x-i);}
			if(isIn(y,x+i,h,w) && mapCopy[y][x+i]!=0 && !chk[y][x+i]) {chk[y][x+i]=true; breakk(y,x+i);}
			if(isIn(y-i,x,h,w) && mapCopy[y-i][x]!=0 && !chk[y-i][x]) {chk[y-i][x]=true; breakk(y-i,x);}
			if(isIn(y+i,x,h,w) && mapCopy[y+i][x]!=0 && !chk[y+i][x]) {chk[y+i][x]=true; breakk(y+i,x);}
		}
		mapCopy[y][x]=0;
		cntCopy[x]--;
	}
	
	static boolean isIn(int i, int j, int y, int x) {
		if(i>=0 && j>=0 && i<y && j<x) {return true;}
		return false;
	}
}

/*

1
3 10 10
0 0 0 0 0 0 0 0 0 0
1 0 1 0 1 0 0 0 0 0
1 0 3 0 1 1 0 0 0 1
1 1 1 0 1 2 0 0 0 9
1 1 4 0 1 1 0 0 1 1
1 1 4 1 1 1 2 1 1 1
1 1 5 1 1 1 1 2 1 1
1 1 6 1 1 1 1 1 2 1
1 1 1 1 1 1 1 1 1 5
1 1 7 1 1 1 1 1 1 1

12
*/