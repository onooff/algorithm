//Main
import java.util.*;
public class bj1297 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		double a = sc.nextDouble();
		double b = sc.nextDouble();
		double c = sc.nextDouble();
		double r = Math.sqrt((a*a)/(b*b+c*c));
		System.out.print((int)(r*b)+" ");
		System.out.print((int)(r*c));
		sc.close();
	}
}