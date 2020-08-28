//Main
import java.util.*;
public class bj2587 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int sum=0,tmp;
		List<Integer> list = new ArrayList<Integer>();

		for(int i=0;i<5;i++) {
			tmp=sc.nextInt();
			sum+=tmp;
			list.add(tmp);
		}
		Collections.sort(list);

		System.out.println(sum/5);
		System.out.println(list.get(list.size()/2));
		sc.close();
	}
}