import java.util.*;
//////////틀림
/*틀리는케이스:
 * 73
 * 7654321
 */
public class bj2812 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int k = sc.nextInt();
		sc.nextLine();
		StringBuilder sb = new StringBuilder(sc.nextLine());
		int n1,n2,n3,best;
		int[] arr = new int[3];

		//int l = sb.length();
		while(k!=0) {
			//앞의 3자리 숫자 중 하나씩 뺀 3개의 2자리 숫자끼리 비교하여 가장 큰 값을 선택
			if(n<3) {break;}
			n1 = sb.charAt(0)-'0';
			n2 = sb.charAt(1)-'0';
			n3 = sb.charAt(2)-'0';

			arr[0]=n2*10+n3; //arr0이 가장 크면 i+0제거
			arr[1]=n1*10+n3; //arr1이 가장 크면 i+1제거
			arr[2]=n1*10+n2; //arr2이 가장 크면 i+2제거
			best = arr[0]>arr[1]? 0 : 1;
			best = arr[best]>arr[2]? best : 2;

			sb.deleteCharAt(best);
			n--; k--;
		}

		if(k!=0) {
			if(sb.charAt(0)<sb.charAt(1))sb.deleteCharAt(0);
			else sb.deleteCharAt(1);
		}
		System.out.println(sb);
	}
}