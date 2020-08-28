//Main
import java.util.*;
public class bj2747 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();

		if(n<=2) {System.out.println('1');}
		else {
			int[] arr = new int[n+1];
			arr[1]=1;
			arr[2]=1;
			for(int i=3;i<=n;i++) {
				arr[i]=arr[i-1]+arr[i-2];
			}
			System.out.println(arr[n]);
		}

		sc.close();
	}
}