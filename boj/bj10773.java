//Main
import java.util.*;
public class bj10773 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		Stack<Integer> s = new Stack<Integer>();
		int n = sc.nextInt();

		int tmp;
		for(int i=0;i<n;i++) {
			tmp=sc.nextInt();
			if(tmp==0) {
				s.pop();
			}
			else {
				s.push(tmp);
			}
		}

		int sum=0;
		while(!s.isEmpty()) {
			sum+=s.pop();
		}
		System.out.println(sum);

		sc.close();
	}
}