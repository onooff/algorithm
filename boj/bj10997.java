//Main
import java.util.*;
public class bj10997 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		if(n==1) {System.out.println('*');}
		else {
			char[][] arr = new char[4*n-1][4*n-3];

			int i=2*n, j=2*n-2;
			arr[i][j]='*';
			int d=0; //0상 1우 2하 3좌 d+1%4
			int[][] dd= {{-1,0},{0,1},{1,0},{0,-1}};
			int level=2;
			int k;
			loop: while(true) {
				for(k=0;k<level;k++) {
					i+=dd[d][0];
					j+=dd[d][1];
					arr[i][j]='*';
					//System.out.println(i+" "+j);
					if(i==0 && j==arr[0].length-1) break loop;
				}

				d=(d+1)%4;
				if(d==0 || d==2) level+=2;
			}
			StringBuilder sb = new StringBuilder();
			for(i=0;i<arr.length;i++) {
				for(j=0;j<arr[i].length;j++) {
					if(i==1) {sb.append('*'); break;}
					
					if(arr[i][j]=='*') sb.append('*');
					else sb.append(' ');
				}
				if(i!=arr.length-1) sb.append("\n");
			}
			System.out.print(sb.toString());
		}
		sc.close();
	}
}
/*
2 5  7  4 2
3 9  11 6 4
4 13 15 8 6
 */