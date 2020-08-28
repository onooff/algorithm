import java.util.*;
public class swea1808 {
	static boolean[] arr = new boolean [10];
	static int NUM = 0;
	static int MIN = Integer.MAX_VALUE;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		
		for(int tc=1;tc<=t;tc++) {
			for(int i=0;i<10;i++) {
				arr[i]=false;
				if(sc.nextInt()==1) {arr[i]=true;}
			}
			NUM = sc.nextInt();
			
			if(NUM==1) MIN = 2;
			else dfs(0,NUM);
			
			if(MIN==Integer.MAX_VALUE) MIN=-1;
			System.out.printf("#%d %d%n",tc,MIN); MIN=Integer.MAX_VALUE;
		}
		
		sc.close();
	}
	
	static void dfs(int n,int num) { //n = 버튼 누른 횟수 num = 계산으로 구할 수
		//System.out.println(n+" "+num);
		if(num==1) {
			if(MIN>n) MIN=n;
			return;
		}
		
		for(int i = num; i>=2; i--) {
			if(num%i==0) {
				int cnt = 0;
				int tmp = i;
				boolean flag = true;
				while(tmp!=0) {
					if(!arr[tmp%10]) { flag=false; break; }
					tmp/=10;
					cnt++;
				}
				
				if(flag) {dfs(n+cnt+1,num/i);}
			}
		}
	}
}