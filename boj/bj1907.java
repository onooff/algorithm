//Main
import java.util.*;
public class bj1907 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s = sc.next()+"#";
		int[][] m = new int[3][3];//c,h,o 
		int l = s.length();
		int mIdx=0,idx;
		for(int i=0;i<l;i++) {
			switch(s.charAt(i)) {
			case'C':
				idx=0;
				break;
			case'H':
				idx=1;
				break;
			case'O':
				idx=2;
				break;
			default:
				idx=-1;	
			}
			if(idx==-1) {mIdx++; continue;}
			
			if(Character.isDigit(s.charAt(i+1))) {
				m[mIdx][idx]+=s.charAt(i+1)-'0';
				i++;
			}
			else {
				m[mIdx][idx]++;
			}
		}
		
//		for(int i=0;i<3;i++) {
//			for(int j=0;j<3;j++) {
//				System.out.print(m[i][j]);
//			}
//			System.out.println();
//		}
		
		
		sc.close();
	}
}