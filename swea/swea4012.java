import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class swea4012 {
	static int N;
	static int[][] S;
	static boolean[] visit;
	public static void main(String[] args) throws Exception{
		//Scanner sc = new Scanner(System.in);
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());

		for(int tc=1;tc<=t;tc++) {
			N=Integer.parseInt(br.readLine());
			S=new int[N][N];
			visit=new boolean[N];
			
			for(int i=0;i<N;i++) {
				StringTokenizer st = new StringTokenizer(br.readLine()," ");
				
			}
			
			System.out.printf("#%d %d%n",tc,tc);
		}
	}
}