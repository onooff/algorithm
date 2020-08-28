//Main
import java.util.*;
public class bj14649 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int[] stone = new int[100];//0=b 1=r 2=g
		double money = sc.nextDouble();
		int n = sc.nextInt();

		int start,i,j;
		char d;
		for(i=0;i<n;i++) {
			start = sc.nextInt()-1;
			d = sc.next().charAt(0);

			if(d=='L') {
				for(j=start-1;j>=0;j--) {
					stone[j]=(stone[j]+1)%3;
				}
			}
			else {//d=='R'
				for(j=start+1;j<100;j++) {
					stone[j]=(stone[j]+1)%3;
				}
			}
		}

		int[] r = new int[3];
		for(i=0;i<100;i++) {
			switch (stone[i]) {
			case 0:
				r[0]++;
				break;
			case 1:
				r[1]++;
				break;
			case 2:
				r[2]++;
				break;
			}
		}
		for(i=0;i<3;i++) System.out.printf("%.2f\n",money*((double)r[i]/100));
		sc.close();
	}
}