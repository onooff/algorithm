import java.util.*;

public class bj5431_fail2 {
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

			List<Integer> list = new ArrayList<Integer>();
			s = s.replace("[", "");
			s = s.replace("]", "");
			String[] sArr = {};
			if(!"".equals(s)) sArr = s.split(",");
			for(String tmp : sArr){
				list.add(Integer.parseInt(tmp));
			}

			boolean flag =false; //false = 정방향, true = 역방향
			int cl = c.length();

			for(int i=0; i<cl; i++) {
				switch(c.charAt(i)) {
				case 'R':{
					flag=!flag;
					break;
				}
				case 'D':{
					if(list.isEmpty()) {System.out.println("error"); continue loop;}
					if(flag) {
						list.remove(list.size()-1);
					}
					else {
						list.remove(0);						
					}
				}
				}
			}

			int ll = list.size();
			
			if(ll==0) {System.out.println("[]"); continue loop;}
			
			StringBuilder sb = new StringBuilder("[");
			if(flag) {
				for(int i=ll-1; i>0; i--) {
					sb.append(list.get(i)+",");
				}
				sb.append(list.get(0));
			}
			else {
				for(int i=0; i<ll-1; i++) {
					sb.append(list.get(i)+",");
				}
				sb.append(list.get(ll-1));
			}
			sb.append("]");
			System.out.println(sb);

		}
		sc.close();
	}
}
