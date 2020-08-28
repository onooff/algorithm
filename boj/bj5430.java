import java.util.*;

public class bj5430 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = Integer.parseInt(sc.next());
		String c = null;//command
		String s = null;//list
		int size = 0;

		loop:for(int tc=1;tc<=t;tc++) {
			c = sc.next();
			size = Integer.parseInt(sc.next());
			s = sc.next();

			s = s.replace("[", "");
			s = s.replace("]", "");
			String[] sArr = {};
			if(!"".equals(s)) sArr = s.split(",");

			boolean flag =false; //false = 정방향, true = 역방향
			int cl = c.length();
			int front = 0;
			int rear = sArr.length-1;

			for(int i=0; i<cl; i++) {
				switch(c.charAt(i)) {
				case 'R':{
					flag=!flag;
					break;
				}
				case 'D':{
					if(front>rear) {System.out.println("error"); continue loop;}
					if(flag) {
						rear--;
					}
					else {
						front++;						
					}
				}
				}
			}
			
			if(front>rear) {System.out.println("[]"); continue loop;}
			
			StringBuilder sb = new StringBuilder("[");
			if(flag) {
				for(int i=rear; i>=front; i--) {sb.append(sArr[i]); if(i!=front)sb.append(',');}
			}
			else {
				for(int i=front; i<=rear; i++) {sb.append(sArr[i]); if(i!=rear)sb.append(',');}
			}
			sb.append("]");
			System.out.println(sb);

		}
		sc.close();
	}
}
