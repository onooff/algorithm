//Main
import java.util.*;
public class bj2161 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();

		Queue<Integer> q = new LinkedList<Integer>();
		List<Integer> list = new ArrayList<Integer>();
		for(int i=1;i<=n;i++) {
			q.add(i);
		}

		while(q.size()>1) {
			list.add(q.poll());
			q.add(q.poll());
		}
		list.add(q.poll());

		for(int result:list) System.out.print(result+" ");

		sc.close();
	}
}