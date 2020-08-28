import java.util.*;

public class swea2007 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int t = Integer.parseInt(sc.nextLine());
		String s = null;
		String last = null;
		int r = 0;
		for(int tc=1;tc<=t;tc++) {
			s = sc.nextLine();
			for(int i=0; i<10; i++) {
				if(s.substring(0, i).equals(s.substring(i,i*2))) {
					if(s.substring(0, i).equals(last+last)) break;
					r=i;
					last=s.substring(0, i);
				}
			}
			System.out.printf("#%d %d%n",tc,r);
		}
		
		sc.close();
	}
}
