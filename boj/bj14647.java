//Main
import java.util.*;
public class bj14647 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int m = sc.nextInt();
		int[][] map = new int[n][m];

		int i,j,k,l,cnt=0;
		String s;
		for(i=0;i<n;i++) {
			for(j=0;j<m;j++) {
				s=sc.next();
				l=s.length();
				for(k=0;k<l;k++) {
					if(s.charAt(k)=='9') {map[i][j]++; cnt++;}
				}
			}
		}
		
		int max=0, tmp, result;
		boolean resultD;//false = 가로, true = 세로
		for(i=0;i<n;i++) {
			tmp=0;
			for(j=0;j<m;j++) {
				tmp+=map[i][j];
			}
			if(tmp>max) {
				max=tmp;
				result=i;
				resultD=false;
			}
		}
		for(j=0;j<m;j++) {
			tmp=0;
			for(i=0;i<n;i++) {
				tmp+=map[i][j];
			}
			if(tmp>max) {
				max=tmp;
				result=i;
				resultD=true;
			}
		}
		System.out.println(cnt-max);
		sc.close();
	}
}