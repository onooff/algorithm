//Main
import java.util.*;
public class bj16235 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		//long start = System.currentTimeMillis();
		int N = sc.nextInt();
		int M = sc.nextInt();
		int K = sc.nextInt();
		int i,j,a,b;

		Queue<v> haveTree = new LinkedList<v>();
		Queue<v> haveDeadTree = new LinkedList<v>();
		Queue<v> haveBreedingTree = new LinkedList<v>();

		farm[][] map = new farm[N][N];
		int[][] foodArr = new int[N][N];
		for(i=0;i<N;i++) {
			for(j=0;j<N;j++) {
				foodArr[i][j] = sc.nextInt();
				map[i][j]=new farm(5);
			}
		}

		for(a=0;a<M;a++) {
			i=sc.nextInt()-1;
			j=sc.nextInt()-1;
			map[i][j].trees.add(new tree(sc.nextInt()));
			haveTree.offer(new v(i,j));
		}

		//		for(i=0;i<N;i++) {
		//			for(j=0;j<N;j++) {
		//				Collections.sort(map[i][j].trees);
		//			}
		//		}

		int qSize,size,idx,ni,nj;
		farm now;
		LinkedList<tree> trees;
		v tmp;
		for(a=0;a<K;a++) {
			//봄
			qSize = haveTree.size();
			for(i=0; i<qSize; i++) {
				tmp=haveTree.poll();
				now = map[tmp.i][tmp.j];
				trees = now.trees;
				if(!trees.isEmpty()) {
					size=trees.size();
					for(b=0;b<size;b++) {
						if(now.food<trees.get(b).old) {trees.get(b).isALive=false; haveDeadTree.offer(tmp);}
						else {
							now.food-=trees.get(b).old;
							trees.get(b).old++;
							if(trees.get(b).old%5==0) {now.breedingCnt++; haveBreedingTree.offer(tmp);}
						}
					}
				}
			}
			//여름
			qSize = haveDeadTree.size();
			for(i=0; i<qSize; i++) {
				tmp=haveDeadTree.poll();
				now = map[tmp.i][tmp.j];
				trees = now.trees;
				size=trees.size();
				idx=0;
				for(b=0;b<size;b++) {
					if(!trees.get(idx).isALive) {
						now.food+=trees.get(idx).old/2;
						trees.remove(idx);
					}
					else idx++;
				}
			}
			//가을
			qSize = haveBreedingTree.size();
			for(i=0; i<qSize; i++) {
				tmp=haveBreedingTree.poll();
				now = map[tmp.i][tmp.j];
				for(; now.breedingCnt>0; now.breedingCnt--) {
					for(b=0;b<8;b++) {
						ni=tmp.i+d[b][0];
						nj=tmp.j+d[b][1];
						if(isIn(ni,nj,N,N)) map[ni][nj].trees.add(0, new tree(1));
					}
				}
			}

			//겨울
			for(i=0;i<N;i++) {
				for(j=0;j<N;j++) {
					if(!map[i][j].trees.isEmpty()) haveTree.offer(new v(i,j));
					map[i][j].food+=foodArr[i][j];
				}
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
		int breedingCnt;
		public farm(int food) {
			super();
			this.food = food;
			this.trees = new LinkedList<tree>();
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
	static class v{
		int i;
		int j;
		public v(int i, int j) {
			this.i = i;
			this.j = j;
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