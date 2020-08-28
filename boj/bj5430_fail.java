import java.util.*;

public class bj5430_fail {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = Integer.parseInt(sc.next());
		String c = null;//command
		String s = null;//stack
		int size = 0;

		for(int tc=1;tc<=t;tc++) {
			c = sc.next();
			size = Integer.parseInt(sc.next());
			s = sc.next();

			int[] stack = new int[size+1];

			int id = -1;
			char cc;
			for(int i=0;i<s.length();i++) {
				cc=s.charAt(i);
				if(Character.isDigit(cc)) {stack[++id]=cc-'0';}
			}

			//System.out.println("log:"+Arrays.toString(stack));

			int front = 0;
			int rear = stack.length-2;
			boolean flag = false; // false = front, true = rear
			for(int i=0;i<c.length();i++) {
				if(c.charAt(i)=='R') {
					flag = !flag;
				}
				else {
					if(flag) {rear--;}
					else {front++;}
				}
			}
			//System.out.println("log:"+front+" "+rear);
			if(front>rear) {System.out.println("ERROR"); continue;}
			System.out.print("[");
			if(flag) {
				for(int i=rear;i>=front;i--) {
					if(i==front) {System.out.print(stack[i]+"]"); continue;}
					System.out.print(stack[i]+",");
				}
			}
			else {
				for(int i=front;i<=rear;i++) {
					if(i==rear) {System.out.print(stack[i]+"]"); continue;}
					System.out.print(stack[i]+",");
				}
			}
			System.out.println();
		}

		sc.close();
	}
}
