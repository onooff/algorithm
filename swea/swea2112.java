//Solution
import java.util.*;
public class swea2112 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int t = sc.nextInt();

		for(int tc=1;tc<=t;tc++) {

			int n = sc.nextInt();
			int m = sc.nextInt();
			int k = sc.nextInt();

			int[][] map = new int[n][m];
			for(int i=0;i<n;i++) {
				for(int j=0;j<m;j++) {
					map[i][j]=sc.nextInt();
				}
			}

			Queue<node> q = new LinkedList<>();
			q.offer(new node(map,new boolean[n],0));

			boolean[] chk;
			int cnt = 0;
			boolean isOK = false;
			int last,cntK;
			node tmp;
			int[][] tmpMap;
			
			while(!isOK) {
				isOK=true;
				tmp=q.poll();
				map=tmp.map;
				cnt=tmp.cnt;
				chk=tmp.chk;

				loop:for(int j=0;j<m;j++) {
					last=-1;
					cntK=0;
					for(int i=0;i<n;i++) {
						if(last==-1) {last = map[i][j]; cntK++;}
						else {
							if(map[i][j]==last) {
								cntK++;
							}
							else{
								last = map[i][j];
								cntK=1;
							}
						}

						if(cntK>=k) {continue loop;}
					}
					//System.out.println("fail");
					isOK=false;
					break;
				}

				if(!isOK) {
					cnt++;
					System.out.println(cnt);
					if(cnt>=k) break;
					
					for(int i=0;i<n;i++) {
						if(!chk[i]) {
							chk[i]=true;
							tmpMap=deepCopy(map);
							Arrays.fill(tmpMap[i], 0);
							q.offer(new node(deepCopy(tmpMap),Arrays.copyOf(chk, chk.length),cnt));
							Arrays.fill(tmpMap[i], 1);
							q.offer(new node(deepCopy(tmpMap),Arrays.copyOf(chk, chk.length),cnt));
							chk[i]=false;
						}
					}
				}
			}

			System.out.printf("#%d %d%n",tc,cnt);
		}

		sc.close();
	}
	static int[][] deepCopy(int[][] original) {
		if (original == null) {
			return null;
		}

		int[][] result = new int[original.length][original[0].length];
		for (int i = 0; i < original.length; i++) {
			System.arraycopy(original[i], 0, result[i], 0, original[i].length);
		}
		return result;
	}
	static class node{
		int[][] map;
		boolean[] chk;
		int cnt;
		public node(int[][] map, boolean[] chk, int cnt) {
			super();
			this.map = map;
			this.chk = chk;
			this.cnt = cnt;
		}
	}
}