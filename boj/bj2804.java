//Main
import java.util.*;
public class bj2804 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		String s1 = sc.next();
		String s2 = sc.next();
		int l1 = s1.length();
		int l2 = s2.length();

		int i1=0,i2=0;

		loop:for(int i=0; i<l1; i++) {
			for(int j=0; j<l2; j++) {
				if(s1.charAt(i)==s2.charAt(j)) {
					i1=i; i2=j; break loop;
				}
			}
		}

		for(int i=0; i<l2; i++) {
			for(int j=0; j<l1; j++) {
				if(i==i2) {System.out.print(s1.charAt(j)); continue;}
				if(j==i1) {System.out.print(s2.charAt(i)); continue;}
				System.out.print('.');
			}
			System.out.println();
		}

		sc.close();
	}
}