import java.util.*;
public class bj11866 {
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
		nowQ = nowQ.prev;

		StringBuilder sb = new StringBuilder("<");

		for(int i=1;i<=n;i++) {
			for(int j=0;j<k;j++) {
				nowQ=nowQ.next;
			}
			sb.append(nowQ.val);
			if(i!=n) sb.append(", ");

			nowQ.next.prev = nowQ.prev;
			nowQ.prev.next = nowQ.next;
			nowQ = nowQ.prev;
		}
		sb.append('>');
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