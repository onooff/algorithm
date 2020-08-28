import java.util.*;
public class bj17143 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int R = sc.nextInt();
		int C = sc.nextInt();
		int M = sc.nextInt();

		List<fish>[][] pool = new ArrayList[R+1][C+1];
		int y,x,s,d,z;
		for(int i=0; i<M; i++) {
			y=sc.nextInt();
			x=sc.nextInt();
			s=sc.nextInt();
			d=sc.nextInt();
			z=sc.nextInt();
			pool[y][x].add(new fish(s,d,z));
		}
		
		int result = 0;
		fish tmp = null;
		int na,nb;
		for(int i=1; i<=C; i++) {
			for(int j=1; j<=R; j++) {//1.고기잡기
				if(!pool[j][i].isEmpty()) {result+=pool[j][i].remove(0).z; break;}
			}
			//2.고기이동
			for(int a=1;a<=R;a++) {
				for(int b=1;b<=C;b++) {
					if(!pool[a][b].isEmpty()) {
						na=a;
						nb=b;
						tmp = pool[a][b].remove(0);
						switch(tmp.d){
						case 1:{//위
							na-=tmp.s;
							while(!(na>=1 && na<=R)) {
								if(na<=0) na+=2;
							}
							break;
						}
						case 2:{//아래
							
							break;
						}
						case 3:{//오른쪽
							
							break;
						}
						case 4:{//왼쪽
							
							break;
						}
						}
					}
				}
			}
		}
		
		sc.close();
	}

	static class fish {
		int s;//속도
		int d;//방향 1위 2아래 3오른쪽 4왼쪽
		int z;//크기 
		public fish(int s, int d, int z) {
			super();
			this.s = s;
			this.d = d;
			this.z = z;
		}
	}
}
