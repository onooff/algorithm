//Main
import java.util.*;
public class bj1182 {
	static int N,S,cnt=0;
	static int[] arr;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		N = sc.nextInt();
		S = sc.nextInt();
		arr = new int[N];

		for(int i=0;i<N;i++) {
			arr[i]=sc.nextInt();
		}

		for(int i=1;i<=N;i++) {
			dfs(i,0,0);
		}

		System.out.println(cnt);

		sc.close();
	}

	static void dfs(int num, int now, int sum) {
		if(num==now) {
			if(sum==S) cnt++;
			return;
		}

		for(int i=now;i<N;i++) {
			dfs(num,i+1,sum+arr[i]);
		}
	}
}