import java.util.Scanner;
public class swea1907_fail2 {
	static int[][] d = {
			{-1,-1},
			{-1,0},
			{-1,1},
			{0,1},
			{1,1},
			{1,0},
			{1,-1},
			{0,-1},
	};
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();

		for(int tc=1;tc<=t;tc++) {
			int n = sc.nextInt();
			int m = sc.nextInt();
			int[][] arr = new int[n][m];
			String tmp = sc.nextLine();
			
			for(int i=0;i<n;i++) {
				tmp = sc.nextLine();
				for(int j=0;j<m;j++) {
					if(tmp.charAt(j)=='.') arr[i][j]=0;
					else arr[i][j]=tmp.charAt(j)-'0';
				}
			}
			
			boolean chk=true; //�������� �𷡼��� ���� ��� �ݺ��� �����Ű�� ���� �οﺯ��
			boolean[][] damageChk = new boolean[n][m];//�𷡼����� ������ �κ��� ǥ���� �ο�迭
			int cnt=0;//�ĵ� Ƚ��
			
			while(chk) {
				chk=false;//�ĵ��� ���� �������� �𷡰� ���� ��� chk�� false�� �����Ǿ� ���� �ݺ����� ������� �ʰ� �����.
				for(int i=1;i<n-1;i++) {
					for(int j=1;j<m-1;j++) {
						if(arr[i][j]==0) continue;
						int damage = 0;
						int ni,nj;
						for(int k=0;k<8;k++) {
							ni=i+d[k][0];
							nj=j+d[k][1];
							if(arr[ni][nj] == 0) {
								damage++; // 8��Ž��, �ֺ��� �𷡰� ���� ��ǥ�� ���� ī��Ʈ�ؼ� ������ ����
							}
						}
						
						if(arr[i][j]!=0 && damage>=arr[i][j]) { //���� ��ǥ�� �𷡰����� ���������� ���ų� ������
							damageChk[i][j]=true; //���� ��ǥ�� �𷡴� ������ ������ �ǰ�
							chk=true; //���� �ĵ�(�ݺ���)�� �����Ű�� ���� chk�� �ٽ� false�� �ٲ���
						}
					}
				}
				
				if(chk) {//�������� �𷡰� �ִ� ���
					cnt++;//�ĵ��� Ƚ�� ++
					for(int i=1;i<n-1;i++) {
						for(int j=1;j<m-1;j++) {
							if(damageChk[i][j]) {arr[i][j]=0; damageChk[i][j]=false;}//������ �������� ǥ�õǾ��� �κ��� �𷡸� ���ʶ߷��ְ�(0����) ǥ�� ����
							//System.out.print(arr[i][j]+" ");
						}
						//System.out.println();
					}
				}
			}
			
			System.out.printf("#%d %d%n",tc,cnt);
		}
		
		sc.close();
	}
}