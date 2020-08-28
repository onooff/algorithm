import java.util.*;
public class swea1907_fail {
	static int[][] d = {
			{-1,-1},
			{-1,0},
			{-1,1},
			{0,1},
			{1,1},
			{1,0},
			{1,-1},
			{0,-1},
	};
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();

		for(int tc=1;tc<=t;tc++) {
			int n = sc.nextInt();
			int m = sc.nextInt();
			int[][] arr = new int[n][m];
			String tmp = sc.nextLine();
			
			for(int i=0;i<n;i++) {
				tmp = sc.nextLine();
				for(int j=0;j<m;j++) {
					if(tmp.charAt(j)=='.') arr[i][j]=0;
					else arr[i][j]=tmp.charAt(j)-'0';
				}
			}
			
			boolean chk=true;
			boolean[][] damageChk = new boolean[n][m];
			int cnt=0;
			
			while(chk) {
				chk=false;
				for(int i=0;i<n;i++) {
					for(int j=0;j<m;j++) {
						int damage = 0;
						int ni,nj;
						for(int k=0;k<8;k++) {
							ni=i+d[k][0];
							nj=j+d[k][1];
							if(!isIn(ni, nj, n, m)) {
								damage++;
							}
							else if(arr[ni][nj] == 0) {
								damage++;
							}
						}
						
						if(arr[i][j]!=0 && damage>=arr[i][j]) {
							damageChk[i][j]=true;
							chk=true;
						}
					}
				}
				
				if(chk) {
					cnt++;
					for(int i=0;i<n;i++) {
						for(int j=0;j<m;j++) {
							if(damageChk[i][j]) arr[i][j]=0;
							//System.out.print(arr[i][j]+" ");
						}
						//System.out.println();
					}
				}
				

			}
			
			System.out.printf("#%d %d%n",tc,cnt);
		}
		
		sc.close();
	}
	static boolean isIn(int i, int j, int y, int x) {
		if(i>=0 && j>=0 && i<y && j<x) {return true;}
		return false;
	}
}