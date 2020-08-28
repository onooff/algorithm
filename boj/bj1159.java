import java.util.*;
public class bj1159 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int i,j,cnt;
		boolean flag=false;
		int n = sc.nextInt();
		
		String[] arr = new String[n];
		
		for(i=0;i<n;i++) {
			arr[i]=sc.next();
		}
		
		for(i=0;i<26;i++) {
			cnt=0;
			for(j=0;j<n;j++) {
				if(arr[j].charAt(0)=='a'+i) cnt++;
				if(cnt>=5) {System.out.print((char)('a'+i)); flag=true; break;}
			}
		}
		if(!flag) System.out.println("PREDAJA");
		
		sc.close();
	}
}