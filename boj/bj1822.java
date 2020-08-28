//Main
import java.util.*;
public class bj1822 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n=sc.nextInt();
		int m=sc.nextInt();
		int[] arr1 = new int[n];
		int[] arr2 = new int[m];

		for(int i=0;i<n;i++) {
			arr1[i] = sc.nextInt();
		}
		for(int i=0;i<m;i++) {
			arr2[i] = sc.nextInt();
		}

		Set<Integer> set = new HashSet<Integer>();
		for(int tmp : arr2) {
			set.add(tmp);
		}

		Set<Integer> ans = new TreeSet<Integer>();
		for(int tmp : arr1) {
			if(set.add(tmp)) {
				ans.add(tmp);
			}
		}

		StringBuilder sb = new StringBuilder();
		System.out.println(ans.size());

		for(int tmp : ans) {
			sb.append(tmp+" ");
		}
		System.out.println(sb.toString());

		sc.close();
	}
}