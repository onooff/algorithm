//Main
import java.util.*;
public class bj2789 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		Set<Character> set = new HashSet<Character>();
		set.add('C');
		set.add('A');
		set.add('M');
		set.add('B');
		set.add('R');
		set.add('I');
		set.add('D');
		set.add('G');
		set.add('E');

		String s = sc.next();
		StringBuilder sb = new StringBuilder();
		int l = s.length();

		for(int i=0;i<l;i++) {
			if(!set.contains(s.charAt(i))) sb.append(s.charAt(i));
		}
		System.out.println(sb.toString());

		sc.close();
	}
}