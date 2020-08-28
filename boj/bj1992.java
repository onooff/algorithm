//Main
import java.util.*;
public class bj1992 {
	static int n;
	static char[][] map;
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		n = sc.nextInt();
		map = new char[n][];

		for(int i=0;i<n;i++) {
			map[i] = sc.next().toCharArray();
		}

		dfs(0,0,n);
		System.out.println(sb.toString());
		sc.close();
	}

	static void dfs(int i,int j,int range){
		if(range==1) {
			sb.append(map[i][j]);
			return;
		}

		char chk = map[i][j];

		for(int a=i;a<i+range;a++) {
			for(int b=j;b<j+range;b++) {
				if(chk!=map[a][b]) {
					sb.append('(');
					dfs(i,j,range/2);
					dfs(i,j+range/2,range/2);
					dfs(i+range/2,j,range/2);
					dfs(i+range/2,j+range/2,range/2);
					sb.append(')');
					return;
				}
			}
		}
		sb.append(chk);
	}
}