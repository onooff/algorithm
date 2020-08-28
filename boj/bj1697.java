//Main
import java.util.*;
public class bj1697 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int k = sc.nextInt();

		Queue<v> q = new LinkedList<v>();
		q.offer(new v(0,n));

		v tmp;
		int min=Math.abs(k-n);
		while(!q.isEmpty()) {
			tmp = q.poll();
			if(tmp.cnt>=min) continue;
			if(tmp.p!=k) {
				if(tmp.p<k) {
					q.offer(new v(tmp.cnt+1,tmp.p+1));
					q.offer(new v(tmp.cnt+1,tmp.p*2));
				}
				if(tmp.p-1 > 0)q.offer(new v(tmp.cnt+1,tmp.p-1));
			}
			else {
				min = Math.min(tmp.cnt, min);
			}
		}
		System.out.println(min);

		sc.close();
	}
	static class v{
		int cnt;
		int p;

		public v(int cnt, int p) {
			super();
			this.cnt = cnt;
			this.p = p;
		}
	}
}