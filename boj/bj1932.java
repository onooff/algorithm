import java.util.Scanner;

public class bj1932 {
	static int[][] t;
	static int[][] memo;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int i,j;
		
		int size = sc.nextInt();
		t=new int[size][];
		
		for(i=0;i<size;i++) {
			t[i]=new int[i+1];
			for(j=0;j<=i;j++) {
				t[i][j]=sc.nextInt();
			}
		}
		
		memo=new int[t.length][];
		for(i=0; i<memo.length; i++) {
			memo[i]=new int[t[i].length];
		}
		
		for(j=0; j<memo[memo.length-1].length; j++) {
			memo[memo.length-1][j]=t[memo.length-1][j];
		}
		
		for(i=memo.length-2; i>=0; i--) {
			for(j=0; j<memo[i].length; j++) {
				if(memo[i+1][j]>memo[i+1][j+1]) {
					memo[i][j]=t[i][j]+memo[i+1][j];
				}
				else memo[i][j]=t[i][j]+memo[i+1][j+1];
			}
		}
		System.out.println(memo[0][0]);
		sc.close();
	}
}
