import java.util.*;

public class swea1966 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int t=sc.nextInt();
		for(int tc = 1;tc<=t;tc++) {
			int n=sc.nextInt();
			int[] arr = new int[n];
			
			for(int i=0;i<n;i++) {arr[i]=sc.nextInt();}
			Arrays.sort(arr);
			
			StringBuilder sb = new StringBuilder();
			sb.append("#"+tc);
			for(int i=0;i<n;i++) {sb.append(" "+arr[i]);}
			System.out.println();
		}
		sc.close();
	}
}
