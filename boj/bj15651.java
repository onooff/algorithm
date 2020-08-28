//Main
import java.util.*;
public class bj15651 {
	static int N,M;
	static int[] arr;
	static boolean[] chk;
	static Set<String> set = new HashSet<String>();
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		N = sc.nextInt();
		M = sc.nextInt();
		arr = new int[N];
		chk = new boolean[N];
		for(int i=0;i<N;i++) {
			arr[i] = sc.nextInt();
		}
		Arrays.sort(arr);
		
		p("",0,0);

		sc.close();
	}

	static void p(String s, int ii, int n) {
		if(n>=M) {
			if(set.add(s)) System.out.println(s);
			return;
		}
		for(int i=ii;i<N;i++) {
			//if(chk[i]) continue;
			//else{
				//chk[i]=true;
				p(s+arr[i]+" ", i, n+1);
				//chk[i]=false;
			//}
		}
	}
}