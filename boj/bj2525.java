//Main
import java.util.*;
public class bj2525 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int h = sc.nextInt();
		int m = sc.nextInt();

		m+=sc.nextInt();

		int hh = m/60;
		m=m%60;

		h=(h+hh)%24;

		System.out.println(h+" "+m);

		sc.close();
	}
}