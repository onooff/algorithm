//Main
import java.util.*;
public class bj5532 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int l = sc.nextInt();
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		int d = sc.nextInt();
		
		while(true) {
			a-=c;
			b-=d;
			l--;
			if(a<=0 && b<=0) break;
		}
		System.out.println(l);
		
		sc.close();
	}
}