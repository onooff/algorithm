import java.util.*;
public class swea1181 {
	static Set<String> set = new HashSet<>(); 
	static List<String> list = new LinkedList<>();

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

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

		for(String s : list) {
			System.out.println(s);
		}
		sc.close();
	}
}