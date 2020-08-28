//Main
import java.util.Scanner;
public class bj15650 {
	static int N,M;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		N = sc.nextInt();
		M = sc.nextInt();
		p("",0,0);
		
		sc.close();
	}
	
	static void p(String s, int ii, int n) {
		if(n>=M) {System.out.println(s); return;}
		for(int i=ii+1;i<=N;i++) {
			p(s+i+" ", i, n+1);
		}
	}
}