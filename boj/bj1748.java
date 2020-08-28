//Main
import java.util.*;
public class bj1748 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int num=1,cnt=10;
		long result=0;
		for(int i=1;i<=n;i++) {
			if(i==cnt) {num++; cnt*=10;}
			result+=num;
		}
		System.out.println(result);
		sc.close();
	}
}