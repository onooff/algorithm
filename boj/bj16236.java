
//Main
import java.util.*;

public class bj16236 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int mapSize = sc.nextInt();
		int[][] map = new int[mapSize][mapSize];
		boolean[][] chk = new boolean[mapSize][mapSize];
		int[] fishes = new int[7];

		PriorityQueue<v> bfs = new PriorityQueue<>();
		for (int i = 0; i < mapSize; i++) {
			for (int j = 0; j < mapSize; j++) {
				map[i][j] = sc.nextInt();
				if (map[i][j] == 9) {
					bfs.offer(new v(i, j, 0));
					chk[i][j] = true;
					map[i][j] = 0;
				} else if (map[i][j] != 0) {
					fishes[map[i][j]]++;
				}
			}
		}
		int time = 0;
		int mySize = 2;
		int next = mySize;
		int eatable = fishes[1];
		int eatCnt = 0;
		while (!bfs.isEmpty() && eatable != 0) {
			v tmp = bfs.poll();

			if (map[tmp.y][tmp.x] != 0 && map[tmp.y][tmp.x] < mySize) {
				eatCnt++;
				map[tmp.y][tmp.x] = 0;
				time += tmp.d;
				next--;
				eatable--;
				if (next == 0) {
					mySize++;
					next = mySize;
					if (mySize < 8)
						eatable += fishes[mySize - 1];
				}

				bfs.clear();
				chk = new boolean[mapSize][mapSize];
				bfs.offer(new v(tmp.y, tmp.x, 0));
				chk[tmp.y][tmp.x] = true;
//				System.out.println("eat:" + tmp.toString()+" eatable:"+eatable+" eatCnt:"+eatCnt+" size:"+mySize);
				System.out.printf("(%d, %d) %d\n",tmp.y+1,tmp.x+1,eatCnt);
				continue;
			}

			int nd = tmp.d + 1;
			for (int i = 0; i < 4; i++) {
				int ny = tmp.y + d[i][0];
				int nx = tmp.x + d[i][1];
				if (isIn(ny, nx, mapSize, mapSize) && !chk[ny][nx] && map[ny][nx] <= mySize) {
					bfs.add(new v(ny, nx, nd));
					chk[ny][nx] = true;
				}
			}
		}
		System.out.println(time);

		sc.close();
	}

	static class v implements Comparable<v> {
		int y;
		int x;
		int d;

		@Override
		public int compareTo(v o) {
			if (this.d > o.d)
				return 1;
			else if (this.d == o.d && this.y > o.y)
				return 1;
			else if (this.d == o.d && this.y == o.y && this.x > o.x)
				return 1;
			return -1;
		}

		public v(int y, int x, int d) {
			super();
			this.y = y;
			this.x = x;
			this.d = d;
		}

		@Override
		public String toString() {
			return "v [y=" + y + ", x=" + x + "]";
		}
	}

	static boolean isIn(int i, int j, int y, int x) {
		if (i >= 0 && j >= 0 && i < y && j < x) {
			return true;
		}
		return false;
	}

	static int[][] d = { { 0, 1 }, { 0, -1 }, { 1, 0 }, { -1, 0 } };
}