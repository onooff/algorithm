import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class swea9659SangWok {
	static StringBuffer sb = new StringBuffer();
	static int[][] coe;
	static long[] answer;
	static final long mod = 998244353;
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for(int tc = 1; tc <= T; tc++) {
			sb.append("#" + tc);
			int N = Integer.parseInt(br.readLine()); // 2 ~ 50
			coe = new int[N + 1][3];
			answer = new long[N + 1];
			answer[0] = 1;
			StringTokenizer st;

			for(int i = 2; i < N + 1; i++) {
				st = new StringTokenizer(br.readLine(), " ");
				for(int j = 0; j < 3; j++)
					coe[i][j] = Integer.parseInt(st.nextToken());
			}

			int M = Integer.parseInt(br.readLine());
			st = new StringTokenizer(br.readLine(), " ");

			for(int i = 0; i < M; i++) {
				long x = Long.parseLong(st.nextToken());
				answer[1] = x;
				for(int m = 2; m < N + 1; m++) {
					switch(coe[m][0]) {
					case 1:
						answer[m] = (answer[coe[m][1]] + answer[coe[m][2]]) % mod;
						break;
					case 2:
						answer[m] = (coe[m][1] * answer[coe[m][2]]) % mod;
						break;
					case 3:
						answer[m] = (answer[coe[m][1]] * answer[coe[m][2]]) % mod;
						break;
					default: break;
					}
				}
				sb.append(" " + answer[N]%mod); 
			}
			sb.append("\n");
		}
		System.out.println(sb.toString());
	}

}