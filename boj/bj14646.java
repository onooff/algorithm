//Main
import java.util.*;
public class bj14646 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int[] arr = new int[n+1];

		int tmp,cnt=0,max=0;
		int l = n*2;
		for(int i=0;i<l;i++){
			tmp=sc.nextInt();
			//System.out.println(tmp);

			if(arr[tmp]==-1) continue;
			else if(arr[tmp]==1) {arr[tmp]=-1; cnt--;}
			else {arr[tmp]++; cnt++;}

			max=Math.max(max, cnt);
		}
		System.out.println(max);
		sc.close();
	}
}