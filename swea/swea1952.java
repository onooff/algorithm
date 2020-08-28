import java.util.*;

public class swea1952 {
	static int BEST = 0;
	static int[] ARR = null;
	static boolean[] CHK = null;
	static int D,M,M3,Y,CNT;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int t = sc.nextInt();

		for(int tc=1;tc<=t;tc++) {

			D=sc.nextInt();
			M=sc.nextInt();
			M3=sc.nextInt();
			Y=sc.nextInt();
			ARR = new int[12];
			CHK = new boolean[14];
			BEST = Y;
			CNT=0;

			for(int i=0;i<12;i++) {
				ARR[i]=sc.nextInt();
				if(ARR[i]!=0) {CHK[i]=true; CNT++;} // CHK가 true면 해당 월 0 아님 = 처리 필요
			}

			calc(0, CNT,0);
			
			if(CNT==0) {BEST=0;}
			System.out.printf("#%d %d%n",tc,BEST);
		}

		sc.close();
	}

	static void calc(int idx, int cnt, int price) {
		//if(price>BEST) return;
		
		if(cnt<=0) {
			//System.out.println("lastPrice="+price);
			if(BEST>price) {
				BEST=price;
			}
			return;
		}

		int i;

		for(i=idx;i<12;i++) {
			if(CHK[i]) {
				int pTmp;
				////////////////////3개월////////////////////
				CHK[i]=false;
				int tmp = 1;
				boolean tmp1 = CHK[i+1]; CHK[i+1]=false; if(tmp1) tmp++;
				boolean tmp2 = CHK[i+2]; CHK[i+2]=false; if(tmp2) tmp++;
				pTmp = price+M3;
				if(pTmp<BEST) calc(i, cnt-tmp, pTmp);
				//CHK[i]=true;
				CHK[i+1]=tmp1;
				CHK[i+2]=tmp2;
				////////////////////1개월////////////////////
				//CHK[i]=false;
				pTmp = price+M;
				if(pTmp<BEST) calc(i, cnt-1, pTmp);
				//CHK[i]=true;
				////////////////////1일////////////////////
				//CHK[i]=false;
				pTmp = price+D*ARR[i];
				if(pTmp<BEST) calc(i, cnt-1, pTmp);
				CHK[i]=true;
				break;
			}
		}
	}
}