import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class bj1197 {
	static int[] parents;
	static int[] rank;
	// 입력은 첫줄에 정점의 갯수와 간선의 개숫가 들어오고
	// 그 다음 줄부터 간선의 정보가 정점1 정점2 가중치로 간선의 갯수만큼 들어옴
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int V = sc.nextInt();
		int E = sc.nextInt();
		int[][] edges = new int[E][3];
		parents = new int[V+1];
		rank = new int[V+1];

		for(int i = 0; i < E; i++)
		{
			edges[i][0] = sc.nextInt();
			edges[i][1] = sc.nextInt();
			edges[i][2] = sc.nextInt();
			//System.out.println(edges[i][0]+" "+edges[i][1]+" "+edges[i][2]);
		}

		// 간선들을 가중치 오름차순으로 정렬
		Arrays.sort(edges, new Comparator<int[]>() {

			@Override
			public int compare(int[] o1, int[] o2) {
				// TODO Auto-generated method stub
				return Integer.compare(o1[2], o2[2]);
			}
		});

		//각 정점에 대해 union-find 준비
		for(int i = 0; i < V; i++){
			parents[i]=i;
		}

		long result = 0;
		int cnt = 0;

		for(int i = 0; i < E; i++)
		{
			int a = findSet(edges[i][0]);
			int b = findSet(edges[i][1]);

			if(a == b)
				continue;
			union(a, b);
			// 간선을 선택
			result += edges[i][2];
			// 정점의 갯수 -1 번 반복하면 종료
			cnt++;
			if(cnt == V - 1)
				break;
		}

		System.out.println(result);
	}

	static int findSet(int x)
	{
		if(x == parents[x]) {
			return x;
		}
		else
		{
			parents[x] = findSet(parents[x]);
			return parents[x];
		}
	}

	static void union(int x, int y)
	{
		int px = findSet(x);
		int py = findSet(y);
		if(rank[px] > rank[py])
			parents[py] = px;
		else
		{
			parents[px] = py;
			if(rank[px] == rank[py])
				rank[py]++;
		}
	}

}