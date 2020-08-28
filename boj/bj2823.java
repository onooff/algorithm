import java.util.*;

public class bj2823 {
	static int[] dy = {-1,0,1,0};
	static int[] dx = {0,1,0,-1};
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int y=sc.nextInt();
		int x=sc.nextInt();
		char[][] arr = new char[y][];
		sc.nextLine();
		
		for(int i=0;i<arr.length;i++) {
			arr[i]=sc.nextLine().toCharArray();
			//System.out.println(arr[i].length);
		}
		
		for(int i=0;i<arr.length;i++) {
			for(int j=0;j<arr[i].length;j++) {
				if(arr[i][j]=='.') {
					int cnt=0;
					int ni,nj;
					for(int k=0;k<4;k++) {
						ni=i+dy[k]; nj=j+dx[k];
						if(isIn(ni,nj,y,x)) {
							if(arr[ni][nj]=='.') {cnt++;}
						}
					}
					if(cnt<=1) {System.out.println(1); return;}
				}
			}
		}
		
		System.out.println(0);
		sc.close();
	}
	
	static boolean isIn(int i, int j, int y, int x) {
		if(i>=0 && j>=0 && i<y && j<x) {return true;}
		return false;
	}
}
