//Main
import java.util.*;
public class bj18429 {
	static int[] arr;
	static boolean[] chk;
	static int n,k,cnt=0;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		n = sc.nextInt();
		k = sc.nextInt();
		arr = new int[n];
		chk = new boolean[n];
		for(int i=0;i<n;i++) arr[i]=sc.nextInt();

		dfs(500,0);
		System.out.println(cnt);

		sc.close();
	}

	static void dfs(int power,int chked){
		if(chked==n) {cnt++; return;}
		for(int i=0;i<n;i++) {
			if(!chk[i] && power+arr[i]-k>=500) {
				chk[i]=true;
				dfs(power+arr[i]-k,chked+1);
				chk[i]=false;
			}
		}
	}
}