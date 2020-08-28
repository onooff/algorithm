//문제범위인 100000개까지 노드를 가질 수 있는 트리를 2차원 배열로 표현할 경우 메모리 박살남

import java.util.*;
public class swea4534_fail {
	static int RESULT=0;
	static int ROOT=0;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int t = sc.nextInt();

		for(int tc=1;tc<=t;tc++) {

			int n = sc.nextInt();

			boolean[][] tree = new boolean[n+1][n+1];

			int a,b;
			ROOT = 0;
			for(int i=0;i<n-1;i++) {
				a = sc.nextInt();
				b = sc.nextInt();

				tree[b][a]=true;
				tree[b][a]=true;
			}

			dfs(tree,ROOT,1,0);

			System.out.printf("#%d %d%n",tc, RESULT); RESULT=0;
		}

		sc.close();
	}

	private static void dfs(boolean[][] tree, int idx, int w, int b) {
		int d=0; //degree
		for(int i=0;i<tree[idx].length;i++) {
			if(tree[idx][i]) d++;
		}

		if(d==0) {RESULT+=(w+b)%1000000007; return;}
		else{
			//value=((value*(d+1))-1)%1000000007;
			//if(idx==ROOT) value = 2;
			int tmp=w;
			w=(b+w)%1000000007;
			b=tmp%1000000007;
			System.out.println("->"+w+" "+b);
			for(int i=0;i<tree[idx].length;i++) {
				if(tree[idx][i]) {
					dfs(tree,i,w,b);
				}
			}
		}
	}
}