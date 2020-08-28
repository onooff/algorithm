//Solution
import java.util.*;
public class swea5653 {
	
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int t = sc.nextInt();

		for(int tc=1;tc<=t;tc++) {
			
			
			
			System.out.printf("#%d %d%n",tc,tc);
		}

		sc.close();
	}
}

class Cell{
	int i;
	int j;
	int defaultLife;
	int nowLife;
}