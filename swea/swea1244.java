import java.util.*;
 
public class swea1244 {
    static String N;
    static int S;
    static char[] Arr;
    static int Best = Integer.MIN_VALUE;
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t=sc.nextInt();
        for(int tc=1;tc<=t;tc++) {
        	
            N = sc.next();//숫자, String으로 읽은 후 toCharArray로 배열로 만들어서 perm
            Arr = N.toCharArray();
            S = sc.nextInt();//swap 시행 횟수
            
            perm(0);
             
            System.out.printf("#%d %d%n",tc,Best);
            Best=Integer.MIN_VALUE; 
        }
        sc.close();
    }
 
    static void perm(int k){
        if (k==Arr.length) {
            int r = Integer.parseInt(String.valueOf(Arr));
            //System.out.println(Arrays.toString(Arr));
            if(Best<r) Best=r;
            return;
        }
        
        for(int i=k;i<Arr.length;i++) {                   
            //if(i==k) continue;
        	swap(i,k);
            perm(k+1);
            swap(i,k);
        }
    }
 
    static void swap(int k, int i) {
        char temp = Arr[k];
        Arr[k] = Arr[i];
        Arr[i] = temp;
    }
}



//import java.util.*;
//
//public class swea1244 {
//	static String N;
//	static int S;
//	static char[] Arr;
//	static Integer[] IntArr;
//	static int Best = Integer.MIN_VALUE;
//	public static void main(String[] args) {
//		Scanner sc = new Scanner(System.in);
//		int t=sc.nextInt();
//
//		for(int tc=1;tc<=t;tc++) {
//			N = sc.next();
//			S = sc.nextInt();
//
//			Arr = N.toCharArray();
//			IntArr = new Integer[Arr.length];
//			for(int i=0;i<Arr.length;i++) IntArr[i]=Arr[i]-'0';
//
//			if(S>IntArr.length) {
//				Arrays.sort(IntArr, Collections.reverseOrder());
//				S=S%IntArr.length;
//			}
//			perm(IntArr.length,0);
//
//			System.out.printf("#%d %d%n",tc,Best);
//			Best=Integer.MIN_VALUE;
//		}
//		sc.close();
//	}
//
//	static void perm(int n, int k){
//		if (k==S) { 
//			int r = 0;
//			int d = 1;
//			for(int i=IntArr.length-1;i>=0;i--) {
//				r+=IntArr[i]*d;
//				d*=10;
//			}
//			//System.out.println("num: "+r);
//			if(Best<r) {
//				Best=r;
//			}
//		}
//
//		for(int i=k;i<n;i++) {                   
//			swap(i,k);
//			perm(n,k+1);
//			swap(i,k);
//		}
//	}
//
//
//	static void swap(int k, int i) {
//		int temp = IntArr[k];
//		IntArr[k] = IntArr[i];
//		IntArr[i] = temp;
//	}
//}
