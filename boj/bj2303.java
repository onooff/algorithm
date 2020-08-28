//Main
import java.util.*;
public class bj2303 {
	static int[][] arr;
	//static boolean[][] chk;
	static int[] result;
	static int n,max=-1,maxIdx;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		n = sc.nextInt();
		arr = new int[n][5];
		//chk = new boolean[n][5];
		result = new int[n];
		for(int i=0;i<n;i++) {
			for(int j=0;j<5;j++) {
				arr[i][j] = sc.nextInt();
			}
		}

		for(int i=0;i<n;i++) {
			dfs(i,0,0,0);
		}
		for(int i=0;i<n;i++) {
			if(max<=result[i]) {max=result[i]; maxIdx=i;}
		}
		System.out.println(maxIdx+1);
		sc.close();
	}

	static void dfs(int idx, int start, int cnt, int sum) {
		if(cnt==3) {
			result[idx]=Math.max(result[idx], sum%10);
			return;
		}
		for(int i=start;i<5;i++) {
			//if(!chk[idx][i]) {
			//chk[idx][i]=true;
			dfs(idx,i+1,cnt+1,sum+arr[idx][i]);
			//chk[idx][i]=false;
			//}
		}
	}
}