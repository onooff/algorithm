//Main
import java.math.BigInteger;
import java.util.*;
public class bj1271 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		BigInteger a = new BigInteger(sc.next());
		BigInteger b = new BigInteger(sc.next());

		System.out.println(a.divide(b));
		System.out.println(a.mod(b));
		sc.close();
	}
}