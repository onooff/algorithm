//잘못짠거같음

import java.util.*;

public class swea1979 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int t=sc.nextInt();
		for(int tc = 1;tc<=t;tc++) {
			int n = sc.nextInt();
			int w = sc.nextInt();
			int[][] arr = new int[n][n];
			int cnt=0;

			for(int i=0;i<n;i++) {
				for(int j=0;j<n;j++) {
					arr[i][j]=sc.nextInt();
				}
			}
			for(int i=0;i<n;i++) {
				for(int j=0;j<n;j++) {
					if(arr[i][j]==1) {

						boolean jFlag=false;
						boolean iFlag=false;
						//가로 가능여부 = j
						for(int k=1;k<=w;k++){
							if(!isIn(i,j+k,n,n)) {break;}
							if(arr[i][j+k]!=1) {break;}
							if(k==w) {jFlag=true;}
						}
						if(jFlag) {
							if(isIn(i,j+w+1,n,n) && isIn(i,j-1,n,n)) {
							    if(arr[i][j+w+1]!=1 && arr[i][j-1]!=1) {cnt++;}
							}
							else {
							    if(!isIn(i,j+w+1,n,n)) {cnt++;}
							}
						}
						//세로 가능여부 = i
						for(int k=1;k<=w;k++){
							if(!isIn(i+k,j,n,n)) {break;}
							if(arr[i+k][j]!=1) {break;}
							if(k==w) {iFlag=true;}
						}
						if(iFlag) {
							if(isIn(i+w+1,j,n,n) && isIn(i-1,j,n,n)) {
							    if(arr[i+w+1][j]!=1 && arr[i-1][j]!=1) {cnt++;}
							}
							else {
							    if(!isIn(i+w+1,j,n,n)) {cnt++;}
							}
						}
					}
				}
			}
			System.out.printf("#%d %d%n",tc,cnt);
		}
		sc.close();
	}

	static boolean isIn(int x, int y, int n, int m) {
		if(x>=0 && y>=0 && x<n && y<m) {return true;}
		return false;
	}
}
/*
1
5 2
0 0 1 1 1
1 1 1 1 0
0 0 1 0 0
0 1 1 1 1
1 1 1 0 1
 */
