//Main
import java.util.*;
public class bj11053 {
	static int n,max=Integer.MIN_VALUE;
	static int[] arr;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		n = sc.nextInt();
		arr = new int[n];

		for(int i=0;i<n;i++) {
			arr[i]=sc.nextInt();
		}

		dfs(-1,0,0);
		System.out.println(max);
		sc.close();
	}
	static void dfs(int last, int idx, int cnt) {
		if(cnt+(n-idx)<max) return;
		for(int i=idx; i<n;i++) {
			if(last<arr[i]) dfs(arr[i], i+1, cnt+1);
		}
		System.out.println("1");
		max=Math.max(max, cnt);
	}
}