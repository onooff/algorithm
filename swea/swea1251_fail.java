import java.util.*;
public class swea1251_fail {
	static int n;
	static double e;
	static int[] order;
	//static long[] l;
	static boolean[] chk;
	static List<v> vList  = new ArrayList<>();
	static long min;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();

		for(int tc=1;tc<=t;tc++) {
			n = sc.nextInt();
			order = new int[n];
			//l = new long[n-1];
			chk = new boolean[n];
			vList.clear();
			min = Long.MAX_VALUE;
			
			for(int i=0;i<n;i++) {
				vList.add(new v());
				vList.get(i).x = sc.nextInt();
			}
			for(int i=0;i<n;i++) {
				vList.get(i).y = sc.nextInt();
			}
			e=sc.nextDouble();
			
			makeOrder(0);
			
			System.out.printf("#%d %d%n",tc,min);
		}
		
		sc.close();
	}
	
	static void makeOrder(int idx) {
		if(idx==n) {
			//System.out.println(Arrays.toString(order));//dbg
			calc(0,0);
			return;
		}
		
		for(int i=0;i<n;i++) {
			if(!chk[i]) {
				chk[i]=true;
				order[idx]=i;
				makeOrder(idx+1);
				chk[i]=false;
			}
		}
	}
	
	static void calc(int idx, long sum) {
		if(sum>min) return;
		if(idx==n-1) {
			//System.out.println(sum);//dbg
			if(min>sum) min=sum;
			return;
		}
		long nx = Math.abs(vList.get(order[idx]).x-vList.get(order[idx+1]).x);
		long ny = Math.abs(vList.get(order[idx]).y-vList.get(order[idx+1]).y);
		sum+=Math.round(e*((nx*nx)+(ny*ny)));
//		l[idx]=
//		sum+=
//		Math.round((
//			Math.pow(Math.abs(vList.get(idx).x-vList.get(idx+1).x),2)+
//			Math.pow(Math.abs(vList.get(idx).y-vList.get(idx+1).y),2)
//		)*e);
		calc(idx+1,sum);
	}

	static class v{
		int x;
		int y;
	}
}