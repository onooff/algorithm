import java.util.*;

public class bj2851 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Random r = new Random();
		int N = 10;
		
		int[] arr = new int[N];
		
		for(int i=0;i<N;i++) {
			//arr[i] = sc.nextInt();
			arr[i] = r.nextInt(99)+1;
			System.out.println(arr[i]);
		}
		
		int best = Integer.MIN_VALUE;
		for(int i=0;i<arr.length;i++) {
			int sum = 0;
			int lastSum = Integer.MIN_VALUE;
			int point = Integer.MIN_VALUE;
			for(int j=i;j<=arr.length;j++) {
				if(j==arr.length) {point = lastSum; break;}
				sum+=arr[j];
				if(sum==100) {System.out.println(100); return;}
				if(sum>100) {
					point = Math.abs(100-sum)>Math.abs(100-lastSum)? lastSum : sum;
					//sum이 lastSum보다 큰 값임은 확실하므로, sum과 100의 차가 lastSum과 100의 차보다 큰지만 확인하면
					//나머지 경우의 수는 같거나 작은 경우가 남는데 같은 경우에 sum 값을 취함으로써 더 큰값을 갖는다는 문제조건에 부합한다
					break;
				}
				lastSum=sum;
			}
			if(Math.abs(100-best)>Math.abs(100-point)) {best = point;}
			else if(Math.abs(100-best)==Math.abs(100-point)) {
				best = best>point? best : point;
			}
		}
		
		System.out.println(best);
		sc.close();
	}
}