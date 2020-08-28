//Main
import java.util.*;
public class bj1051 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int m = sc.nextInt();

		char[][] map = new char[n][m];
		int size = Math.min(n, m)-1;
		int i,j,k;
		char tmp;

		for(i=0;i<n;i++) map[i]=sc.next().toCharArray();
		sc.close();

		for(k=size;k>=0;k--) {
			for(i=0;i<n-k;i++) {
				for(j=0;j<m-k;j++) {
					tmp=map[i][j];
					if(map[i+k][j]==tmp && map[i][j+k]==tmp && map[i+k][j+k]==tmp) {
						System.out.println((k+1)*(k+1));
						return;
					}
				}
			}
		}
	}
}