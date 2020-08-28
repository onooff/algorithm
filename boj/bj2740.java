//Main
import java.util.*;
public class bj2740 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int y1 = sc.nextInt();
		int x1 = sc.nextInt();
		int[][] arr1 = new int[y1][x1];
		for(int i=0;i<y1;i++) {
			for(int j=0;j<x1;j++) {
				arr1[i][j]=sc.nextInt();
			}
		}

		int y2 = sc.nextInt();
		int x2 = sc.nextInt();
		int[][] arr2 = new int[y2][x2];
		for(int i=0;i<y2;i++) {
			for(int j=0;j<x2;j++) {
				arr2[i][j]=sc.nextInt();
			}
		}

		int[][] ans = new int [y1][x2];
		for(int i=0;i<y1;i++) {
			for(int j=0;j<x2;j++) {
				for(int k=0;k<y2;k++) {
					ans[i][j]+=arr1[i][k]*arr2[k][j];
				}
				System.out.print(ans[i][j]+" ");
			}
			System.out.println();
		}
		sc.close();
	}
}