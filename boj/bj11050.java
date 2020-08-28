//Main
import java.util.*;
public class bj11050 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int k = sc.nextInt();

		int nn=1;
		int kk=1;

		for(int i=0;i<k;i++) {
			nn*=n-i;
		}
		for(int i=0;i<k;i++) {
			kk*=k-i;
		}

		System.out.println(nn/kk);

		sc.close();
	}
}