//Main
import java.util.*;
public class bj2636 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int i,j,k,ni,nj;
		int n = sc.nextInt();
		int m = sc.nextInt();
		int tCnt=0; //시간
		int cCnt=0; //남은치즈개수

		int[][] cheese = new int [n][m]; //0=공기 1=치즈 2=치즈녹이는공기 3=곧녹을치즈
		for(i=0;i<n;i++) {
			for(j=0;j<m;j++) {
				cheese[i][j]=sc.nextInt();
				if(cheese[i][j]==1) cCnt++;
			}
		}
		int lastCheese = cCnt;

		Queue<v> air = new LinkedList<>();
		Queue<v> melt = new LinkedList<>();
		Queue<v> nextMelt = new LinkedList<>();
		cheese[0][0]=2;
		air.add(new v(0,0));
		v tmp;
		while(true){
			while(!air.isEmpty()) {
				tmp=air.poll();
				for(k=0;k<4;k++) {
					ni=tmp.i+d[k][0];
					nj=tmp.j+d[k][1];
					if(isIn(ni,nj,n,m)) {
						if(cheese[ni][nj]==0) {
							cheese[ni][nj]=2;
							air.add(new v(ni,nj));
						}
						else if(cheese[ni][nj]==1) {
							cheese[ni][nj]=3;
							melt.add(new v(ni,nj));
						}
					}
				}
			}

			while(!melt.isEmpty()) {
				tmp=melt.poll();
				i=tmp.i;
				j=tmp.j;
				cheese[i][j]=2;
				cCnt--;

				for(k=0;k<4;k++) {
					ni=i+d[k][0];
					nj=j+d[k][1];
					if(isIn(ni,nj,n,m)) {
						if(cheese[ni][nj]==0) {
							cheese[ni][nj]=2;
							air.add(new v(ni,nj));
						}
						else if(cheese[ni][nj]==1) {
							cheese[ni][nj]=3;
							nextMelt.add(new v(ni,nj));
						}
					}
				}
			}

			tCnt++;
			//System.out.println(cCnt);//test
			if(cCnt==0) break;
			lastCheese = cCnt;
			melt=nextMelt;
			nextMelt = new LinkedList<>();
		}
		System.out.println(tCnt);
		System.out.println(lastCheese);

		///////////////test/////////////
		//		for(i=0;i<n;i++) {
		//			for(j=0;j<m;j++) {
		//				System.out.print(cheese[i][j]+" ");
		//			}
		//			System.out.println();
		//		}
		////////////////////////////////
		sc.close();
	}

	static class v{
		int i;
		int j;
		public v(int i, int j) {
			super();
			this.i = i;
			this.j = j;
		}
	}

	static boolean isIn(int i, int j, int y, int x) {
		if(i>=0 && j>=0 && i<y && j<x) {return true;}
		return false;
	}

	static int[][] d= {
			{0,1},
			{0,-1},
			{1,0},
			{-1,0}
	};
}