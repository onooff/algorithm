import java.util.*;

public class bj1786 {
	static int cnt = 0;
	static StringBuilder r = new StringBuilder();
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String parent = sc.nextLine();
		String pattern = sc.nextLine();
		KMP(parent, pattern);

		System.out.println(cnt);
		System.out.println(r);

		sc.close();
	}

	static int[] getPi(String pattern) {
		int[] pi = new int[pattern.length()];

		int j = 0;
		for (int i = 1; i < pattern.length(); i++) {

			while (j > 0 && pattern.charAt(i) != pattern.charAt(j)) {
				j = pi[j - 1];
			}
			if (pattern.charAt(i) == pattern.charAt(j)) {
				pi[i] = ++j;
			}
		}
		return pi;
	}

	static void KMP(String parent, String pattern) {
		int[] table = getPi(pattern);
		int j = 0; 
		for(int i = 0 ; i< parent.length(); i++) {
			while(j >0 && parent.charAt(i) != pattern.charAt(j)) {
				j = table[j - 1];
			}
			if(parent.charAt(i) == pattern.charAt(j)) {
				if(j == pattern.length()-1) {
					cnt++;
					r.append(String.format("%d\n", (i-pattern.length()+2)));
					j = table[j];
				}else {
					j++;
				}
			}
		}
	}
}
