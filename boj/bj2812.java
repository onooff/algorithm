import java.util.*;
//////////Ʋ��
/*Ʋ�������̽�:
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
			//���� 3�ڸ� ���� �� �ϳ��� �� 3���� 2�ڸ� ���ڳ��� ���Ͽ� ���� ū ���� ����
			if(n<3) {break;}
			n1 = sb.charAt(0)-'0';
			n2 = sb.charAt(1)-'0';
			n3 = sb.charAt(2)-'0';

			arr[0]=n2*10+n3; //arr0�� ���� ũ�� i+0����
			arr[1]=n1*10+n3; //arr1�� ���� ũ�� i+1����
			arr[2]=n1*10+n2; //arr2�� ���� ũ�� i+2����
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