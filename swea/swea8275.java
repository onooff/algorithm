import java.util.*;

public class swea8275 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();

		for(int tc=1;tc<=t;tc++) {
			
			int n = sc.nextInt();//케이지 갯수
			int x = sc.nextInt();//케이지 하나에 살 수 있는 최대 햄스터 수
			int m = sc.nextInt();//기록 갯수
			
			for(int i=0;i<m;i++) {
				int l = sc.nextInt();//l번 케이지부터
				int r = sc.nextInt();//r번 케이지까지
				int s = sc.nextInt();//햄스터가 총 s마리 있다
			}
			
			System.out.printf("#%d %d%n",tc,tc);
		}
		sc.close();
	}
}

/*
3
3 5 1
1 2 5
3 5 2
1 2 6
2 3 7
4 5 2
1 3 15
3 4 4 
*/