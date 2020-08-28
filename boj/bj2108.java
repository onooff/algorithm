//Main
import java.util.*;
public class bj2108 {
	static int RNG = 4000;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] arr = new int [RNG*2+1];

		int n = sc.nextInt();
		int[] center = new int[n];
		int sum=0,min=Integer.MAX_VALUE,max=Integer.MIN_VALUE,mode=Integer.MIN_VALUE;
		int tmp;

		for(int i=0;i<n;i++) {
			tmp=sc.nextInt();
			sum+=tmp;
			min = Math.min(min, tmp);
			max = Math.max(max, tmp);
			arr[tmp+RNG]++;
			mode = Math.max(mode, arr[tmp+RNG]);
			center[i]=tmp;
		}
		Arrays.sort(center);

		System.out.println(Math.round((double)sum/n));
		System.out.println(center[n/2]);
		int modeNum=0;
		boolean chk=false;
		for(int i=0;i<arr.length;i++) {
			if(arr[i]==mode){
				if(!chk) {modeNum=i-RNG; chk=true;}
				else {modeNum=i-RNG; break;}
			}
		}
		System.out.println(modeNum);
		System.out.println(max-min);
		sc.close();
	}
}