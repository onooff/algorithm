//Solution
import java.util.*;
public class swea6109 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();

		for(int tc=1;tc<=t;tc++) {
			int n = sc.nextInt();
			String s = sc.next();
			int[][] arr = new int [n][n];
			
			for(int i=0;i<n;i++) {
				for(int j=0;j<n;j++) {
					arr[i][j] = sc.nextInt();
				}
			}
			
			
			
			System.out.printf("#%d %d%n",tc,tc);
		}
		
		sc.close();
	}
}
