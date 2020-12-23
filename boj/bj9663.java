import java.util.Scanner;

public class bj9663 {
	static int n, cnt = 0;
	static int[][] chk;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		n = sc.nextInt();
		chk = new int[n][n];

		dfs(0);
		System.out.println(cnt);

		sc.close();
	}

	static void dfs(int now) {
		for (int i = 0; i < n; i++) {
			if (chk[now][i] == 0) {
				if (now + 1 == n) {
					cnt++;
				} else {
					int r = 0, l = 0;
					for (int j = now + 1; j < n; j++) {
						r++;
						l++;
						chk[j][i]++;
						if (i + r < n)
							chk[j][i + r]++;
						if (i - l >= 0)
							chk[j][i - l]++;
					}
					dfs(now + 1);
					r = 0;
					l = 0;
					for (int j = now + 1; j < n; j++) {
						r++;
						l++;
						chk[j][i]--;
						if (i + r < n)
							chk[j][i + r]--;
						if (i - l >= 0)
							chk[j][i - l]--;
					}
				}
			}
		}
	}
}