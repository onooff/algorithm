//Main
import java.util.*;
public class bj2480 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] arr = new int[6];
		int tmp,max=0;

		for(int i=0;i<3;i++) {
			tmp = sc.nextInt()-1;
			arr[tmp]++;
			max=Math.max(max, arr[tmp]);
		}
		int ans=0;
		switch(max) {
		case 1:
			for(int i=5;i>=0;i--) {
				if(arr[i]!=0) {
					ans=100*(i+1);
					break;
				}
			}
			break;
		case 2:
			for(int i=5;i>=0;i--) {
				if(arr[i]==2) {
					ans=100*(i+1)+1000;
					break;
				}
			}
			break;
		case 3:
			for(int i=5;i>=0;i--) {
				if(arr[i]==3) {
					ans=1000*(i+1)+10000;
					break;
				}
			}
			break;
		}
		System.out.println(ans);
		sc.close();
	}
}