import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Scanner;

public class bj1753 {
	static class Edge implements Comparable<Edge>{
		int v, weight;
		public Edge(int v, int weight) {
			this.v = v;
			this.weight = weight;
		}
		@Override
		public int compareTo(Edge o) {
			// TODO Auto-generated method stub
			return Integer.compare(this.weight, o.weight);
		}
		@Override
		public String toString() {
			return weight + "";
		}

	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int V = sc.nextInt();
		int E = sc.nextInt();
		int start = sc.nextInt();
		PriorityQueue<Edge> pq = new PriorityQueue<>();
		boolean[] check = new boolean[V+1];
		Edge[] D = new Edge[V+1];
		List<Edge>[] adj = new ArrayList[V+1];

		for(int i = 1; i < V+1; i++)
			adj[i] = new ArrayList<>();

		for(int i = 0; i < E; i++) {
			adj[sc.nextInt()].add(new Edge(sc.nextInt(), sc.nextInt()));
		}

		for(int i = 1; i < V+1; i++) {
			//원하는 출발지
			if( i == start ) {
				D[i] = new Edge(i, 0);
			}
			else {
				D[i] = new Edge(i, 987645321);
			}
			pq.add(D[i]);
		}
		while( !pq.isEmpty() ) {
			Edge edge = pq.poll();

			for( Edge next : adj[edge.v] ) {
				if( !check[next.v] && D[next.v].weight > D[edge.v].weight + next.weight ) {
					D[next.v].weight = D[edge.v].weight + next.weight;
					pq.remove(D[next.v]);
					pq.add(D[next.v]);
				}
			}
			check[edge.v] = true;
		}
		for(int i=1; i<=V; i++) {
			if(D[i].weight == 987645321) System.out.println("INF");
			else System.out.println(D[i].weight);
		}
	}
}