import java.util.*;
public class swea7701 {
	static Set<String> set = new HashSet<>(); 
	static List<String> list = new LinkedList<>();

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int t = Integer.parseInt(sc.nextLine());

		for(int tc=1;tc<=t;tc++) {
			set.clear();
			list.clear();
			int n = Integer.parseInt(sc.nextLine());

			for(int i=0;i<n;i++) {
				set.add(sc.nextLine());
			}

			for(String s : set) {
				list.add(s);
			}
			Collections.sort(list);
			Collections.sort(list, new Comparator<String>(){
				public int compare(String s1, String s2){
					return Integer.compare(s1.length(), s2.length());
				}
			});

			StringBuilder sb = new StringBuilder();
			sb.append(String.format("#%d%n",tc));
			for(String s : list) {
				sb.append(s+"%n");
			}
			System.out.println(sb);
		}
		sc.close();
	}
}