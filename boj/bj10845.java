//Main
import java.util.*;
public class bj10845 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		List<Integer> q = new ArrayList<Integer>();

		int n = sc.nextInt();
		for(int i=0; i<n; i++) {
			String s = sc.next();
			switch(s) {
			case "push":{
				q.add(sc.nextInt());
				break;
			}
			case "pop":{
				if(q.isEmpty()) System.out.println("-1");
				else System.out.println(q.remove(0));
				break;
			}
			case "size":{
				System.out.println(q.size());
				break;
			}
			case "empty":{
				if(q.isEmpty()) System.out.println('1');
				else System.out.println('0');
				break;
			}
			case "front":{
				if(q.isEmpty()) System.out.println("-1");
				else System.out.println(q.get(0));
				break;
			}
			case "back":{
				if(q.isEmpty()) System.out.println("-1");
				else System.out.println(q.get(q.size()-1));
			}
			}
		}

		sc.close();
	}
}