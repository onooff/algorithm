import java.math.BigInteger;
import java.util.Scanner;

public class jo1240 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		BigInteger n = new BigInteger(sc.next());
		
		sc.close();
		
		BigInteger i=new BigInteger("2");
		while(true) {
			if(n.compareTo(i.multiply(i))==-1) {System.out.println(i.subtract(BigInteger.ONE)); return;}
			i.add(BigInteger.ONE);
		}
	}
}
