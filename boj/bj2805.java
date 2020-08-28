import java.util.*;
public class bj2805 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n=sc.nextInt();
		long m=sc.nextLong();

		int[] tree = new int[n];

		for(int i=0;i<n;i++) {
			tree[i]=sc.nextInt();
		}

		int low=0, high=2000000000, middle=0 ,lastMiddle=0;
		int sum=0,tmp;
		while(low<=high) {
			lastMiddle = middle;
			middle=(low+high)/2;
			sum=0;
			for(int i=0;i<n;i++) {
				tmp=tree[i]-middle;
				if(tmp>0) sum+=tmp;
			}
			//System.out.println(low+" "+middle+" "+high+"="+sum);
			if(sum==m) break;
			else if(sum>m) {
				low = middle+1;
			}
			else {//sum<m
				high = middle-1;
			}
		}
		if(sum<m) System.out.println(lastMiddle);
		else System.out.println(middle);
		sc.close();
	}
}