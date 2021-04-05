
//Main
import java.util.*;

public class p42883 {
	public static void main(String[] args) {
//		Scanner sc = new Scanner(System.in);
		System.out.println(solution("12345678987654321", 10));
//		sc.close();
	}

	public static String solution(String number, int k) {
		String answer = "";
		char[] carr = number.toCharArray();
		int len = carr.length;
		Stack<Character> stk = new Stack<Character>();
		stk.push(carr[0]);
		int idx=1;
		int cnt=0;
		for(int i=1;i<len;i++) {
			if(cnt>=k) {
				stk.push(carr[i]);
			}
			else {
				while(!stk.isEmpty() && stk.peek()<carr[i] && cnt<k) {
					stk.pop();
					cnt++;
				}
				stk.push(carr[i]);
			}
		}
		while(cnt<k) {stk.pop(); cnt++;}
		while(!stk.isEmpty()) {
			answer=stk.pop()+answer;
		}
		return answer;
	}
}