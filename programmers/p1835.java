import java.util.HashMap;

public class p1835 {
	public static void main(String[] args) {
		String[] test = new String[] {"M~C<2", "C~M>1"};
        System.out.println(solution(test.length, test));
	}

	static char[] friends = null;

	static int size = 8;
	static boolean[] visited = new boolean[8];
	static int[] output = new int[8];
	static HashMap<Character, Integer> map = new HashMap<Character, Integer>();

	static int answer = 0;
	static String[] q = null;

	public static int solution(int n, String[] data) {
		char[] tmp = {'A','C','F','J','M','N','R','T'};
		friends=tmp;
        size = friends.length;
        visited = new boolean[size];
        output = new int[size];
        map = new HashMap<Character, Integer>();

        answer = 0;
		q = data;
		perm(0);
		return answer;
	}

	public static void perm(int depth) {
		if (depth == size) {
			for (int i = 0; i < size; i++) {
				map.put((char)friends[output[i]], i);
			}
			
			boolean isAnswer = true;
			char c1, c2, oper;
			int value, chk;
			for (String query : q) {
				c1 = query.charAt(0);
				c2 = query.charAt(2);
				oper = query.charAt(3);
				value = query.charAt(4) - '0';
				chk = Math.abs(map.get(c1)-map.get(c2))-1;
//				System.out.println(c1+" "+c2+" "+oper+" "+value+" "+chk);
				switch (oper) {
				case '>':
					if(chk<=value) isAnswer=false;
					break;
				case '<':
					if(chk>=value) isAnswer=false;
					break;
				case '=':
					if(chk!=value) isAnswer=false;
					break;
				default:
					break;
				}
				if(!isAnswer) break;
			}
			if(isAnswer) answer++;
//			if(isAnswer) {
//				for (int i = 0; i < size; i++) {
//					System.out.print((char)friends[output[i]]+" ");
//				}
//				System.out.println();
//			}
			return;
		}
		for (int k = 0; k < size; k++) {
			if (!visited[k]) {
				visited[k] = true;
				output[depth] = k;
				perm(depth + 1);
				visited[k] = false;
			}
		}
		return;
	}
}