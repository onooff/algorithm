//Main
import java.util.*;
public class bj15953 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		for(int tc=1;tc<=t;tc++) {
			int[][] reward2017 = {
					{5000000,1},
					{3000000,2},
					{2000000,3},
					{500000,4},
					{300000,5},
					{100000,6}
			};//21등까지
			int[][] reward2018 = {
					{5120000,1},
					{2560000,2},
					{1280000,4},
					{640000,8},
					{320000,16}
			};//31등까지
			int j2017 = sc.nextInt()-1;
			int j2018 = sc.nextInt()-1;

			int sum = 0;
			if(j2017!=-1 && j2017<21) {
				int get = 0;
				for(int i=0;i<j2017;i++) {
					reward2017[get][1]--;
					if(reward2017[get][1]==0) get++;
				}
				sum+=reward2017[get][0];
			}
			if(j2018!=-1 && j2018<31) {
				int get = 0;
				for(int i=0;i<j2018;i++) {
					reward2018[get][1]--;
					if(reward2018[get][1]==0) get++;
				}
				sum+=reward2018[get][0];
			}
			System.out.printf("%d%n",sum);
		}
		sc.close();
	}
}