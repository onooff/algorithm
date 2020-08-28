import java.util.*;

public class bj15649 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int m = sc.nextInt();
		boolean[] v = new boolean[n+1];
		dfs(n,m,v,"");
		sc.close();
	}

	private static void dfs(int n, int m, boolean[] v, String string) {
		if(m==0) {System.out.println(string); return;}
		
		for(int i=1;i<=n;i++) {
			if(v[i]) {continue;}
			v[i]=true;
			dfs(n,m-1,v,string+i+" ");
			v[i]=false;
		}		
	}
}
