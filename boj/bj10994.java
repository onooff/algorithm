//Main
import java.util.*;
public class bj10994 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		if(n==1) {System.out.println('*');}
		else {
			char[][] arr = new char[4*n-3][4*n-3];

			int i, j;//중심
			int[][] dd= {{0,-1},{-1,0},{0,1},{1,0}};
			int level=1;
			int a,b;
			while(true) {
				i=arr.length-(level*2-1);
				j=arr.length-(level*2-1);
				arr[i][j]='*';
				if(level==n) break;
				
				for(a=0;a<4;a++) {
					for(b=0;b<arr.length-(4*level-3);b++) {
						arr[i][j]='*';
						i+=dd[a][0];
						j+=dd[a][1];
						//System.out.println(i+" "+j);
					}
				}
				level++;
			}
			
			StringBuilder sb = new StringBuilder();
			for(i=0;i<arr.length;i++) {
				for(j=0;j<arr[i].length;j++) {					
					if(arr[i][j]=='*') sb.append('*');
					else sb.append(' ');
				}
				if(i!=arr.length-1) sb.append("\n");
			}
			System.out.print(sb.toString());
		}
		sc.close();
	}
}