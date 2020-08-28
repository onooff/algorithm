import java.util.*;
public class bj1021 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int m = sc.nextInt();
		q nowQ = new q(1);
		q tmp = nowQ;
		int sum=0;

		for(int i=2; i<=n; i++) {
			q newQ = new q(i);
			nowQ.next=newQ;
			newQ.prev=nowQ;
			nowQ=newQ;
		}
		nowQ.next=tmp;
		tmp.prev=nowQ;
		nowQ=tmp;

		int finding,next,prev,min;
		q tmpN,tmpP;
		for(int i=0;i<m;i++) {
			finding = sc.nextInt();
			next=0;
			prev=0;

			tmpN=nowQ;
			while(tmpN.val!=finding) {
				tmpN=tmpN.next;
				next++;
			}
			tmpP=nowQ;
			while(tmpP.val!=finding) {
				tmpP=tmpP.prev;
				prev++;
			}

			if(next>=prev) {
				nowQ=tmpP.next;
				tmpP.next.prev = tmpP.prev;
				tmpP.prev.next = tmpP.next;
				sum+=prev;
			}
			else {//next<prev
				nowQ=tmpN.next;
				tmpN.next.prev = tmpN.prev;
				tmpN.prev.next = tmpN.next;
				sum+=next;
			}
		}
		System.out.println(sum);

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

/*
10 3
1 2 3
 */