//Main
import java.util.*;
public class bj2754 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		String s = sc.next();
		int score=0;

		switch (s.charAt(0)) {
		case 'F':
			break;
		case 'A':
			score=40;
			break;
		case 'B':
			score=30;
			break;
		case 'C':
			score=20;
			break;
		case 'D':
			score=10;
		}

		if(score!=0) {
			switch (s.charAt(1)) {
			case '+':
				score+=3;
				break;
			case '-':
				score-=3;
				break;
			case '0':
			}
		}

		System.out.println(score/10+"."+score%10);

		sc.close();
	}
}