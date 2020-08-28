import java.util.*;
//public class Main {
public class bj1062 {
	static int[] c = new int[26];
	static int N,T,LIMIT=0,max=Integer.MIN_VALUE;
	static String[] words; //0=필요없음 1=필요함 2=사용중
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		N = sc.nextInt();
		T = sc.nextInt();

		if(T<5) {System.out.println('0'); sc.close(); return;}
		else T=T-5;

		words = new String[N];

		c['a'-'a']=2;
		c['n'-'a']=2;
		c['t'-'a']=2;
		c['i'-'a']=2;
		c['c'-'a']=2;

		int l;
		for(int i=0;i<N;i++) {
			words[i]=sc.next();
			words[i]=words[i].replaceAll("a", "");
			words[i]=words[i].replaceAll("n", "");
			words[i]=words[i].replaceAll("t", "");
			words[i]=words[i].replaceAll("i", "");
			words[i]=words[i].replaceAll("c", "");
			//System.out.println(words[i]);
			l=words[i].length();
			for(int j=0;j<l;j++) {
				if(c[words[i].charAt(j)-'a']!=1) {
					c[words[i].charAt(j)-'a']=1;
					LIMIT++;
				}
			}
		}
		//System.out.println(Arrays.toString(c));
		dfs(1,0);
		System.out.println(max);

		sc.close();
	}

	static void dfs(int idx, int n) {
		if(n==T || n==LIMIT) {
			int cnt=0;
			int l;
			for(int i=0;i<N;i++) {
				l=words[i].length();
				int j;
				for(j=0; j<l; j++) {
					if(c[words[i].charAt(j)-'a']!=2) break;
				}
				
				if(j==l) {cnt++;}
			}
			max = Math.max(cnt, max);
			return;
		}
		
		for(int i=idx; i<26; i++) {
			if(c[i]==1) {
				c[i]=2;
				dfs(i+1,n+1);
				c[i]=1;
			}
		}
	}
}



