import java.util.*;

public class bj2037 {
	static int p;
	static int w;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		p = sc.nextInt();
		w = sc.nextInt();
		
		sc.nextLine();
		char[] arr = sc.nextLine().toCharArray();
		int[] t = null;
		int lastB = -1;
		int sum=0;
		for(int i=0;i<arr.length;i++) {
			t=button(arr[i]);
			if(lastB==t[0] && t[0]!=1) {t[1]+=w;}
			sum+=t[1];
			lastB = t[0];
		}
		System.out.println(sum);
		sc.close();
	}
	static int[] button(char c) {
		int[] arr = new int[2];
		switch(c) {
		case 'C':{arr[1]+=p;}
		case 'B':{arr[1]+=p;}
		case 'A':{arr[1]+=p; arr[0]=2; break;}
		case 'F':{arr[1]+=p;}
		case 'E':{arr[1]+=p;}
		case 'D':{arr[1]+=p; arr[0]=3; break;}
		case 'I':{arr[1]+=p;}
		case 'H':{arr[1]+=p;}
		case 'G':{arr[1]+=p; arr[0]=4; break;}
		case 'L':{arr[1]+=p;}
		case 'K':{arr[1]+=p;}
		case 'J':{arr[1]+=p; arr[0]=5; break;}
		case 'O':{arr[1]+=p;}
		case 'N':{arr[1]+=p;}
		case 'M':{arr[1]+=p; arr[0]=6; break;}
		case 'S':{arr[1]+=p;}
		case 'R':{arr[1]+=p;}
		case 'Q':{arr[1]+=p;}
		case 'P':{arr[1]+=p; arr[0]=7; break;}
		case 'V':{arr[1]+=p;}
		case 'U':{arr[1]+=p;}
		case 'T':{arr[1]+=p; arr[0]=8; break;}
		case 'Z':{arr[1]+=p;}
		case 'Y':{arr[1]+=p;}
		case 'X':{arr[1]+=p;}
		case 'W':{arr[1]+=p; arr[0]=9; break;}
		case ' ':{arr[1]+=p; arr[0]=1; break;}
		}
		return arr;
	}
}
