//Main
import java.util.*;
public class bj1806 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int m = sc.nextInt();

		int[] arr = new int[n];

		for(int i=0;i<n;i++) {
			arr[i]=sc.nextInt();
		}

		int min = Integer.MAX_VALUE;
		int sum,length;
		for(int i=0;i<n;i++) {
			sum=0;
			length=0;
			for(int j=i;j<n;j++) {
				sum+=arr[j];
				length++;
				if(sum<m) continue;

				min=Math.min(min, length);
				break;
			}
		}

		if(min==Integer.MAX_VALUE) min=0;
		System.out.println(min);

		sc.close();
	}
}