//Main
import java.util.*;
public class bj1654 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		long n = sc.nextInt();
		long k = sc.nextInt();
		long[] arr = new long[(int)n];
		for(int i=0; i<n; i++){
			arr[i] = sc.nextInt();
		}

		long high = Long.MAX_VALUE;
		long low = 0;
		long center = 0;
		long sum = 0;
		while(high>=low) {
			center = (high+low)/2;
			sum=0;
			for(long i:arr) sum+=i/center;
			System.out.print("low="+low+" high="+high+" bt="+center+" sum="+sum);

			if(sum>=k) {
				System.out.println(" low up");
				low = center+1;
				if (center > high) high = center;
			}
			else {
				System.out.println(" high down");
				high = center-1;
			}
		}

		System.out.println(high);
		sc.close();
	}
}
/*
4 11
802
743
457
539
 */