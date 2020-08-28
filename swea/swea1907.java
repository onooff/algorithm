import java.util.Scanner;
public class swea1907 {
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

			boolean chk=true; //�������� �𷡼��� ���� ��� �ݺ��� �����Ű�� ���� �οﺯ��
			int[][] damageChk = new int[n][m];
			int cnt=0;//�ĵ� Ƚ��

			while(chk) {
				chk=false;//�ĵ��� ���� �������� �𷡰� ���� ��� chk�� false�� �����Ǿ� ���� �ݺ����� ������� �ʰ� �����.
				for(int i=0;i<n;i++) {
					for(int j=0;j<m;j++) {
						int ni,nj;
						if(arr[i][j]==0) {
							for(int k=0;k<8;k++) {
								ni=i+d[k][0];
								nj=j+d[k][1];
								if(isIn(ni,nj,n,m) && arr[ni][nj] != 0) {
									damageChk[ni][nj]++; // 8��Ž��
								}
							}
						}
					}
				}

				for(int i=1;i<n-1;i++) {
					for(int j=1;j<m-1;j++) {
						if(arr[i][j]!=0 && damageChk[i][j]>=arr[i][j]) {
							if(!chk) {cnt++; chk=true;}
							arr[i][j]=0;
						}
						damageChk[i][j]=0;
						System.out.print(arr[i][j]+" ");
					}
					System.out.println();
				}
				System.out.println();

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