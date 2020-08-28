//1/31, 2/28, 3/31, 4/30, 5/31, 6/30, 7/31, 8/31, 9/30, 10/31, 11/30, 12/31

import java.util.*;

public class swea1948 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] day = {0,31,28,31,30,31,30,31,31,30,31,30,31};
		int m1,d1,m2,d2;
		
		int t=sc.nextInt();
		for(int tc = 1;tc<=t;tc++) {
			m1=sc.nextInt();
			d1=sc.nextInt();
			m2=sc.nextInt();
			d2=sc.nextInt();
			
			for(int i=1;i<m1;i++) {
				d1+=day[i];
			}
			for(int i=1;i<m2;i++) {
				d2+=day[i];
			}
			System.out.printf("#%d %d%n",tc,d2-d1+1);
		}
		
		sc.close();
	}
}
