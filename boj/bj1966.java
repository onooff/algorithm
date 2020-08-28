import java.util.*;
public class bj1966 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int t = sc.nextInt();

		for(int tc=1;tc<=t;tc++) {

			int[] p = new int[10];
			int n = sc.nextInt();
			int m = sc.nextInt();
			int[] q = new int [n];

			for(int i=0; i<n; i++) {
				q[i]=sc.nextInt();
				p[q[i]]++;
			}

			int printable = 0;
			for(int i=9;i>=0;i--) {
				if(p[i]!=0) {printable=i; break;}
			}

			int idx = 0;
			int cnt = 1;
			while(true) {
				if(q[idx]==printable) {
					if(idx==m) {System.out.println(cnt); break;}
					cnt++;
					p[q[idx]]--;

					if(p[q[idx]]==0) {
						for(int i=q[idx];i>=0;i--) {
							if(p[i]!=0) {printable=i; break;}
						}
					}
					q[idx]=-1;
				}
				else idx = (idx+1)%n;
			}
		}
		sc.close();
	}
}