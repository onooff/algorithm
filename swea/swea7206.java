//Solution
import java.util.*;
public class swea7206 {
	static Queue<node> q;
	static int max;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int t = sc.nextInt();

		for(int tc=1;tc<=t;tc++) {
			//			String s = "12345";//01234
			//			System.out.println(Integer.parseInt(s.substring(0, 1)));
			//			System.out.println(Integer.parseInt(s.substring(1, 5)));
			q = new LinkedList<>();
			max=-1;

			q.offer(new node(sc.next(),0));

			node tmp;
			int l,i;
			while(!q.isEmpty()) {
				tmp = q.poll();
				if(tmp.s.length()==1) {
					max = Math.max(max, tmp.cnt);
				}
				else {
//					l=tmp.s.length();
//					for(i=1;i<l;i++) {
//						q.offer(new node(String.valueOf(
//							Integer.parseInt(tmp.s.substring(0, i)) * Integer.parseInt(tmp.s.substring(i, l))
//						),tmp.cnt+1));
//					}
					dfs(tmp.s,tmp.cnt);
				}
			}

			System.out.printf("#%d %d%n",tc,max);
		}

		sc.close();
	}
	static class node{
		String s;
		int cnt;
		public node(String s, int cnt) {
			this.s = s;
			this.cnt = cnt;
		}
	}
	static void dfs(String s, int cnt) {
		
	}
}