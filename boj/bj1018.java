import java.util.*;
public class bj1018 {
	public static void main(String[] args) {
		char[][] chk1 = {
			{'W','B','W','B','W','B','W','B'},
			{'B','W','B','W','B','W','B','W'},
			{'W','B','W','B','W','B','W','B'},
			{'B','W','B','W','B','W','B','W'},
			{'W','B','W','B','W','B','W','B'},
			{'B','W','B','W','B','W','B','W'},
			{'W','B','W','B','W','B','W','B'},
			{'B','W','B','W','B','W','B','W'}
		};
		char[][] chk2 = {
				{'B','W','B','W','B','W','B','W'},
				{'W','B','W','B','W','B','W','B'},
				{'B','W','B','W','B','W','B','W'},
				{'W','B','W','B','W','B','W','B'},
				{'B','W','B','W','B','W','B','W'},
				{'W','B','W','B','W','B','W','B'},
				{'B','W','B','W','B','W','B','W'},
				{'W','B','W','B','W','B','W','B'}
			};
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		char[][] map = new char[n][];
		for(int i=0;i<n;i++) {
			map[i] = sc.next().toCharArray();
		}
		int cnt1,cnt2;
		int ans = Integer.MAX_VALUE;
		for(int i=0;i<=n-8;i++) {
			for(int j=0;j<=m-8;j++) {
				cnt1=0; cnt2=0;
				for(int a=0;a<8;a++) {
					for(int b=0;b<8;b++) {
						if(chk1[a][b]!=map[i+a][j+b]) cnt1++;
						if(chk2[a][b]!=map[i+a][j+b]) cnt2++;
					}
				}
				ans = Math.min(ans, cnt1);
				ans = Math.min(ans, cnt2);
			}
		}
		System.out.println(ans);
		sc.close();
	}
}
