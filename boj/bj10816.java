//Main
import java.util.*;
public class bj10816 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Map<Integer, Integer> map = new HashMap<Integer, Integer>();
		int n = sc.nextInt();

		int tmp;
		for(int i=0;i<n;i++) {
			tmp=sc.nextInt();
			if(!map.containsKey(tmp)) map.put(tmp, 1);
			else map.put(tmp, map.get(tmp)+1);
		}

		StringBuilder sb = new StringBuilder();
		int m = sc.nextInt();
		for(int i=0;i<m;i++) {
			tmp=sc.nextInt();
			if(!map.containsKey(tmp)) sb.append("0 ");
			else sb.append(map.get(tmp)+" ");
		}
		System.out.println(sb.toString());

		sc.close();
	}
}