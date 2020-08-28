import java.util.Scanner;
public class bj3025 {
	static class v{
		int i;
		int j;
		public v(int i, int j) {
			super();
			this.i = i;
			this.j = j;
		}
	}
	static boolean isIn(int i, int j, int r, int c) {
		if(i>=0 && j>=0 && i<r && j<c) {return true;}
		return false;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int r = sc.nextInt();
		int c = sc.nextInt();
		char[][] map = new char[r][];

		for(int a=0;a<r;a++) {
			map[a] = sc.next().toCharArray();
		}

		int n = sc.nextInt();
		int i,j;

		for(int k=0;k<n;k++) {
			i=0;
			j=sc.nextInt()-1;
			
			while(isIn(i+1,j,r,c)) {
				if(map[i+1][j]=='X') break;
				else if(map[i+1][j]=='O') {
					if(isIn(i,j-1,r,c) && map[i][j-1]=='.' && map[i+1][j-1]=='.') {
						i++;
						j--;
					}
					else if(isIn(i,j+1,r,c) && map[i][j+1]=='.' && map[i+1][j+1]=='.') {
						i++;
						j++;
					}
					else break; 
				}
				else i++;
			}
			map[i][j]='O'; 
		}

		for(int a=0;a<r;a++) {
			for(int b=0;b<c;b++) {
				System.out.print(map[a][b]);
			}
			System.out.println();
		}
		sc.close();
	}
}