//Main
import java.util.*;
public class bj1706 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int m = sc.nextInt();

		char[][] map = new char[n][m];
		int i,j;

		for(i=0;i<n;i++) map[i]=sc.next().toCharArray();

		Set<String> set = new TreeSet<>();
		StringBuilder sb = new StringBuilder();
		char tmp;
		for(i=0;i<n;i++) {
			for(j=0;j<m;j++) {
				tmp = map[i][j];
				if(tmp=='#') {
					if(sb.length()>1) {
						set.add(sb.toString());
					}
					sb = new StringBuilder();
				}
				else {
					sb.append(tmp);
				}
			}
			if(sb.length()>1) {
				set.add(sb.toString());
			}
			sb = new StringBuilder();
		}
		for(i=0;i<m;i++) {
			for(j=0;j<n;j++) {
				tmp = map[j][i];
				if(tmp=='#') {
					if(sb.length()>1) {
						set.add(sb.toString());
					}
					sb = new StringBuilder();
				}
				else {
					sb.append(tmp);
				}
			}
			if(sb.length()>1) {
				set.add(sb.toString());
			}
			sb = new StringBuilder();
		}

		for(String s:set) {System.out.println(s); break;}

		sc.close();
	}
}