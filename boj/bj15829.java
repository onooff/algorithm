//Main
import java.math.BigInteger;
import java.util.*;
public class bj15829 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		String s = sc.next();
		BigInteger hash = new BigInteger("0");
		BigInteger r = new BigInteger("31");
		BigInteger m = new BigInteger("1234567891");
		BigInteger a,bigI;
		for(int i=0;i<n;i++) {
			bigI = new BigInteger(String.valueOf(i));
			a = new BigInteger(String.valueOf((int)s.charAt(i)-'`'));
			hash = hash.add(a.multiply(r.pow(i)));
			hash.mod(m);
		}
		System.out.println(hash.mod(m));
		sc.close();
	}
}