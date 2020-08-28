//Main
import java.util.*;
public class bj1764 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int m = sc.nextInt();
		StringBuilder sb = new StringBuilder();
		Set<String> chk = new TreeSet<String>();
		Set<String> dbj = new TreeSet<String>();
		
		for(int i=0;i<n;i++) {
			chk.add(sc.next());
		}
		
		String s;
		int cnt=0;
		for(int i=0;i<m;i++) {
			s = sc.next();
			if(!chk.add(s)) {
				dbj.add(s);
				cnt++;
			}
		}
		
		System.out.println(cnt);
		for(String str:dbj) System.out.println(str);
		
		sc.close();
	}
}