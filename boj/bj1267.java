//Main
import java.util.*;
public class bj1267 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int[] arr = new int[n];
		
		for(int i=0;i<n;i++) arr[i]=sc.nextInt();
		
		int Y=0, M=0, tmp;
		for(int i=0;i<n;i++) {
			tmp=arr[i];
			while(tmp>=0) {tmp-=30; Y+=10;}
			tmp=arr[i];
			while(tmp>=0) {tmp-=60; M+=15;}
		}
		
		int min = Math.min(Y, M);
		if(Y==min) System.out.print("Y ");
		if(M==min) System.out.print("M ");
		System.out.println(min);
		sc.close();
	}
}
