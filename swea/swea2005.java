//Solution
import java.util.*;
public class swea2005 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		int n,i,j;
		int[][] arr = new int[10][10];
		for(i=0;i<10;i++) {
			for(j=0;j<=i;j++) {
				if(j==0 || j==i) arr[i][j]=1;
				else arr[i][j]=arr[i-1][j]+arr[i-1][j-1];
			}
		}
		StringBuilder sb;

		for(int tc=1;tc<=t;tc++) {
			n = sc.nextInt()-1;
			sb=new StringBuilder("#"+tc+"\n");
			for(i=0;i<=n;i++) {
				for(j=0;j<=i;j++) {
					sb.append(arr[i][j]+" ");
				}
				sb.append("\n");
			}
			System.out.print(sb.toString());
		}
		sc.close();
	}
}