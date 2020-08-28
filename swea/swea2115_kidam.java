import java.io.*;
import java.util.*;

class swea2115_kidam {
	static int m, max;
	static List<Integer> list = new ArrayList<>();
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int TC = Integer.parseInt(br.readLine());
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		for (int test_case = 1; test_case <= TC; ++test_case) {
			sb.append("#" + test_case + " ");
			st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			m = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			int[][] arr = new int[n][n];
			for (int i = 0; i < n; ++i) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < n; ++j) arr[i][j] = Integer.parseInt(st.nextToken());
			}
			
			
			int[][] ans = new int[n][n + 1 - m];
			for (int i = 0; i < n; ++i) {
				for (int j = 0; j < n + 1 - m; ++j) {
					list.clear();
					for (int k = j; k < j + m; ++k) {
						list.add(arr[i][k]);
					}
					max=0;
					go(0,0,c);
					ans[i][j]=max;
				}
			}
			int maxi=0, maxj=0;
			for(int i=0; i<n; ++i) {
				for (int j=0; j<n+1-m; ++j) {
					if(ans[maxi][maxj]<ans[i][j]) {
						maxi=i;
						maxj=j;
					}
				}
			}
			int ret=ans[maxi][maxj];
			for(int i=maxj; i>=maxj-(m-1); --i) {
				if(i>=0) {
					ans[maxi][i]=0;
				}
			}
			for(int i=maxj; i<=maxj+m-1; ++i) {
				if(i<n+1-m) {
					ans[maxi][i] = 0;
				}
			}
			max=0;
			for(int i=0; i<n; ++i) {
				for (int j=0; j<n+1-m; ++j) {
					if(max<ans[i][j]) {
						max = ans[i][j];
					}
				}
			}
			ret+=max;
			sb.append(ret + "\n");
		}
		System.out.println(sb);
	}
	
	static void go(int idx, int sum, int limit) {
		if(idx == m) {
			if(max<sum)max=sum;
			return;
		}
		int tmp = list.get(idx);
		if(tmp<=limit) go(idx+1, sum+tmp*tmp,limit-tmp);
		go(idx+1, sum, limit);
	}
}