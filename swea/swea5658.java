import java.util.*;

public class swea5658 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int t = sc.nextInt();

		for(int tc=1;tc<=t;tc++) {

			int n = sc.nextInt();
			int k = sc.nextInt();
			char[] str = sc.next().toCharArray();

			Set<Integer> set = new TreeSet<Integer>();
			int length = n/4;
			int idx = 0;

			for(int l=0;l<length;l++) {
				for(int i=0;i<4;i++) {
					StringBuilder tmp = new StringBuilder();
					for(int j=0;j<length;j++) {
						tmp.append(str[idx++%n]);
					}
					set.add(Integer.parseInt(tmp.toString(),16));
				}
				idx++;
			}
			Iterator<Integer> it = set.iterator();
			idx = set.size()-k;
			for(int i=0;i<idx;i++) {
				it.next();
			}
			System.out.printf("#%d %d%n",tc, it.next());
		}
		sc.close();
	}
}