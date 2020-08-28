//Solution
import java.util.*;
public class swea1953 {
	static int[][] map = new int[50][50];
	static boolean[][] chk;
	static boolean isIn(int i, int j, int y, int x) {
		if(i>=0 && j>=0 && i<y && j<x) {return true;}
		return false;
	}

	static int[][] d= {
			{-1,0},//상0
			{1,0},//햐1
			{0,-1},//좌2
			{0,1}//우3
	};

	static int[][] pipe= {
			{},
			{0,1,2,3},//상하좌우1
			{0,1},//상하2
			{2,3},//좌우3
			{0,3},//상우4
			{1,3},//하우5
			{1,2},//하좌6
			{0,2},//상좌7
	};


	static class v{
		int i;
		int j;
		public v(int i, int j) {
			super();
			this.i = i;
			this.j = j;
		}
	}

	public static void main(String[] args) {
		List<Integer>[] connect = new List[4];
		connect[0]=new ArrayList<Integer>(); connect[0].add(1); connect[0].add(2); connect[0].add(5);  connect[0].add(6);
		connect[1]=new ArrayList<Integer>(); connect[1].add(1); connect[1].add(2); connect[1].add(4);  connect[1].add(7);
		connect[2]=new ArrayList<Integer>(); connect[2].add(1); connect[2].add(3); connect[2].add(4);  connect[2].add(5);
		connect[3]=new ArrayList<Integer>(); connect[3].add(1); connect[3].add(3); connect[3].add(6);  connect[3].add(7);
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		int n,m,r,c,l,i,j,k,ni,nj,time,p,cnt;
		Queue<v> q,tmpQ;
		for(int tc=1;tc<=t;tc++) {
			q=new LinkedList<>();
			chk = new boolean[51][51];
			cnt=1;

			n=sc.nextInt();
			m=sc.nextInt();
			r=sc.nextInt();
			c=sc.nextInt();
			l=sc.nextInt();

			for(i=0;i<n;i++) {
				for(j=0;j<m;j++) {
					map[i][j] = sc.nextInt();
				}
			}

			chk[r][c]=true;
			q.offer(new v(r,c));
			v tmp;
			for(time=1;time<l;time++) {
				tmpQ=new LinkedList<>();
				while(!q.isEmpty()) {
					tmp=q.poll();
					i=tmp.i;
					j=tmp.j;
					p=map[i][j];
					//System.out.println("start"+i+" "+j+" P="+p);
					for(k=0; k<pipe[p].length; k++) {
						ni = i+d[pipe[p][k]][0];
						nj = j+d[pipe[p][k]][1];
						//System.out.println(ni+"/"+nj+"? "+isIn(ni,nj,n,m) +" "+ connect[pipe[p][k]].contains(map[ni][nj]) + connect[pipe[p][k]].toString());
						if(isIn(ni,nj,n,m) && !chk[ni][nj] && connect[pipe[p][k]].contains(map[ni][nj])) {
							chk[ni][nj]=true;
							tmpQ.offer(new v(ni,nj));
							cnt++;
						}
					}
				}
				q=tmpQ;
				//System.out.println("-------------");
			}

			System.out.printf("#%d %d%n",tc,cnt);
		}
		sc.close();
	}
}