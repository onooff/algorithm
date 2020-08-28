import java.util.Scanner;
import java.util.Stack;
public class bj2493 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int i=0, temp=0;
		int n = sc.nextInt();
		StringBuilder sb = new StringBuilder();
		Stack<Tower> s = new Stack<Tower>();
		for(i=1;i<=n;i++) {
			temp = sc.nextInt();
			while(!s.isEmpty()){
				if(s.peek().h>temp){sb.append(s.peek().idx+" "); break;}
				s.pop();
			}
			if(s.isEmpty()){sb.append("0 ");}
			s.push(new Tower(i,temp));
		}
		System.out.println(sb);

		sc.close();
	}
	static class Tower{
		public Tower(int i, int hh){
			this.idx=i;
			this.h=hh;
		}

		int idx;
		int h;
	}
}