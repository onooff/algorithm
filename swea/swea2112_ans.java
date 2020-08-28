//Solution
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
public class swea2112_ans {
	static int[][] map;
	static int D,W;
	static int K;
	static int min;
	static int[] list;//0:약품을 넣지 않은 경우 1:a약품(0) 2:b약품(1)
	public static void main(String[] args) throws Exception {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(in.readLine());

		for(int tc=1;tc<=T;tc++) {
			min=Integer.MAX_VALUE;

			StringTokenizer st = new StringTokenizer(in.readLine()," ");
			D = Integer.parseInt(st.nextToken());
			W = Integer.parseInt(st.nextToken());
			K = Integer.parseInt(st.nextToken());
			map = new int[D][W];
			list = new int[D];
			for(int i=0;i<D;i++) {
				st=new StringTokenizer(in.readLine()," ");
				for(int j=0;j<W;j++) {
					map[i][j]=Integer.parseInt(st.nextToken());
				}
			}
			dfs(0,0);
			System.out.printf("#%d %d\n",tc,min);
		}
	}

	private static void dfs(int row, int count) {
		if(row==D) {
			if(check()) {
				min=Math.min(min, count);
			}
			return;
		}

		if(count>=min) {
			return;
		}

		list[row]=0;
		dfs(row+1,count);

		list[row]=1;
		dfs(row+1,count+1);

		list[row]=2;
		dfs(row+1,count+1);

	}

	private static boolean check() {
		int count,cur,next;
		for(int i=0;i<W;i++) {
			count=1;
			for(int j=0;j<D-1;j++) {
				cur=map[j][i];
				next=map[j+1][i];
				if(list[j]>0) {
					cur=list[j]-1;
				}
				if(list[j+1]>0) {
					next=list[j+1]-1;
				}
				if(cur==next) {
					count++;
					if(count>=K) break;
				}else {
					count=1;
				}
			}
			if(count<K) return false;
		}
		return true;
	}
}