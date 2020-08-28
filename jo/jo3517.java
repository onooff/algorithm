import java.util.Arrays;
import java.util.Scanner;

public class jo3517 {
	static int[] arr = null;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		arr = new int[n];
		
		for(int i=0;i<n;i++) {
			arr[i] = sc.nextInt();
		}
		
		Arrays.sort(arr);
		
		int q = sc.nextInt();
		for(int i=0;i<q;i++) {
			System.out.print(binary_search(sc.nextInt(),0,arr.length-1)+" ");
		}
	}
	
	static int binary_search(int t, int s, int e){//t=target s=start e=end
		/*
		if(s>e) {return -1;}
		int mid = (s+e)/2;
		
		if(t<arr[mid]) return binary_search(t,s,mid-1);
		if(t>arr[mid]) return binary_search(t,mid+1,e);
		return mid;
		*/
		int mid;
		while(s<=e) {
			mid = (s+e)/2;
			//System.out.println("mid:"+mid+" arr["+mid+"]:"+arr[mid]);
			if (arr[mid]==t) return mid;
			else if (t<arr[mid]) e=mid-1;
			else s=mid+1;
		}
		return -1;
	}
}
