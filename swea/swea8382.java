import java.util.*;
public class swea8382 {
	
	static int x1,y1,x2,y2;
	static Queue<v> q = new LinkedList<v>();
	static boolean[][] chk = new boolean[201][201];
	static int min = Integer.MAX_VALUE;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();

		for(int tc=1;tc<=t;tc++) {
			
			x1=sc.nextInt()+100;
			y1=sc.nextInt()+100;
			x2=sc.nextInt()+100;
			y2=sc.nextInt()+100;
			
			if(x1==x2 && y1==y2) {System.out.printf("#%d %d%n",tc,0); continue;}
			
			bfs(false);
			bfs(true);
			
			System.out.printf("#%d %d%n",tc,min);
			min = Integer.MAX_VALUE;
		}
		sc.close();
	}
	
	private static void bfs(boolean startD) {
		chk[x1][y1] = true;
		q.offer(new v(x1,y1,startD,0));
		
		while(!q.isEmpty()){
			v tmp = q.poll();
			int y = tmp.y;
			int x = tmp.x;
			if(x==x2 && y==y2) {
				if(min>tmp.cnt) min=tmp.cnt;
				q.clear();
				break;
			}
			
			if(tmp.d) {//true 가로로 이동, false 세로
				if(isIn(y,x-1,201,201) && !chk[y][x-1]) {
					chk[y][x-1] = true;
					q.offer(new v(x-1,y,false,tmp.cnt+1));
				}
				if(isIn(y,x+1,201,201) && !chk[y][x+1]) {
					chk[y][x+1] = true;
					q.offer(new v(x+1,y,false,tmp.cnt+1));
				}
			}
			else {
				if(isIn(y-1,x,201,201) && !chk[y-1][x]) {
					chk[y-1][x] = true;
					q.offer(new v(x,y-1,true,tmp.cnt+1));
				}
				if(isIn(y+1,x,201,201) && !chk[y+1][x]) {
					chk[y+1][x] = true;
					q.offer(new v(x,y+1,true,tmp.cnt+1));
				}
			}
		}
		for(int i=0;i<chk.length;i++) {Arrays.fill(chk[i], false);}
	}
	
	static boolean isIn(int i, int j, int y, int x) {
		if(i>=0 && j>=0 && i<y && j<x) {return true;}
		return false;
	}
	
	static class v{
		int x;
		int y;
		boolean d;
		int cnt;
		public v(int x, int y, boolean d, int cnt) {
			super();
			this.x = x;
			this.y = y;
			this.d = d;
			this.cnt = cnt;
		}
	}
}