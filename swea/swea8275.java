import java.util.*;

public class swea8275 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();

		for(int tc=1;tc<=t;tc++) {
			
			int n = sc.nextInt();//������ ����
			int x = sc.nextInt();//������ �ϳ��� �� �� �ִ� �ִ� �ܽ��� ��
			int m = sc.nextInt();//��� ����
			
			for(int i=0;i<m;i++) {
				int l = sc.nextInt();//l�� ����������
				int r = sc.nextInt();//r�� ����������
				int s = sc.nextInt();//�ܽ��Ͱ� �� s���� �ִ�
			}
			
			System.out.printf("#%d %d%n",tc,tc);
		}
		sc.close();
	}
}

/*
3
3 5 1
1 2 5
3 5 2
1 2 6
2 3 7
4 5 2
1 3 15
3 4 4 
*/