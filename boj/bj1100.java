//Main
import java.util.*;
public class bj1100 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String tmp = null;
		int cnt = 0;
		
		for(int i=0;i<8;i++) {
			tmp = sc.nextLine();
			for(int j=0;j<8;j++) {
				if(i%2==0 && j%2==0 && tmp.charAt(j)=='F') cnt++;
				else if(i%2==1 && j%2==1 && tmp.charAt(j)=='F') cnt++;
			}
		}
		System.out.println(cnt);
		
		sc.close();
	}
}
