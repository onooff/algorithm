//Solution
import java.util.*;
public class swea9370 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		for(int tc=1;tc<=t;tc++) {
			int max = Integer.MIN_VALUE;
			int sum = 0;
			int n = sc.nextInt();

			int[] arr = new int[n];
			for(int i=0;i<n;i++) {
				arr[i] = sc.nextInt();
			}
			for(int i=n-1;i>=0;i--) {
				if(max<arr[i]) max=arr[i];
				else sum+=max-arr[i];
			}
			System.out.printf("#%d %d%n",tc,sum);
		}
		sc.close();
	}
}

/*
3
3
10 7 6
3
3 5 9
5
1 1 3 1 2

0
10
5
 */