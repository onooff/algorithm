import java.util.Scanner;

public class bj2447 {
	
	private static char[][] starArr = new char[6561][6561];
	
	private static void makeStar(int n, int x, int y) {
		
		if(n<=0) {
			starArr[0][0] = '*';
			return;
		}
		
		int div = n/3;
		
		for(int i=x; i<x+n; i++) {
			for(int j=y; j<y+n; j++) {
				starArr[i][j] = starArr[i%n][j%n];
			}
		}
		
		for(int i=0; i<3; i++) {
			for(int j=0; j<3; j++) {
				if(i==1 && j==1) {
					continue;
				}
				makeStar(div, div*i, div*j);
			}
		}
		
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		
		sc.close();
		
		makeStar(n, 0, 0);
		
		StringBuilder sb = new StringBuilder();
		
		for(int i=0; i<n; i++) {
			for(int j=0; j<n; j++) {
				if(starArr[i][j]=='*') sb.append('*');
				else sb.append(" ");
			}
			sb.append("\n");
		}
		
		//sb.deleteCharAt(sb.length()-1);
		
		System.out.println(sb);
		
	}

}