//Main
import java.util.*;
public class bj2609 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int gcd=1;

		int a = sc.nextInt();
		int b = sc.nextInt();

		int aa = a;
		int bb = b;

		while(true) {
			if(aa>bb) {
				if(aa%bb==0) {gcd=bb; break;}
				else aa=aa%bb;
			}
			else {
				if(bb%aa==0) {gcd=aa; break;}
				else bb=bb%aa;
			}
		}

		System.out.println(gcd);
		System.out.println((a/gcd)*(b/gcd)*gcd);

		sc.close();
	}
}