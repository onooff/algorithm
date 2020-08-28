import java.util.*;

public class swea1251_kruskal {
	static int n,cnt;
	static double e;
	static int[] vtx;
	static List<v> vList  = new ArrayList<>();
	static List<edge> eList  = new ArrayList<>();
	static double min;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int t = sc.nextInt();

		for(int tc=1;tc<=t;tc++) {
			n = sc.nextInt();
			cnt = n;
			vtx = new int[n];
			vList.clear();
			eList.clear();
			min = 0;

			for(int i=0;i<n;i++) {
				vtx[i]=i;
				vList.add(new v(sc.nextInt(),0));
				//vList.get(i).x = sc.nextInt();
			}

			for(int i=0;i<n;i++) {
				vList.get(i).y = sc.nextInt();
			}
			
			e = sc.nextDouble();
			
			long nx,ny;
			double nl;
			for(int i=0;i<n;i++) {
				for(int j=0;j<i;j++) {
					nx = Math.abs(vList.get(i).x-vList.get(j).x);
					ny = Math.abs(vList.get(i).y-vList.get(j).y);
					//nl = Math.round(e*((nx*nx)+(ny*ny)));
					nl = e*((nx*nx)+(ny*ny));
					//System.out.println(nx+" "+ny+" "+l);//dbg
					eList.add(new edge(i,j,nl));
				}
			}
			
			Collections.sort(eList, new Comparator<edge>() {
				public int compare(edge e1, edge e2) {
					int ee1,ee2;
					if(e1.l<e2.l) {ee1=1; ee2=2;}
					else if(e1.l==e2.l) {ee1=1; ee2=1;}
					else {ee1=2; ee2=1;}

					return ee1-ee2;
				}
			});

			greedy();

			System.out.printf("#%d %d%n",tc,Math.round(min));
		}

		sc.close();
	}

	static void greedy() {
		int size = eList.size();

		for(int i=0;i<size;i++) {
			if(!union(eList.get(i).v1, eList.get(i).v2)) continue;
			
			min+=eList.get(i).l;
			if(cnt==1) break;
		}
	}

	static boolean union(int x,int y) {
		x=findSet(x);
		y=findSet(y);
		if(x==y) {return false;}
		vtx[y]=x; cnt--;
		return true;
	}

	static int findSet(int x) {
		if(x==vtx[x]) {
			return x;
		}
		int px = findSet(vtx[x]);
		vtx[x] = px;
		return vtx[x];
	}

	static class edge{
		int v1;
		int v2;
		double l;
		public edge(int v1, int v2, double nl) {
			super();
			this.v1 = v1;
			this.v2 = v2;
			this.l = nl;
		}
	}

	static class v{
		int x;
		int y;
		public v(int x, int y) {
			super();
			this.x = x;
			this.y = y;
		}
	}
}