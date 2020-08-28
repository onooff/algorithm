import java.util.*;

public class swea5656_fail {
	static List<Integer>[] map = null;
	static List<Integer>[] mapCopy = null;
	static int[] ball = null;
	static int n,w,h;
	static int min = Integer.MAX_VALUE;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int t = sc.nextInt();

		for(int tc=1;tc<=t;tc++) {
			n = sc.nextInt();
			w = sc.nextInt();
			h = sc.nextInt();
			map = new List[w];
			ball = new int[n];

			for(int i=0;i<w;i++) {
				map[i] = new LinkedList<Integer>();
			}

			int tmp;
			for(int i=0;i<h;i++) {
				for(int j=0;j<w;j++) {
					tmp = sc.nextInt();
					if(tmp==0) continue;
					map[j].add(tmp);
				}
			}
			for(int i=0;i<h;i++) {
				Collections.reverse(map[i]);//0이 맨아래로 만듦
			}

			shot(0);

			System.out.printf("#%d %d%n",tc,min); min=Integer.MAX_VALUE;
		}

		sc.close();
	}
	private static void shot(int ballIdx) {
		if(ballIdx==n) {
			mapCopy = new List[w];
			for(int j=0;j<w;j++) {
				mapCopy[j] = new LinkedList<Integer>();
				mapCopy[j].addAll(map[j]);
			}
			System.out.print(Arrays.toString(ball));
			shoot(0); 
			return;
		}
		for(int i=0;i<w;i++) {
			ball[ballIdx]=i;
			shot(ballIdx+1);
		}
	}

	static void shoot(int cnt) {
		if(cnt==n) {
			int tmp=0;
			for(int i=0;i<w;i++) {
				if(mapCopy[i].isEmpty()) continue;
				tmp+=mapCopy[i].size();
			}
			if(min>tmp) min=tmp;
			System.out.println("min="+tmp); //debug
			return;
		}
		
		int x = ball[cnt];
		if(mapCopy[x].isEmpty()) {shoot(n); return;}

		breakk(x, mapCopy[x].size()-1);
		shoot(cnt+1);
	}

	private static boolean breakk(int x, int y) {
		if(y<0 || mapCopy[x].isEmpty() || y>=mapCopy[x].size()) return false;
		//System.out.println(x+" "+y); //debug
		Integer range = mapCopy[x].get(y);
		//System.out.println(x+" "+y+" "+range); //debug

		//for(int i=range-1; i>0; i--) {
		for(int i=0; i<range-1; i--) {
			if(isIn(x-i)) breakk(x-i, y);
			if(isIn(x+i)) breakk(x+i, y);
			if(y-i>=0) {if(breakk(x, y-i)) y--;}
			if(y+i<mapCopy[x].size()) breakk(x, y+i);
		}
		
		mapCopy[x].remove((int)y);
		return true;
	}

	static boolean isIn(int x) {
		if(x>=0 && x<w) return true;
		else return false;
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