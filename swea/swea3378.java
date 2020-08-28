import java.util.*;
public class swea3378 {
	//static int r,c,s;
	static char[][] pArr;
	static int[][] pArrCnt;//0=들여쓰기수 1=소괄호들여쓰기(x) 2=중괄호들여쓰기(y)값 3=대괄호들여쓰기(z)값 
	static List<int[]> pChk = new LinkedList<>();
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int t = sc.nextInt();

		for(int tc=1;tc<=t;tc++) {

			int p = sc.nextInt();
			int q = sc.nextInt();
			sc.nextLine();
			pArr = new char[p][];
			pArrCnt = new int[p][4];
			char[][] qArr = new char[q][];
			int s1=0,s2=0,m1=0,m2=0,l1=0,l2=0;
			//r=-1; c=-1; s=-1;

			for(int i=1;i<=20;i++) {
				for(int j=1;j<=20;j++) {
					for(int k=1;k<=20;k++) {
						pChk.add(new int[] {i,j,k});
					}
				}
			}

			for(int i=0;i<p;i++) {

				pArr[i] = sc.nextLine().toCharArray();
				for(int j=0;j<pArr[i].length;j++) {
					if(j==0 && pArr[i][j]=='.') {
						boolean flag=true;
						int dotCnt = 0;
						while(flag) {
							dotCnt++; j++;
							if(pArr[i][j]!='.') {
								flag=false; break;
							}
						}
						pArrCnt[i][0]=dotCnt;
					}

					switch(pArr[i][j]) {
					case '(':{s1++; break;}
					case ')':{s2++; break;}
					case '{':{m1++; break;}
					case '}':{m2++; break;}
					case '[':{l1++; break;}
					case ']':{l2++;}
					}
					
					if(i!=p-1) {
					pArrCnt[i+1][1]=s1-s2;
					pArrCnt[i+1][2]=m1-m2;
					pArrCnt[i+1][3]=l1-l2;
					}
				}
				//System.out.println(Arrays.toString(pArrCnt[i]));//dbg
			}
			
			calc();
			
			s1=0;s2=0;m1=0;m2=0;l1=0;l2=0;
			int result,tmp;
			StringBuilder sb = new StringBuilder("#"+tc);
			
			for(int i=0;i<q;i++) {
				//System.out.println(s1+" "+m1+" "+l1);//dbg
				
				result=(pChk.get(0)[0]*(s1-s2)+pChk.get(0)[1]*(m1-m2)+pChk.get(0)[2]*(l1-l2));
				for(int[] a:pChk) {
					tmp=(a[0]*(s1-s2)+a[1]*(m1-m2)+a[2]*(l1-l2));
					if(tmp!=result) {result=-1; break;}
				}
				
				sb.append(" "+result);
				
				qArr[i] = sc.nextLine().toCharArray();
				
				for(int j=0;j<qArr[i].length;j++) {
					//System.out.print(qArr[i][j]);//dbg
					switch(qArr[i][j]) {
					case '(':{s1++; break;}
					case ')':{s2++; break;}
					case '{':{m1++; break;}
					case '}':{m2++; break;}
					case '[':{l1++; break;}
					case ']':{l2++;}
					}
				}
				//System.out.println();//dbg
			}
			
			//System.out.println(r+" "+c+" "+s);//dbg
			System.out.println(sb);
		}

		sc.close();
	}
	
	static void calc() {
		int size = pChk.size();
		for(int i=0;i<size;i++) {
			for(int idx=1;idx<pArrCnt.length;idx++) {
				//System.out.println(Arrays.toString(pChk.get(i)));//dbg
				//System.out.println(pArrCnt[idx][1]*pChk.get(i)[0]+pArrCnt[idx][2]*pChk.get(i)[1]+pArrCnt[idx][3]*pChk.get(i)[2]+" "+pArrCnt[idx][0]);//dbg
				if(pArrCnt[idx][1]*pChk.get(i)[0]+pArrCnt[idx][2]*pChk.get(i)[1]+pArrCnt[idx][3]*pChk.get(i)[2]!=pArrCnt[idx][0]) {
					//r=pChk.get(i)[0]; c=pChk.get(i)[0]; s=pChk.get(i)[0];
					//return;
					pChk.remove(i); i--; size--; break;
				}
			}
		}

//		if(pChk.isEmpty()) {return;}
//		//for(int[] a : pChk) System.out.println(Arrays.toString(a));//dbg
//
//		size = pChk.size();
//		boolean flag[] = new boolean[3];
//		r=pChk.get(0)[0]; c=pChk.get(0)[1]; s=pChk.get(0)[2];
//		for(int i=1;i<size;i++) {
//			if(!flag[0] && r!=pChk.get(i)[0]) {r=-100000;}
//			if(!flag[1] && c!=pChk.get(i)[1]) {c=-100000;}
//			if(!flag[2] && s!=pChk.get(i)[2]) {s=-100000;}
//		}
	}
}