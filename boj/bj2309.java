//Main
import java.util.*;
public class bj2309 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int[] arr = new int[9];
		
		int sum=0;
		for(int i=0;i<9;i++) {
			arr[i]=sc.nextInt();
			sum+=arr[i];
		}
		
		Arrays.sort(arr);
		
		int not1=0,not2=0;
		loop:for(int i=0;i<8;i++) {
			for(int j=i+1;j<9;j++) {
				if(sum-arr[i]-arr[j]==100) {not1=i; not2=j; break loop;}
			}
		}
		
		for(int i=0;i<9;i++) {
			if(i==not1 || i==not2) continue;
			System.out.println(arr[i]);
		}
		
		sc.close();
	}
}
