import java.util.*;

public class bj2846 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Stack<Integer> s = new Stack<>();
		
		int n = sc.nextInt();
		int tmp,l=0,best=Integer.MIN_VALUE;
		
		for(int i=0;i<n;i++) {
			tmp=sc.nextInt();
			if(s.isEmpty()) {l=tmp; s.push(tmp); continue;}
			
			if(s.peek()>=tmp) {
				if(best<s.peek()-l) {best=s.peek()-l;}
				s.clear();
				l=tmp; s.push(tmp);
				continue;
			}
			s.push(tmp);
		}
		if(best<s.peek()-l) {best=s.peek()-l;}
		
		System.out.println(best);
		sc.close();
	}
}