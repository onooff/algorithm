import java.util.*;

public class bj1773 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int c = sc.nextInt();
		int[] arr = new int[c+1];
		
		int t;
		for(int i=0;i<n;i++) {
			t=sc.nextInt();
			for(int j=t;j<=c;j+=t) {
				arr[j]=1;
			}
		}
		
		int sum = 0;
		for(int i=1;i<=c;i++) {sum+=arr[i];}
		System.out.println(sum);
		
		sc.close();
	}
}
