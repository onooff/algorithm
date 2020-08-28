import java.util.*;
public class swea4534 {
	static int RESULT=0;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int t = sc.nextInt();

		for(int tc=1;tc<=t;tc++) {

			int n = sc.nextInt();
			List<Integer>[] tree = new List[n+1];
			for(int i=0;i<tree.length;i++) {
				tree[i] = new ArrayList<Integer>();
			}

			int a,b;

			for(int i=0;i<n-1;i++) {
				a = sc.nextInt();
				b = sc.nextInt();

				tree[a].add(b);
				tree[b].add(a);
			}

			dfs(tree,1,-1,n,true);
			dfs(tree,1,-1,n,false);

			System.out.printf("#%d %d%n",tc, RESULT); RESULT=0;
		}

		sc.close();
	}


	private static void dfs(List<Integer>[] tree, int idx, int p, int cnt, boolean lastColor) {//true = black, false = white
		tree[idx].remove((Integer)p);
		int d=tree[idx].size(); //degree
		if(cnt==0) {RESULT=(RESULT+1)%1000000007; return;}
		
		for(int i=0;i<d;i++) {
			if(!lastColor) dfs(tree,(int)tree[idx].get(i),idx,cnt-1,true);
			dfs(tree,(int)tree[idx].get(i),idx,cnt-1,false);
		}
	}
//	private static void dfs(List<Integer>[] tree, int idx, int p, int w, int b) {
	//		
	//		if(p!=-1) {
	//			//System.out.printf("tree[%d].remove(%d)\n",idx,p);//debug
	//			if(!tree[idx].isEmpty()) tree[idx].remove((Integer)p);
	//		}
	//
	//		int d=tree[idx].size(); //degree
	//		//System.out.printf("tree[%d].size()=%d\n",idx,d);//debug
	//
	//		int tmp=w;
	//		w=(b+tmp)%1000000007;
	//		b=tmp;
	//		//System.out.println(idx+"->"+w+" "+b);//debug
	//		
	//		if(d==0) {RESULT+=(w*b)%1000000007; return;}
	//		else{
	//			for(int i=0;i<d;i++) {
	//				dfs(tree,(int)tree[idx].get(i),idx,w,b);
	//			}
	//		}
	//	}
	
//	private static void dfs(List<Integer>[] tree, int idx, int p, boolean lastColor) {//ºÎ¸ðÀÇcolor true = black, false = white
//
//		if(p!=-1) {
//			//System.out.printf("tree[%d].remove(%d)\n",idx,p);//debug
//			if(!tree[idx].isEmpty()) tree[idx].remove((Integer)p);
//		}
//		int d=tree[idx].size(); //degree
//		//System.out.printf("tree[%d].size()=%d\n",idx,d);//debug
//
//		if(tree[idx].isEmpty()) {RESULT++; return;}
//		else{
//			for(int i=0;i<d;i++) {
//				if(!lastColor) dfs(tree,(int)tree[idx].get(i),idx,true);
//				dfs(tree,(int)tree[idx].get(i),idx,false);
//			}
//		}
//	}
}