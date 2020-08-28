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
			
			boolean chk=true; //무너지는 모래성이 없는 경우 반복을 종료시키기 위한 부울변수
			boolean[][] damageChk = new boolean[n][m];//모래성에서 무너질 부분을 표시할 부울배열
			int cnt=0;//파도 횟수
			
			while(chk) {
				chk=false;//파도에 의해 무너지는 모래가 없을 경우 chk는 false로 유지되어 다음 반복문은 진행되지 않고 종료됨.
				for(int i=1;i<n-1;i++) {
					for(int j=1;j<m-1;j++) {
						if(arr[i][j]==0) continue;
						int damage = 0;
						int ni,nj;
						for(int k=0;k<8;k++) {
							ni=i+d[k][0];
							nj=j+d[k][1];
							if(arr[ni][nj] == 0) {
								damage++; // 8방탐색, 주변의 모래가 없는 좌표의 수를 카운트해서 데미지 산정
							}
						}
						
						if(arr[i][j]!=0 && damage>=arr[i][j]) { //현재 좌표의 모래강도가 데미지보다 같거나 작으면
							damageChk[i][j]=true; //현재 좌표의 모래는 무너질 예정이 되고
							chk=true; //다음 파도(반복문)을 진행시키기 위해 chk를 다시 false로 바꿔줌
						}
					}
				}
				
				if(chk) {//무너지는 모래가 있는 경우
					cnt++;//파도의 횟수 ++
					for(int i=1;i<n-1;i++) {
						for(int j=1;j<m-1;j++) {
							if(damageChk[i][j]) {arr[i][j]=0; damageChk[i][j]=false;}//무너질 예정으로 표시되었던 부분의 모래를 무너뜨려주고(0대입) 표시 삭제
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