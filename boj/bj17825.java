//Main
import java.util.*;
public class bj17825 {
	static int max = Integer.MIN_VALUE;
	static int[] dice = new int[10];
	static int[] mal = {0,0,0,0};

	static int[] map = {
			0,
			2, 4, 6, 8,10,//1~5
			12,14,16,18,20,//6~10
			22,24,26,28,30,//11~15
			32,34,36,38,40,0,//16~20, 21=끝
			13,16,19,//10에서 갈림길 22,23,24
			28,27,26,//30에서 갈림길 25,26,27
			22,24,25,30,35//20에서 갈림길 28,29,30,31,32
	};

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		for(int i=0;i<10;i++) {
			dice[i]=sc.nextInt();
		}

		mal[0]=dice[0];

		dfs(1,map[mal[0]]);

		System.out.println(max);

		sc.close();
	}

	static void dfs(int turn, int point) {
		if(max<point) max=point;
		if(turn>=10) {
			return;
		}
		for(int i = 0;i<4;i++) {
			if(i!=0 && mal[i-1]==0) return;
			if(mal[i]==21) continue;
			
			int tmp = mal[i];
			int next = go(mal[i],dice[turn]);
			if(!isExist(next)) {
				mal[i]=next;
//				System.out.println(Arrays.toString(mal)+" "+(point+map[next]));
				dfs(turn+1, point+map[next]);
				mal[i]=tmp;
			}
		}
	}

	static boolean isExist(int n) {
		if(n==21) return false;
		for(int i = 0;i<4;i++) {
			if(mal[i]==n) return true;
		}
		return false;
	}

	static int go(int now, int d) {
		/*
		static int[] map = {
			0,
			2, 4, 6, 8,10,//1~5 => 22
			12,14,16,18,20,//6~10 => 28
			22,24,26,28,30,//11~15 => 25
			32,34,36,38,40,0,//16~20, 21=끝
			13,16,19,//10에서 갈림길 22,23,24 => 30
			28,27,26,//30에서 갈림길 25,26,27 => 30
			22,24,25,30,35//20에서 갈림길 28,29,30,31,32 => 20
		};
		 */
		switch(now) {
		case 5:
			d--;
			now=22;
			break;
		case 10:
			d--;
			now=28;
			break;
		case 15:
			d--;
			now=25;
			break;
		case 24:
			d--;
			now=30;
			break;
		case 27:
			d--;
			now=30;
			break;
		case 32:
			d--;
			now=20;
			break;
		}
		
		if(now<21) {
			now+=d;
			if(now>21) now=21;
			return now;
		}
		
		while(d>0) {
			d--;
			switch(now) {
			case 24:
				now=30;
				break;
			case 27:
				now=30;
				break;
			case 32:
				now=20+d;
				if(now>21) now=21;
				return now;
			default:
				now++;
			}
		}
		return now;
	}
}