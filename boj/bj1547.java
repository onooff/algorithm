//Main
import java.util.*;
public class bj1547 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		boolean[] cups = {false,true,false,false}; //idx 0은 사용 x
		
		int n = sc.nextInt();
		
		int a,b;
		boolean tmp;
		for(int i=0;i<n;i++) {
			a=sc.nextInt();
			b=sc.nextInt();
			tmp= cups[a];
			cups[a]= cups[b];
			cups[b]= tmp;
		}
		
		for(int i=1;i<=3;i++) {
			if(cups[i]) System.out.println(i);
		}
		
		sc.close();
	}
}