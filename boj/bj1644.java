//Main
import java.util.*;
public class bj1644 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		ArrayList<Integer> prime = getPrimes(4100000);
		int n = sc.nextInt();
		int size = prime.size();
		int cnt = 0;
		int tmp,idx;
		
		for(int i=0;i<size;i++) {
			tmp=0;
			idx=i;
			if(prime.get(idx)>n) break;
			while(tmp<n) {
				tmp+=prime.get(idx++);
			}
			if(tmp==n) cnt++;
		}
		
		System.out.println(cnt);
		
		sc.close();
	}

	static ArrayList<Integer> getPrimes(int n){
		boolean[] arr = new boolean[n+1];
		arr[0]=true;
		arr[1]=true;
		int sqrt = (int)Math.sqrt(n);
	    for(int i=2; i<=sqrt; i++){
	        if(arr[i] == true)
	            continue;
	        for(int j=i+i; j<=n; j+=i){
	            arr[j] = true;
	        }
	    }
	    ArrayList<Integer> list = new ArrayList<Integer>();
	    for(int i=2; i<=n ; i++){
	        if(!arr[i])
	           list.add(i);
	    }
	    return list;
	}
}