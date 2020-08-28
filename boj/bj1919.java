//Main
import java.util.*;
public class bj1919 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		String s1 = sc.next();
		String s2 = sc.next();
		int[] arr1 = new int[26];
		int[] arr2 = new int[26];

		int i,l;
		l=s1.length();
		for(i=0;i<l;i++) {
			arr1[s1.charAt(i)-'a']++;
		}
		l=s2.length();
		for(i=0;i<l;i++) {
			arr2[s2.charAt(i)-'a']++;
		}

		int sum = 0;
		for(i=0;i<26;i++) {
			sum+=Math.abs(arr1[i]-arr2[i]);
		}

		System.out.println(sum);

		sc.close();
	}
}