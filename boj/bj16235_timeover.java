//Main
import java.util.*;
public class bj16235_timeover {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		//long start = System.currentTimeMillis();
		int N = sc.nextInt();
		int M = sc.nextInt();
		int K = sc.nextInt();
		int i,j,a,b;

		farm[][] map = new farm[N][N];
		int[][] foodArr = new int[N][N];
		for(i=0;i<N;i++) {
			for(j=0;j<N;j++) {
				foodArr[i][j] = sc.nextInt();
				map[i][j]=new farm(5);
			}
		}

		for(a=0;a<M;a++) {
			map[sc.nextInt()-1][sc.nextInt()-1].trees.add(new tree(sc.nextInt()));
		}

		//		for(i=0;i<N;i++) {
		//			for(j=0;j<N;j++) {
		//				Collections.sort(map[i][j].trees);
		//			}
		//		}

		int size,idx,ni,nj;
		LinkedList<tree> trees;
		for(a=0;a<K;a++) {
			//봄
			for(i=0;i<N;i++) {
				for(j=0;j<N;j++) {
					trees = map[i][j].trees;
					if(!trees.isEmpty()) {
						size=trees.size();
						for(b=0;b<size;b++) {
							if(map[i][j].food<trees.get(b).old) {trees.get(b).isALive=false; map[i][j].isHaveDeadTree=true;}
							else {
								map[i][j].food-=trees.get(b).old;
								trees.get(b).old++;
								if(trees.get(b).old%5==0) map[i][j].breedingCnt++;
							}
						}
					}
				}
			}
			//여름
			for(i=0;i<N;i++) {
				for(j=0;j<N;j++) {
					if(map[i][j].isHaveDeadTree) {
						trees = map[i][j].trees;
						size=trees.size();
						idx=0;
						for(b=0;b<size;b++) {
							if(!trees.get(idx).isALive) {
								map[i][j].food+=trees.get(idx).old/2;
								trees.remove(idx);
							}
							else idx++;
						}
						map[i][j].isHaveDeadTree = false;
					}
				}
			}
			//가을
			for(i=0;i<N;i++) {
				for(j=0;j<N;j++) {
					for(; map[i][j].breedingCnt>0; map[i][j].breedingCnt--) {
						for(b=0;b<8;b++) {
							ni=i+d[b][0];
							nj=j+d[b][1];
							if(isIn(ni,nj,N,N)) map[ni][nj].trees.add(0, new tree(1));
						}
					}
				}
			}
			//겨울
			for(i=0;i<N;i++) {
				for(j=0;j<N;j++) map[i][j].food+=foodArr[i][j];
			}
		}

		int sum=0;
		for(i=0;i<N;i++) {
			for(j=0;j<N;j++) sum+=map[i][j].trees.size();
		}

		System.out.println(sum);

		sc.close();
	}

	static class farm{
		int food;
		LinkedList<tree> trees;
		boolean isHaveDeadTree;
		int breedingCnt;
		public farm(int food) {
			super();
			this.food = food;
			this.trees = new LinkedList<tree>();
			this.isHaveDeadTree = false;
			this.breedingCnt = 0;
		}
	}
	static class tree implements Comparable<tree>{
		int old;
		boolean isALive;
		public tree(int old) {
			this.old = old;
			this.isALive = true;
		}
		@Override
		public int compareTo(tree o) {
			return Integer.compare(this.old, o.old);
		}
		@Override
		public String toString() {
			return "tree [old=" + old + ", isALive=" + isALive + "]";
		}
	}

	static boolean isIn(int i, int j, int y, int x) {
		if(i>=0 && j>=0 && i<y && j<x) {return true;}
		return false;
	}

	static int[][] d= {
			{-1,-1},
			{-1,0},
			{-1,1},
			{0,1},
			{1,1},
			{1,0},
			{1,-1},
			{0,-1}
	};
}

/*
5 2 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 1 3
3 2 3

15
 */