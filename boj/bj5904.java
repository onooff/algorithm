//Main
import java.util.*;
public class bj5904 {
	static int n;
	static StringBuilder sb  = new StringBuilder("moo");
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		n = sc.nextInt();
		
		dfs();
		System.out.println(sb.charAt(n-1));
		
		sc.close();
	}
	static void dfs() {
		if(n<sb.length()) return;
		n-=sb.length();
		sb.append(sb);
		sb.insert(1, 'o');
		//System.out.println(n);
		dfs();
	}
}