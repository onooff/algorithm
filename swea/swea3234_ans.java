import java.util.Scanner;



public class swea3234_ans {



	private static int[] scale;

	private static Scanner scanner;

	private static int count = 0;

	private static int visited[];

        private static int exponential[] = { 1, 2, 4, 8, 16, 32, 64, 128, 256, 512 };

        private static int factorial[] = { 0, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880 };

        private static int sum = 0;

    

	public static void main(String[] args) {

		// TODO Auto-generated method stub

		scanner = new Scanner(System.in);

		int testCase = scanner.nextInt();

		int index = 0;

		while (testCase-- > 0) {

			int N = scanner.nextInt();

			scale = new int[N];

			visited = new int[N];

			for (int i = 0; i < N; i++) {

				scale[i] = scanner.nextInt();

				sum += scale[i];

			}



			calc(0, 0, 0, N);



			System.out.println("#" + (++index) + " " + count);

			sum = 0;

			count = 0;

		}

	}



	// visited 배열은 방문한 곳을 더이상 방문하지 않도록 , 즉 중복으로 left에 1 1 1 이렇게 안더해지도록 하는 역할

	private static void calc(int inx, int left, int right, int N) {

		if (inx >= N) {

			count += 1;

			return;

		}

		

		

		// 최대 카운트수는 2^n * n!이므로 

		// 아래와 같이 count에 추가해줍니다.

		// 단, left에 값을 계속해서 추가하고 있고, sum은 앞서 요소들의 전체 값이므로 

		// left >= sum - left의 조건을 만족하기 위해서는 결국 마지막까지는 돌아야 한다는 사실을 알 수 있다.

		// 가령 9를 예를 들면, 합은 45이며, left가 1~8까지의 합을 더했을 때 남은 9와 

		// sum - left의 결과인 9와 상충되므로 아래 조건을 만족한다.

		// 끝단까지 갔을 때 count를 하나씩 증가시키지 않고 바로 값을 추가하고 리턴하여 시간을 줄이는 것이다.

		if(left >= sum - left) {

			count += exponential[N-inx] * factorial[N-inx];

			return;

		}



		for (int i = 0; i < N; i++) {

			// 값을 left부터 먼저 넣고 돌리기



			if (visited[i] == 1)

				continue;



			visited[i] = 1;

			calc(inx + 1, left + scale[i], right, N);



			if (left - (scale[i] + right) >= 0)

				calc(inx + 1, left, right + scale[i], N);



			visited[i] = 0;

		}



	}



}