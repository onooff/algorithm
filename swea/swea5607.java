import java.util.*;
public class swea5607 {
	static int mod = 1234567891;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int t = sc.nextInt();

		for(int tc=1;tc<=t;tc++) {
			long n = sc.nextLong();
			long r = sc.nextLong();

			System.out.printf("#%d %d%n",tc,
					myFactorial(n)*myPow((myFactorial(n-r)*myFactorial(r))%mod,mod-2)%mod
					);
		}

		sc.close();
	}

	private static long myPow(long b, long e) {
		if(e == 0) return 1;
		if(e == 1) return b;

		long num = myPow(b, e/2)%mod;
		if(e%2==0) {return (num*num)%mod;}
		else{return (((num*num)%mod)*b)%mod;}
	}
	private static long myFactorial(long n) {
		long result = 1;
		for(int i=1;i<=n;i++) {
			result*=i;
			result%=mod;
		}
		return result;
	}
}