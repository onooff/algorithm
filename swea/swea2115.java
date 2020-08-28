import java.util.Arrays;
import java.util.Scanner;

public class swea2115 {

	static int N,M,C;
	static int WORKER = 2;
	static int[][] ARR = null;
	static int[] WORKZONE = null;
	static boolean[] CHK = null;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int t = Integer.parseInt(sc.nextLine());
		for(int tc=1;tc<=t;tc++) {
			N = sc.nextInt();
			M = sc.nextInt();
			C = sc.nextInt();
			ARR = new int[N][N];

			for(int i=0;i<N;i++) {
				for(int j=0;j<N;j++) {
					ARR[i][j] = sc.nextInt();
				}
			}

			System.out.printf("#%d %d%n",tc,honey(0,0,0));
		}

		sc.close();
	}

	static int honey(int ii, int jj, int depth) { //탐색 시작할 i, j, depth = 재귀호출깊이 = 일꾼 수

		int best = Integer.MIN_VALUE;
		WORKZONE = new int[M];
		CHK = new boolean[M];
		//int bi=-1, bj=-1;//debug

		for(int i=ii;i<N;i++) {	
			//if(depth==0 && i==N-1) break;

			int j = 0;
			if(depth!=0 && i == ii) {j=jj+M;}

			for(;j<=N-M;j++) {
				int temp = 0;
				for(int k=0;k<M;k++) {
					WORKZONE[k] = ARR[i][j+k];
				}

				temp += work(0);
				if(depth+1 < WORKER) {
					temp += honey(i,j,depth+1);
				}
				if(best<temp) {
					best = temp;
					//bi=i;bj=j;//debug	
				}
			}
		}
		//System.out.println("d="+depth+" i="+bi+" j="+bj);//debug
		return best;
	}

	//	static int work(int[] arr) {
	//		int best = Integer.MIN_VALUE;
	//		
	//		for(int i=0;i<arr.length;i++) {
	//			int sum = 0;
	//			int temp = 0;
	//			for(int j=i;j<arr.length;j++) {
	//				if(sum+arr[j]>C) continue;
	//				sum += arr[j];
	//				temp += arr[j]*arr[j];
	//			}
	//			if(best<temp) best = temp;
	//		}
	//		
	//		System.out.println("b="+best+" "+C+" "+arr.length);//debug
	//		return best;
	//	}
	//	static int work(int sum) {
	//		for(int i=0;i<M;i++) {
	//			if(!CHK[i]) {
	//				if(CHK[i]) {continue;}
	//				if(sum+WORKZONE[i]>C) {continue;}
	//				CHK[i]=true;
	//				work(sum+WORKZONE[i]);
	//				CHK[i]=false;
	//			}
	//		}
	//	}
	static int work(int sum) {
		int temp=0;

		for(int i=0;i<M;i++) {
			if(CHK[i]) {continue;}
			if(sum+WORKZONE[i]>C) {continue;}
			CHK[i]=true;
			int tt = work(sum+WORKZONE[i]);
			if(tt>temp) temp = tt;
			CHK[i]=false;
		}

		int temp2 = 0;
		for(int i=0;i<M;i++) {
			if(CHK[i]) {
				temp2 += WORKZONE[i]*WORKZONE[i];
				//System.out.print(WORKZONE[i]+" ");
			}
		}
		//System.out.println(" : "+temp +" "+temp2);
		if(temp<temp2) return temp2;
		return temp;
	}
}

/*
10
4 2 13
6 1 9 7
9 8 5 8
3 4 5 3
8 2 6 7
3 3 10
7 2 9
6 6 6
5 5 7
4 1 10
8 1 8 2
4 6 1 6
4 9 6 3
7 4 1 3
4 3 12
8 8 6 5
5 2 7 4
8 5 1 7
7 8 9 4
5 2 11
7 5 9 9 6
7 3 7 9 3
1 7 1 4 5
1 7 9 2 6
6 6 8 3 8
6 3 20
8 5 2 4 3 1
4 3 6 1 1 8
4 4 1 2 3 1
1 7 4 9 6 1
6 5 1 2 8 4
3 1 4 5 1 3
7 2 11
2 8 2 5 2 8 6
2 3 7 4 6 4 8
3 7 8 3 9 4 4
8 8 5 9 3 6 9
9 7 6 2 4 1 3
2 9 2 8 9 7 3
2 1 7 2 7 8 3
8 3 12
9 1 6 7 5 4 6 7
9 5 1 8 8 3 5 8
5 2 6 8 6 9 2 1
9 2 1 8 7 5 2 3
6 5 5 1 4 5 7 2
1 7 1 8 1 9 5 5
6 2 2 9 2 5 1 4
7 1 1 2 5 9 5 7
9 4 20
5 2 4 8 3 7 6 2 1
7 9 8 5 8 2 6 3 6
1 9 4 6 7 5 3 1 1
4 4 7 6 2 2 8 1 7
9 6 8 5 7 3 7 9 5
7 3 1 4 1 1 8 5 3
4 6 8 9 4 5 3 8 8
1 3 4 2 4 1 1 3 6
5 9 2 3 5 2 4 8 5
10 5 30
7 4 7 5 9 3 6 4 6 7
8 9 8 4 5 7 8 9 2 9
6 5 3 4 6 4 7 6 3 2
4 7 4 3 4 7 3 3 4 3
3 5 6 4 8 8 2 1 8 6
3 7 9 7 1 7 6 2 8 9
3 6 1 6 8 9 7 7 5 1
4 3 5 6 2 1 2 6 3 6
3 4 9 2 1 5 9 9 6 3
9 9 7 3 7 5 5 5 8 4


#1 174
#2 131
#3 145
#4 155
#5 166
#6 239
#7 166
#8 172
#9 291
#10 464

#1 174	ㅇ
#2 131	ㅇ
#3 145	ㅇ
#4 155	ㅇ
#5 166	ㅇ
#6 239	ㅇ
#7 166	ㅇ
#8 172	ㅇ
#9 291	ㅇ
#10 464	ㅇ


1
4 3 12
8 8 6 5
5 2 7 4
8 5 1 7
7 8 9 4

57 9
25 49 81 = 155


필요한 함수 기능 = 
파라미터 = 1차원 int배열
처리 = 합이 C이하인 모든 조합 작성
리턴 = 모든 조합 중 원소^2의 합이 가장 큰 조합을 찾아 그 값을 리턴?

*/