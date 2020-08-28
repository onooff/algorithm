//Main
import java.util.*;
public class bj2576 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int sum=0, min=Integer.MAX_VALUE,tmp;

		for(int i=0;i<7;i++) {
			tmp=sc.nextInt();
			if(tmp%2==1) {
				sum+=tmp;
				min = Math.min(min, tmp);
			}
		}
		if(sum==0) System.out.println("-1");
		else {
			System.out.println(sum);
			System.out.println(min);
		}
		sc.close();
	}
}