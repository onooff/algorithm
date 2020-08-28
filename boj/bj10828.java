import java.util.*;

public class bj10828 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] stack = new int[10001];
		int size = 0;
		
		int n = Integer.parseInt(sc.next());
		
		String c = null; // command
		for(int i=0;i<n;i++) {
			c=sc.next();
			switch (c.charAt(0)) {
			case 'p':{
				if(c.charAt(1)=='u') {//push
					stack[++size]=Integer.parseInt(sc.next());
				}
				else {//pop
					if(size==0) System.out.println(-1);
					else System.out.println(stack[size--]);				
				}
				break;
			}
			case 's':{System.out.println(size); break;}//size
			case 'e':{//empty
				if(size==0) System.out.println(1);
				else System.out.println(0);
				break;
			}
			case 't':{//top
				if(size==0) System.out.println(-1);
				else System.out.println(stack[size]);
			}
			}
			
		}
		
		sc.close();
	}
}
