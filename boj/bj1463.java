//Main
import java.util.*;
public class bj1463 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		Queue<node> q = new LinkedList<node>();
		q.offer(new node(sc.nextInt(),0));
		
		node tmp;
		while(true) {
			tmp=q.poll();
			if(tmp.val==1) break;
				
			if(tmp.val%3==0) q.offer(new node(tmp.val/3,tmp.cnt+1));
			if(tmp.val%2==0) q.offer(new node(tmp.val/2,tmp.cnt+1));
			q.offer(new node(tmp.val-1,tmp.cnt+1));
		}
		System.out.println(tmp.cnt);
		sc.close();
	}
	
	static class node{
		int val;
		int cnt;
		public node(int val, int cnt) {
			super();
			this.val = val;
			this.cnt = cnt;
		}
	}
}