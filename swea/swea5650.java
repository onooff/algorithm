import java.util.*;
public class swea5650 {
	static final int UP = 0,RIGHT = 1,DOWN = 2,LEFT = 3; // 공 진행방향 상수로 선언 가독성 업
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		for(int tc=1;tc<=t;tc++) {
			int n = sc.nextInt();
			int[][] map = new int[n+2][n+2];//맵 2차원 배열로 선언할때 크기 +2 해서 테두리에 벽 있게 만듬
			Map<Integer, List<v>> wormholes = new HashMap<>();//웜홀은 해쉬맵으로 관리해서 맵 탐색 없이 찾을 수 있게 구현
			for(int i=0;i<n+2;i++) {
				for(int j=0;j<n+2;j++) {
					map[i][j]=5;
					if(i!=0 && i!=n+1 && j!=0 && j!=n+1) {						
						map[i][j] = sc.nextInt();
						if(map[i][j]>5) {
							if(!wormholes.containsKey(map[i][j])) {
								wormholes.put(map[i][j], new ArrayList<>());
							}
							wormholes.get(map[i][j]).add(new v(i,j));
						}
					}
				}
			}
			
			int max = 0;//모둔 경우의 수 중 최대 점수를 구해야 하므로 최대값 저장할 변수 선언
			for(int i=1;i<n+1;i++) {
				for(int j=1;j<n+1;j++) {
					if(map[i][j]==0) {//현재위지에 아무것도 없을 때 탐색 시작한다
						for(int go=0;go<4;go++) {//상하좌우 4방향 모두 탐색하기 위해 반복
							int point = 0;//점수 변수 초기화
							int nowI=i, nowJ=j;//현재 공 위치 좌표 변수 초기화
							int d = go;//공 진행방향
							do {
								switch(d){//현재 진행해야하는 방향에 따라 공 위치를 이동시킨다
								case UP:
									nowI--;
									break;
								case LEFT:
									nowJ--;
									break;
								case DOWN:
									nowI++;
									break;
								case RIGHT:
									nowJ++;
									break;
								}
								//이동 후에 현재 공 위치의 좌표에 무엇이 있는지 확인한다
								if(map[nowI][nowJ]==-1) break; //블랙홀이면 시행을 종료한다
								else if(map[nowI][nowJ]>=1 && map[nowI][nowJ]<=5) {//벽이면
									d=meetWall(map[nowI][nowJ], d);//벽 만남 처리 한다 - 현재 벽타입과 내 진행방향에 따라 다음 진행방향이 어디가 되어야 하는지 결정함
									point++;//점수도 1점 더해준다
								}
								else if(map[nowI][nowJ]!=0) {//웜홀이면
									v check = wormholes.get(map[nowI][nowJ]).get(0);//현재 칸의 웜홀번호의 첫번째 입구를 기준으로 확인한다
									if(check.i==nowI && check.j==nowJ) {//현재 공이 만난 웜홀이 첫번째 입구면
										check = wormholes.get(map[nowI][nowJ]).get(1);//두번째 입구 좌표로
										nowI=check.i;//이동
										nowJ=check.j;//시킨다
									}
									else {//첫번째 입구가 아니면 두번째 입구를 만난 상태이므로
										nowI=check.i;//첫번째 입구 좌표로
										nowJ=check.j;//이동시킨다
									}
								}
							} while(!(nowI==i && nowJ==j));//이 로직을 처음 출발지로 돌아올 때까지 반복한다
							if(max<point) max=point;//구해진 점수가 최대값이라면 최대값 변수에 저장한다
						}
					}
				}
			}
			System.out.printf("#%d %d%n",tc,max);//결과 출력한다
		}
		sc.close();
	}
	
	static class v{ // 좌표 저장할 클래스 웜홀 관리할 때 사용
		int i;
		int j;
		public v(int i, int j) {
			super();
			this.i = i;
			this.j = j;
		}
		@Override
		public String toString() {
			return "v [i=" + i + ", j=" + j + "]";
		}
	}
	static int meetWall(int type, int nowD) {
		int nextD = -1;
		switch(type) {
		case 1://◣ 벽 모양이 이거면
			switch(nowD) { //공 현재방향이
			case UP://위로가는 중이었으면
				nextD=DOWN; //다음에는 아래로 가야되고
				break;
			case LEFT://왼쪽으로 가는 중이었으면
				nextD=UP;//다음에는 위로 가야되고 그런식임
				break;
			case DOWN:
				nextD=RIGHT;
				break;
			case RIGHT:
				nextD=LEFT;
				break;
			}
			break;
		case 2://◤
			switch(nowD) {
			case UP:
				nextD=RIGHT;
				break;
			case LEFT:
				nextD=DOWN;
				break;
			case DOWN:
				nextD=UP;
				break;
			case RIGHT:
				nextD=LEFT;
				break;
			}
			break;
		case 3://◥
			switch(nowD) {
			case UP:
				nextD=LEFT;
				break;
			case LEFT:
				nextD=RIGHT;
				break;
			case DOWN:
				nextD=UP;
				break;
			case RIGHT:
				nextD=DOWN;
				break;
			}
			break;
		case 4://◢
			switch(nowD) {
			case UP:
				nextD=DOWN;
				break;
			case LEFT:
				nextD=RIGHT;
				break;
			case DOWN:
				nextD=LEFT;
				break;
			case RIGHT:
				nextD=UP;
				break;
			}
			break;
		case 5://■
			switch(nowD) {
			case UP:
				nextD=DOWN;
				break;
			case LEFT:
				nextD=RIGHT;
				break;
			case DOWN:
				nextD=UP;
				break;
			case RIGHT:
				nextD=LEFT;
				break;
			}
			break;
		}
		return nextD; // 결정된 다음 진행방향을 리턴해줌
	}
}