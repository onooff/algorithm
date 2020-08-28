//Solution
import java.util.*;
public class swea4366 {
	static int tc;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int t = sc.nextInt();

		for(tc=1;tc<=t;tc++) {
			char[] s2 = sc.next().toCharArray();
			char[] s3 = sc.next().toCharArray();

			Set<Integer> set = new HashSet<Integer>();

			for(int i=0;i<s2.length;i++) {
				if(s2[i]=='0') {
					intoSet(i,s2,'1',set,2);
				}
				else {
					intoSet(i,s2,'0',set,2);
				}
			}
			for(int i=0;i<s3.length;i++) {
				if(s3[i]=='0') {
					if(!intoSet(i,s3,'1',set,3)) break;
					if(!intoSet(i,s3,'2',set,3)) break;
				}
				else if(s3[i]=='1') {
					if(!intoSet(i,s3,'0',set,3)) break;
					if(!intoSet(i,s3,'2',set,3)) break;
				}
				else {
					if(!intoSet(i,s3,'0',set,3)) break;
					if(!intoSet(i,s3,'1',set,3)) break;
				}
			}
		}
		sc.close();
	}
	
	static boolean intoSet(int i, char[] s, char c, Set<Integer> set, int n) {
		char tmp = s[i];
		s[i] = c;
		boolean b = set.add(Integer.parseInt(new String(s),n));
		
		if(!b) {System.out.printf("#%d %d%n",tc,Integer.parseInt(new String(s),n)); return b;}
		s[i] = tmp;
		return b;
	}
}