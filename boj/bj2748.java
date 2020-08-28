//Main
import java.util.*;
public class bj2748 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();

		long[] p = new long[n+3];

		p[1] = 1;
		p[2] = 1;

		for(int i=3;i<=n;i++) {
			p[i] = p[i-1]+p[i-2];
		}

		System.out.println(p[n]);

		sc.close();
	}
}