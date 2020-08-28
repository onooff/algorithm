//Main
import java.util.*;
public class bj1629{
	static long a,b,c;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		a = sc.nextInt();
		b = sc.nextInt();
		c = sc.nextInt();


		System.out.println(myPow(a,b));

		sc.close();
	}

	static long myPow(long base, long exp) {

		if(exp == 0) {return 1;}
		if(exp == 1) {return base%c;}

		long su = myPow(base, exp/2);

		su=(su*su)%c;
		if(exp%2==1) {su=(su*base)%c;}     

		return su;
	}
}