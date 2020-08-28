//Main
import java.util.*;
public class bj1457 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		char[] num = sc.next().toCharArray();

		int setCnt=1, need;
		int[] set = {1,1,1,1,1,1,1,1,1,1};
		for(int i=0;i<num.length;i++) {
			need = num[i]-'0';
			if(set[need]>0) set[need]--;
			else {
				if(need==6) {
					if(set[9]>0) set[9]--;
					else {
						setCnt++;
						for(int j=0;j<10;j++) {
							set[j]++;
						}
						set[need]--;
					}
				}
				else if(need==9) {
					if(set[6]>0) set[6]--;
					else {
						setCnt++;
						for(int j=0;j<10;j++) {
							set[j]++;
						}
						set[need]--;
					}
				}
				else {
					setCnt++;
					for(int j=0;j<10;j++) {
						set[j]++;
					}
					set[need]--;
				}
			}
		}
		//System.out.println(Arrays.toString(set));
		System.out.println(setCnt);

		sc.close();
	}
}