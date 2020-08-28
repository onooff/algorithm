import java.util.*;
public class swea3234 {
	static int n,cnt,sum;
	static int[] chu;
	static boolean[] chk;
	static int exponential[] = { 1, 2, 4, 8, 16, 32, 64, 128, 256, 512 };
    static int factorial[] = { 0, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880 };
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int t = sc.nextInt();

		for(int tc=1;tc<=t;tc++) {
			n=sc.nextInt();
			cnt=0;
			sum=0;
			chu = new int[n];
			chk = new boolean[n];
			for(int i=0;i<n;i++) {
				chu[i]=sc.nextInt();
				sum+=chu[i];
			}
			dfs(0,0,0);
			System.out.printf("#%d %d%n",tc,cnt);
		}
		sc.close();
	}

	static void dfs(int chuCnt,int lSum,int rSum) {
		if(chuCnt==n) {
			cnt++;
			return;
		}
		if(lSum >= sum - lSum) {
			cnt+=exponential[n-chuCnt]*factorial[n-chuCnt];
			return;
		}
		for(int i=0;i<n;i++) {
			if(!chk[i]) {
				chk[i]=true;
				dfs(chuCnt+1,lSum+chu[i],rSum);
				if(rSum+chu[i]<=lSum) {
					dfs(chuCnt+1,lSum,rSum+chu[i]);
				}
				chk[i]=false;
			}
		}
	}
}

/*
static void method(int idx) {
if(idx == N) {
    answer++;
    return;
}
int temp = list[order.get(idx)];
left += temp;
method(idx + 1);
left -= temp;
right += temp;
if(left < right) {
    right -= temp;
    return;
}
method(idx + 1);
right -= temp;
}

static void dfs(int idx) {
if(idx == N) {
    // 여기서 경우마다 진행
    left = 0; right = 0;
    method(0);
    return;
}

for(int i = 0; i < N; i++) {
    if(!visit[i]) {
        visit[i] = true;
        order.add(i);
        dfs(idx + 1);
        order.removeLast();
        visit[i] = false;
    }
}
}
 */