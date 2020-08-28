import java.util.*;
public class bj2252 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		int[] arr = new int[n+1];
		ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
		for(int i=0;i<=n;i++) {
			graph.add(new ArrayList<Integer>());
		}

		int v1,v2;
		for(int i=0;i<m;i++) {
			v1=sc.nextInt();
			v2=sc.nextInt();
			graph.get(v1).add(v2);
			arr[v2]++;
		}

		Queue<Integer> q = new LinkedList<Integer>();
		StringBuilder sb = new StringBuilder();
		for (int i=1;i<=n;i++) {
			if (arr[i] == 0) {
				q.offer(i);
			}
		}
		
		int tmp;
		for (int i=0;i<n;i++) {
			tmp = q.poll();
			sb.append(tmp + " ");
			for (int v : graph.get(tmp)) {
				arr[v]--;
				if (arr[v] == 0) {
					q.add(v);
				}
			}
		}
		System.out.println(sb);
		sc.close();
	}
}