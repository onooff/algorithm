//Main
import java.util.*;
public class bj1268 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int[][] arr = new int[n][6];

		for(int i=0;i<n;i++) {
			for(int j=0;j<5;j++) {
				arr[i][j] = sc.nextInt();
			}
		}

		for(int i=0;i<n;i++) {
			for(int j=0;j<n;j++) {
				if(j==i) continue;
				for(int k=0;k<5;k++) {
					if(arr[i][k]==arr[j][k]) {arr[i][5]++; break;}
				}
			}
		}

		int max = Integer.MIN_VALUE;
		int who = 0;
		for(int i=0;i<n;i++) {
			if(max<arr[i][5]) {max = arr[i][5]; who=i;}
		}

		System.out.println(who+1);

		sc.close();
	}
}
