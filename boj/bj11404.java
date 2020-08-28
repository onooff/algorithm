import java.util.Arrays;
import java.util.Scanner;

public class bj11404 {
	public static void main(String[] args) {
		final int M = 1987654321;
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int l = sc.nextInt();
		int a,b,c;

		int[][] D = new int[n+1][n+1];
		for(int i=0;i<=n;i++) {
			Arrays.fill(D[i], M);
		}

		for(int i=0;i<l;i++) {
			a=sc.nextInt();
			b=sc.nextInt();
			c=sc.nextInt();
			D[a][b] = Math.min(D[a][b], c);
		}

		for (int k = 1; k < D.length; k++) { 
			for (int i = 1; i < D.length; i++) {
				if (k == i) {D[i][k]=0; continue;}
				for (int j = 1; j < D.length; j++) {
					if (k == j || i == j) continue;

					if (D[i][k] != M && D[k][j] != M &&
							D[i][j] > D[i][k] + D[k][j]) {
						D[i][j] = D[i][k] + D[k][j];
					}
				}
			}
		}

		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
                if(D[i][j]==M) System.out.print("0 ");
				else System.out.print(D[i][j]+" ");
			}
			System.out.println();
		}
	}
}