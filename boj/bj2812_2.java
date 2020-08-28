//친구들에게 고맙다
import java.util.*;

public class bj2812_2 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int k = sc.nextInt();
		//int num = sc.nextInt();
		sc.nextLine();
		char[] arr = sc.nextLine().toCharArray();
		Stack<Integer> s = new Stack<>();
		
		s.push(arr[0]-'0');
		for(int i=1;i<arr.length;i++) {
			
			while(!s.isEmpty() && s.peek()<arr[i]-'0' && k!=0) {
				s.pop(); k--;
			}
			s.push(arr[i]-'0');
		}
		
		for(int i=k;k>0;k--) {s.pop();}
		
		int size = s.size();
		for(int i=0;i<size;i++) {
			System.out.print(s.get(i));
		}
	}
}