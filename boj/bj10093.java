//Main
import java.math.BigInteger;
import java.util.*;
public class bj10093 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		BigInteger a = new BigInteger(sc.next());
		BigInteger b = new BigInteger(sc.next());
		if(a.compareTo(b)>0) {
			BigInteger tmp = a;
			a=b;
			b=tmp;
		}
		int range = Integer.parseInt(b.subtract(a).toString())-1;
		if(range==-1) range=0;
		System.out.println(range);
		for(long i=0;i<range;i++) {
			a=a.add(BigInteger.ONE);
			System.out.print(a+" ");
		}
		sc.close();
	}
}