//Main
import java.util.*;
public class bj1874 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int[] arr = new int[n];

		for(int i=0;i<n;i++) arr[i]=sc.nextInt();

		int idx = 0;
		int num = 1;
		Stack<Integer> s = new Stack<Integer>();
		s.push(num++);
		StringBuilder sb = new StringBuilder("+\n");

		while(num<=n || !s.isEmpty()) {
			if(!s.isEmpty() && idx<n && s.peek()==arr[idx]) {
				s.pop();
				sb.append("-\n");
				idx++;
				continue;
			}
			if(num>n && !s.isEmpty()) {System.out.println("NO"); return;}
			s.push(num++);
			sb.append("+\n");
		}

		System.out.println(sb.toString());
		sc.close();
	}
}