//Main
import java.io.*;
public class bj10989 {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
		
		int[] arr = new int[10001];

		int n = Integer.parseInt(br.readLine());
		for(int i=0;i<n;i++) {
			arr[Integer.parseInt(br.readLine())]++;
		}

		int cnt=0;
		StringBuilder sb = new StringBuilder();
		for(int i=0;i<arr.length;i++) {
			for(int j=0;j<arr[i];j++) {
				sb.append(i+"\n");
				cnt++;
			}
			if(cnt>=n) break;
		}
		System.out.println(sb.toString());
		br.close();
	}
}