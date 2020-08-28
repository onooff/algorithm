//Main
import java.util.*;
public class bj14648 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int m = sc.nextInt();

		int[] arr = new int[n+1];

		int i,j,q;
		int a,b,c,d,tmp;
		long s1,s2;
		for(i=1;i<=n;i++) {
			arr[i]=sc.nextInt();
		}
		for(i=0;i<m;i++) {
			q=sc.nextInt();
			if(q==1) {
				a=sc.nextInt();
				b=sc.nextInt();
				s1=0;
				for(j=a;j<=b;j++) s1+=arr[j];
				System.out.println(s1);
				tmp=arr[a]; arr[a]=arr[b]; arr[b]=tmp;
			}
			else if(q==2) {
				a=sc.nextInt();
				b=sc.nextInt();
				c=sc.nextInt();
				d=sc.nextInt();
				s1=0;
				s2=0;

				for(j=a;j<=b;j++) s1+=arr[j];
				for(j=c;j<=d;j++) s2+=arr[j];
				System.out.println(s1-s2);
			}
		}

		sc.close();
	}
}