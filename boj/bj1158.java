import java.util.Scanner;

public class bj1158 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int k = sc.nextInt();
		q nowQ = new q(1);
		q tmp = nowQ;

		for(int i=2; i<=n; i++) {
			q newQ = new q(i);
			nowQ.next=newQ;
			newQ.prev=nowQ;
			nowQ=newQ;
		}
		nowQ.next=tmp;
		tmp.prev=nowQ;
		nowQ=tmp;
		
		StringBuilder sb = new StringBuilder("<");
		
		for(int i=1;i<=n;i++) {
			for(int j=1;j<k;j++) {
				nowQ=nowQ.next;
			}
			if(i==n) sb.append(nowQ.val+">");
			else sb.append(nowQ.val+", ");
			
			nowQ.next.prev = nowQ.prev;
			nowQ.prev.next = nowQ.next;
			nowQ=nowQ.next;
		}
		
		System.out.println(sb.toString());
		
		sc.close();
	}

	static class q{
		q prev;
		q next;
		int val;
		public q(int val) {
			super();
			this.val = val;
		}
	}
}