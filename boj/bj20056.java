import java.util.*;
public class bj20056 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int i,j,go,s;//for문에 쓸 변수
		int n = sc.nextInt(); // map 사이즈 = nxn
		int m = sc.nextInt(); // 파이어볼 개수
		int k = sc.nextInt(); // 시뮬레이션 시행횟수
		
		//파이어볼이 돌아다닐 map을 이차원 배열 큐로 선언
		Queue<fireball>[][] map = new Queue[n][n];
		for(i=0;i<n;i++) {
			for(j=0;j<n;j++) {
				map[i][j] = new LinkedList<fireball>();
			}
		}
		
		boolean moved = false; //이번 시행에서 이미 이동을 완료한 파이어볼인지 아닌지 판단할 bool
		for(i=0;i<m;i++) {
			map[sc.nextInt()-1][sc.nextInt()-1].offer(new fireball(sc.nextInt(), sc.nextInt(), sc.nextInt(), !moved));
		}
		
		fireball temp; //임시 파이어볼 객체 공간
		int size, sumM, sumS, oddOrEven; //파이어볼이 합쳐질때 사용할 변수들 size = 합쳐지는 파이어볼 개수, sumM = 질량 합, sumS = 속력합, oddOrEven = 나눠진 파이어볼들의 방향을 결정하기 위해 합쳐지는 파이어볼들의 방향관계 확인
		boolean sumD; //분리될 파이어볼들의 방향 => false = 십자 ,true = X자
		
		//k번 시뮬레이션 시행
		for(go=0;go<k;go++) {
			//이동 시행
			for(i=0;i<n;i++) {
				for(j=0;j<n;j++) {
					if(!map[i][j].isEmpty()) { //map[i][j]에 파이어볼이 있으면
						size = map[i][j].size();
						for(s=0;s<size;s++) { //map[i][j]에 있는 파이어볼 각각에 대해서 반복
							temp = map[i][j].poll();
							if(temp.isMoved == moved) {//이미 다른데서 움직여서 온 파이어볼일수 있다 그런놈들 걸러줌
								map[i][j].offer(temp);
								continue;
							}
							
							temp.isMoved = moved; //이제 움직인 파이어볼이 되므로 isMoved를 moved로 만듬
							
							switch(temp.d) { //방향에 따라서 move함수로 계산된 좌표에 파이어볼 넣는다
							case 0:
								map[move(n,i,-temp.s)][j].offer(temp);
								break;
							case 1:
								map[move(n,i,-temp.s)][move(n,j,temp.s)].offer(temp);
								break;
							case 2:
								map[i][move(n,j,temp.s)].offer(temp);
								break;
							case 3:
								map[move(n,i,temp.s)][move(n,j,temp.s)].offer(temp);
								break;
							case 4:
								map[move(n,i,temp.s)][j].offer(temp);
								break;
							case 5:
								map[move(n,i,temp.s)][move(n,j,-temp.s)].offer(temp);
								break;
							case 6:
								map[i][move(n,j,-temp.s)].offer(temp);
								break;
							case 7:
								map[move(n,i,-temp.s)][move(n,j,-temp.s)].offer(temp);
								break;								
							}
						}
					}
				}
			}
			
			//이동이 모두 끝난 후 파이어볼 합치기
			for(i=0;i<n;i++) {
				for(j=0;j<n;j++) {
					if(map[i][j].size()>1) { //파이어볼이 여러개 있는 칸이 있으면 합치기 시작
						size = map[i][j].size(); // 파이어볼의 개수 저장
						sumM=0; //사용할 변수 초기화
						sumS=0; //사용할 변수 초기화
						oddOrEven=-1; //사용할 변수 초기화
						sumD = false; //사용할 변수 초기화
						while(!map[i][j].isEmpty()) {//지금 칸에 있는 모든 파이어볼에 대해서 반복
							temp = map[i][j].poll(); //뽑아내서
							sumM+=temp.m;//질량 더하고
							sumS+=temp.s;//속도 더한다
							
							if(oddOrEven == -1) oddOrEven = temp.d%2; //첫번째 파이어볼의 방향이 짝수인지 홀수인지 확인해서 저장해둔다
							else if(temp.d%2!=oddOrEven) sumD=true; //이후 파이어볼이 첫번째 파이어볼과 방향이 다르다면 쪼개질 파이어볼들의 방향은 X자가 된다. 만약 모두 같으면 sumD는 false로 유지되어 십자가 될 것
						}
						
						if(sumM<5) continue; //합치기 계산이 끝난 후 질량 합이 5미만이라면 쪼개진 파이어볼의 질량은 0이 되므로 파이어볼이 소멸된다
						//소멸되지 않았다면 아래 코드가 수행된다
						
						if(sumD) {//쪼개지는 파이어볼이 X자로 퍼질 것이므로 1,3,5,7
							map[i][j].offer(new fireball(sumM/5, sumS/size, 1, moved));
							map[i][j].offer(new fireball(sumM/5, sumS/size, 3, moved));
							map[i][j].offer(new fireball(sumM/5, sumS/size, 5, moved));
							map[i][j].offer(new fireball(sumM/5, sumS/size, 7, moved));
						}
						else {//십자는 0,2,4,6
							map[i][j].offer(new fireball(sumM/5, sumS/size, 0, moved));
							map[i][j].offer(new fireball(sumM/5, sumS/size, 2, moved));
							map[i][j].offer(new fireball(sumM/5, sumS/size, 4, moved));
							map[i][j].offer(new fireball(sumM/5, sumS/size, 6, moved));
						}
					}
				}
			}
			moved = !moved;//다음 반복때 움직일 파이어볼 계산을 위해 moved를 반전시켜 줌
		}
		
		int result = 0; //결과값 넣을 변수
		for(i=0;i<n;i++) {
			for(j=0;j<n;j++) {
				while(!map[i][j].isEmpty()) { //파이어볼이 있으면
					temp = map[i][j].poll();
					result+=temp.m; //질량을 결과에 더한다
				}
			}
		}
		System.out.println(result); //결과를 출력한다
		sc.close();
	}
	
	static class fireball{ //파이어볼 객체
		int m;//질량
		int s;//속력
		int d;//방향
		boolean isMoved = false;//움직인 파이어볼인지 판단에 사용할 bool
		
		public fireball(int m, int s, int d, boolean isMoved) { //생성자
			super();
			this.m = m;
			this.s = s;
			this.d = d;
			this.isMoved = isMoved;
		}
	}
	
	static int move(int N, int now, int s) { //파이어볼 이동 후 좌표 계산하는 함수
		int r = (now+s)%N; //map 끝에 도달하면 반대쪽 끝으로 이어지는 구형 좌표계? 이므로 이렇게 계산하면 됨
		if(r<0) return N+r; // 결과가 음수면 N+결과 하면됨
		else return r; // 양수면 그대로 리턴
	}
}