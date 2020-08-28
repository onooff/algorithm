import java.util.*;
public class bj17136_fail {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int[][] map = new int[10][10];
		int cnt=0;

		for(int i=0;i<10;i++) {
			for(int j=0;j<10;j++) {
				map[i][j] = sc.nextInt();
			}
		}

		looop:for(int k=4;k>=0;k--) {
			int havePaper = 5;
			for(int i=0;i<10-k;i++) {
				loop:for(int j=0;j<10-k;j++) {
					for(int a=i;a<=i+k;a++) {
						for(int b=j;b<=j+k;b++) {
							if(map[a][b]==0) {continue loop;}
						}
					}

					for(int a=i;a<=i+k;a++) {
						for(int b=j;b<=j+k;b++) {
							map[a][b]=0;
						}
					}

					for(int a=0;a<10;a++) {
						for(int b=0;b<10;b++) {
							System.out.print(map[a][b]);
						}
						System.out.println();
					}
					System.out.println();
					cnt++;
					havePaper--;
					if(havePaper<=0) {
						if (k!=0) {continue looop;}
						else if(k==0 && havePaper<0) {System.out.println("-1"); return;}
					}
				}
			}
		}

		System.out.println(cnt);
		sc.close();
	}
}