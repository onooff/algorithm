//Main
import java.util.*;
public class bj14584 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String cip = sc.nextLine();
		int n = Integer.parseInt(sc.nextLine());
		String[] words = new String[n];
		
		for(int i=0;i<n;i++) {
			words[i]=sc.nextLine();
		}
		String result = null;
		loop : for(int i=0;i<26;i++) {
			result = k(cip,i);
			for(int j=0;j<n;j++) {
				if(result.contains(words[j])) break loop;
			}
		}
		System.out.println(result);
		sc.close();
	}

	private static String k(String cip, int n) {
		char[] tmp = cip.toCharArray();
		StringBuilder sb = new StringBuilder();
		int nc;
		for(int i=0;i<tmp.length;i++) {
			nc = tmp[i]+n;
			if(nc>122) nc= nc-26;
			sb.append((char)nc);
		}
		return sb.toString();
	}
}