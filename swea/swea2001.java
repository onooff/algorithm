//Solution
import java.util.*;
public class swea2001 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		int[][] arr;
		int i,j,a,b,sum,max;
		for(int tc=1;tc<=t;tc++) {
			int n=sc.nextInt();
			int m=sc.nextInt();
			max=0;

			arr = new int[n][n];

			for(i=0;i<n;i++) {
				for(j=0;j<n;j++) {
					arr[i][j] = sc.nextInt();
				}
			}

			for(i=0;i<=n-m;i++) {
				for(j=0;j<=n-m;j++) {
					sum=0;
					for(a=i;a<i+m;a++) {
						for(b=j;b<j+m;b++) {
							sum+=arr[a][b];
						}
					}
					max=Math.max(max, sum);
				}
			}

			System.out.printf("#%d %d%n",tc,max);
		}
		sc.close();
	}
}