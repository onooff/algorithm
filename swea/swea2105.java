/*
 * 처음진행한방향,거리
 * 한번 방향 바꾼후의 방향, 거리 기억한 후
 * 
 * 처음진행한방향의반대방향,거리
 * 두번째방향의반대방향,거리만큼 이동하면 원래자리 & 사각형모양 루트
 * 
 * (x+2)%4 = 반대방향
 * 
 * 대각선사방탐색
 * 
 * 바로 전 방향으로는 진행하지 말아야 함
 */

import java.util.*;
public class swea2105 {
	static int n = 0;
	static int[][] map = null;
	static boolean[] chk = new boolean[100+1];

	static int max = Integer.MIN_VALUE;

	static int startY=0, startX=0;
	static int[][] d = {
			{1,1},//우하
			{1,-1},//좌하
			{-1,-1},//좌상
			{-1,1},//우상
	};
	static boolean[] chkD = new boolean[4];//[진행방향][진행거리]


	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int t = sc.nextInt();

		for(int tc=1;tc<=t;tc++) {
			n = sc.nextInt();
			map = new int[n][n];

			for(int i=0;i<n;i++) {
				for(int j=0;j<n;j++) { map[i][j]=sc.nextInt(); }
			}

			for(int i=0;i<n-1;i++) {
				for(int j=1;j<n;j++) {
					startY=i;
					startX=j;

					//chk[map[i][j]]=true;
					dfs(i,j,0,false,0);
					//chk[map[i][j]]=false;
				}
			}

			if(max==Integer.MIN_VALUE) max=-1;
			System.out.printf("#%d %d%n",tc,max);
			max = Integer.MIN_VALUE;
		}

		sc.close();
	}



	//	private static void dfs(int y, int x, int cnt, boolean go, int lastD) {
	//		if(go && y==startY && x==startX) {
	//			if(cnt>max) max=cnt;
	//			return;
	//		}
	//
	//		int ny,nx;
	//		for(int i=0;i<4;i++) {
	//			if(!(lastD==i || !chkD[i])) continue;
	//			System.out.println("test");
	//			chkD[i]=true;
	//			ny=y+d[i][0];
	//			nx=x+d[i][1];
	//
	//			if(isIn(ny,nx,n,n) && !chk[map[ny][nx]]) {	
	//				chk[map[ny][nx]]=true;
	//				dfs(ny,nx,cnt+1,true,i);
	//				chk[map[ny][nx]]=false;
	//			}
	//			chkD[i]=false;
	//		}
	//	}
	private static void dfs(int y, int x, int cnt, boolean go, int dd) {
		if(go && y==startY && x==startX) {
			if(cnt>max) max=cnt;
			return;
		}

		int ny,nx;

		//System.out.println("cnt="+cnt);
		ny=y+d[dd][0];
		nx=x+d[dd][1];
		if(isIn(ny,nx,n,n) && !chk[map[ny][nx]]) {	
			chk[map[ny][nx]]=true;
			dfs(ny,nx,cnt+1,true,dd);
			chk[map[ny][nx]]=false;
		}

		if(dd+1<4) {
			ny=y+d[dd+1][0];
			nx=x+d[dd+1][1];
			if(isIn(ny,nx,n,n) && !chk[map[ny][nx]]) {
				chk[map[ny][nx]]=true;
				dfs(ny,nx,cnt+1,true,dd+1);
				chk[map[ny][nx]]=false;
			}
		}
	}

	static boolean isIn(int i, int j, int y, int x) {
		if(i>=0 && j>=0 && i<y && j<x) {return true;}
		return false;
	}
}