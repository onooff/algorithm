import java.util.*;
public class swea6782 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();

		for(int tc=1;tc<=t;tc++) {
			
			double n = sc.nextDouble();
			int cnt=0;
			
			while(n!=2) {
				if(Math.sqrt(n)%1 != 0) {
					double tmp = Math.ceil(Math.sqrt(n));
					cnt += Math.pow(tmp,2)-n;
					n = tmp;
				}
				else n = Math.sqrt(n);
				cnt++;
			}
			
			System.out.printf("#%d %d%n",tc,cnt);
		}
		
		sc.close();
	}
}