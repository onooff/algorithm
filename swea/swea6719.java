import java.util.*;
public class swea6719 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();

		for(int tc=1;tc<=t;tc++) {
			
			int n = sc.nextInt();
			int k = sc.nextInt();
			
			int[] m = new int[n];
			
			for(int i=0;i<n;i++) {
				m[i] = sc.nextInt();
			}
			
			Arrays.sort(m);
			double a = 0;
			
			for(int i=k;i>0;i--) {
				a=((double)a+m[n-i])/2;
			}
			
			System.out.printf("#%d %f%n",tc,a);
		}
		
		sc.close();
	}
}