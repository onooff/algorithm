//Main
import java.util.*;
public class bj2783 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		double min = Double.MAX_VALUE;

		min = Math.min(min, sc.nextDouble()/sc.nextDouble());

		int n = sc.nextInt();

		for(int i=0;i<n;i++) {
			min = Math.min(min, sc.nextDouble()/sc.nextDouble());
		}

		System.out.printf("%.2f",min*1000);

		sc.close();
	}
}