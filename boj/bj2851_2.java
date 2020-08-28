import java.util.*;

public class bj2851_2 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int sum = 0;
		for(int i=0;i<10;i++) {
			int tmp = sc.nextInt();
			if(sum+tmp==100) {System.out.println(100); return;}
			if(sum+tmp>100) {sum = Math.abs(100-sum)<Math.abs(100-sum-tmp)? sum : sum+tmp; break;}
			sum+=tmp;
		}
		System.out.println(sum);
		sc.close();
	}
}