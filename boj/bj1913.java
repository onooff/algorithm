//Main
import java.util.*;
public class bj1913 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int find = sc.nextInt();
		int[][] arr = new int[n][n];

		int i=n/2;
		int j=n/2;
		int num=1;

		arr[i][j]=num++;

		int max=n*n;
		int level=1;
		int a;
		loop:while(true) {
			for(a=0;a<level;a++) {//위로
				arr[--i][j]=num++;
				if(num>max) break loop;
			}
			if(num>=max) break;
			for(a=0;a<level;a++) {//오른쪽으로
				arr[i][++j]=num++;
			}
			level++;
			for(a=0;a<level;a++) {//아래로
				arr[++i][j]=num++;
			}
			for(a=0;a<level;a++) {//왼쪽으로
				arr[i][--j]=num++;
			}
			level++;
		}

		int findI=0, findJ=0;

		StringBuilder sb = new StringBuilder();
		for(i=0;i<n;i++) {
			for(j=0;j<n;j++) {
				if(arr[i][j]==find) {findI=i+1; findJ=j+1;}
				sb.append(arr[i][j]+" ");
			}
			sb.append("\n");
		}
		sb.append(findI+" "+findJ);

		System.out.println(sb.toString());

		sc.close();
	}
}