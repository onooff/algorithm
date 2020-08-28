//Solution
import java.util.*;
public class swea4050 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();

		for(int tc=1;tc<=t;tc++) {
			
			int n = sc.nextInt();
			int[] arr = new int[n];
			for(int i=0;i<n;i++) {
				arr[i]=sc.nextInt();
			}
			
			Arrays.sort(arr);
			
			int sum=0;
			int m=arr.length-1;
			for(int i=0; i<=m; i++) {
				if((i+1)%3==0) continue;
				sum+=arr[m-i];
			}
			
			System.out.printf("#%d %d%n",tc,sum);
		}
		
		sc.close();
	}
}