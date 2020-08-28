//Main
import java.util.*;
public class bj1259 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n,l;
		String s;
		boolean isOK;

		while(true) {
			n=sc.nextInt();
			if(n==0) break;

			s = String.valueOf(n);
			l=s.length();
			isOK=true;

			for(int i=0;i<l/2;i++) {
				if(s.charAt(i)!=s.charAt(l-1-i)) {isOK=false; break;}
			}

			if(isOK) System.out.println("yes");
			else System.out.println("no");
		}

		sc.close();
	}
}