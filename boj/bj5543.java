//Main
import java.util.*;
public class bj5543 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int i,minBurger=2001, minDrink=2001;
		for(i=0;i<3;i++) minBurger=Math.min(minBurger, sc.nextInt());
		for(i=0;i<2;i++) minDrink=Math.min(minDrink, sc.nextInt());
		System.out.println(minBurger+minDrink-50);

		sc.close();
	}
}