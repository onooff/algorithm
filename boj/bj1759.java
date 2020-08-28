//Main
import java.util.*;
public class bj1759 {
	static String[] arr;
	static boolean[] chk;
	static int l,n;
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		l = sc.nextInt();
		n = sc.nextInt();
		sc.nextLine();
		arr = sc.nextLine().split(" ");
		Arrays.sort(arr);
		chk = new boolean[n];
		
		
		dfs("",0,0,0,0);
		System.out.println(sb);
		
		sc.close();
	}
	
	static void dfs(String tmp, int idx, int length, int 모음, int 자음){
		if(length==l) {
			if(모음==0 || 자음<2) return;
			sb.append(tmp);
			sb.append(String.format("\n"));
			return;
		}
		
		for(int i=idx; i<n; i++) {
			if(chk[i]) continue;
			
			chk[i]=true;
			if("a".equals(arr[i]) || "e".equals(arr[i]) || "i".equals(arr[i]) || "o".equals(arr[i]) || "u".equals(arr[i])) dfs(tmp+arr[i],i,length+1,모음+1,자음);
			else dfs(tmp+arr[i],i,length+1,모음,자음+1);
			chk[i]=false;
		}
	}
}
