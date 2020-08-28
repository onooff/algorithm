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
					//sum�� lastSum���� ū ������ Ȯ���ϹǷ�, sum�� 100�� ���� lastSum�� 100�� ������ ū���� Ȯ���ϸ�
					//������ ����� ���� ���ų� ���� ��찡 ���µ� ���� ��쿡 sum ���� �������ν� �� ū���� ���´ٴ� �������ǿ� �����Ѵ�
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