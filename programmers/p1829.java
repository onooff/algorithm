import java.util.LinkedList;
import java.util.Queue;

public class b1829 {
	public int[] solution(int m, int n, int[][] picture) {
		int numberOfArea = 0;
		int maxSizeOfOneArea = 0;
		int[][] d = {{0,1},{0,-1},{1,0},{-1,0}};

		boolean[][] chk = new boolean[m][n];

		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++) {
				if (picture[i][j] != 0 && !chk[i][j]) {
					numberOfArea++;
					int color = picture[i][j];
					int cnt = 1;
					Queue<v> q = new LinkedList<v>();
					q.offer(new v(i, j));
					chk[i][j] = true;
					while (!q.isEmpty()) {
						v tmp = q.poll();
						for(int k=0;k<4;k++) {
							int ni=tmp.i+d[k][0];
							int nj=tmp.j+d[k][1];
							if ((ni>=0 && nj>=0 && ni<m && nj<n) && picture[ni][nj] == color && !chk[ni][nj]) {
								chk[ni][nj] = true;
								cnt++;
								q.offer(new v(ni,nj));
							}
						}
					}
					if(cnt>maxSizeOfOneArea) maxSizeOfOneArea=cnt;
				}
			}
		}

		int[] answer = new int[2];
		answer[0] = numberOfArea;
		answer[1] = maxSizeOfOneArea;
		return answer;
	}

	class v {
		int i;
		int j;

		public v(int i, int j) {
			super();
			this.i = i;
			this.j = j;
		}

	}
}
