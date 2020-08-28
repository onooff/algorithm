import java.util.*;
public class swea4530 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();

		for(int tc=1;tc<=t;tc++) {
			
			long low = sc.nextLong();
			long high = sc.nextLong();
			
			long result = high-low;
			
			if(low<0 && high>0) result--;
			for(long i=result; i>0; i/=10) {
				if(i%10>=4) {
					
					
					
				}
			}
			
			System.out.printf("#%d %d%n",tc,result);
		}
		
		sc.close();
	}
}
/*
001의자리에서 4등장 1*01
010의자리에서 4등장 1*10 (10-1)*01
100의자리에서 4등장 1*100 (10-1)*10 (100-10-1)*1
*/