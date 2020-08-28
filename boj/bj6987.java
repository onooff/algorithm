////Main
//import java.util.*;
//public class bj6987 {
//	public static void main(String[] args) {
//		Scanner sc = new Scanner(System.in);
//		int[][] arr = new int[6][4];
//		for(int t=0; t<10000; t++) {
//			boolean flag = true;
//			int sum = 0, win = 0, lose = 0, draw = 0, drawCnt = 0;
//			for(int i=0;i<6;i++) {
//				arr[i][3]=0;
//				for(int j=0;j<3;j++) {
//					arr[i][j]=sc.nextInt();
//					if(j==0) win+=arr[i][j];
//					else if(j==1 && arr[i][j]!=0) {draw+=arr[i][j]; drawCnt++;}
//					else if(j==2) lose+=arr[i][j];
//					sum+=arr[i][j]; arr[i][3]+=arr[i][j];
//				}
//				if(arr[i][3]!=5) flag=false;
//			}
//			if(flag && win==lose && sum==30 && drawCnt!=1 && draw%2==0 && win<=15 && lose<=15) System.out.print("1 ");
//			else System.out.print("0 ");
//		}
//		sc.close();
//	}
//}

//Main
import java.util.*;
public class bj6987 {
	static int[][] arr;
	static String s;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		arr = new int[6][3];
		for(int t=0; t<4; t++) {
			for(int i=0;i<6;i++) {
				for(int j=0;j<3;j++) {
					arr[i][j] = sc.nextInt();
				}
			}
			s="0 ";
			dfs(0,1,new int[6][3]);
			System.out.print(s);
		}
		sc.close();
	}

	static void dfs(int team1, int team2, int[][] chk) {
		if(team2==6) {
			boolean flag = true;
			for(int i=0;i<6;i++) {
				for(int j=0;j<3;j++) {
					if(arr[i][j]!=chk[i][j]) flag=false;
				}
			}
			if(flag) s="1 ";
			return;
		}

		//System.out.println(team1+" "+team2);
		for(int n=0;n<3;n++) {
			switch(n) {
			case 1://팀1승
				chk[team1][0]++;
				chk[team2][2]++;
				if(team2==5) dfs(team1+1,team1+2,chk);
				else dfs(team1,team2+1,chk);
				chk[team1][0]--;
				chk[team2][2]--;
				break;
			case 2://팀1패
				chk[team1][2]++;
				chk[team2][0]++;
				if(team2==5) dfs(team1+1,team1+2,chk);
				else dfs(team1,team2+1,chk);
				chk[team1][2]--;
				chk[team2][0]--;
				break;
			case 0://무승부
				chk[team1][1]++;
				chk[team2][1]++;
				if(team2==5) dfs(team1+1,team1+2,chk);
				else dfs(team1,team2+1,chk);
				chk[team1][1]--;
				chk[team2][1]--;
			}
		}
	}
}