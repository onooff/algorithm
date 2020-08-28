//문제범위인 100000개까지 노드를 가질 수 있는 트리를 2차원 배열로 표현할 경우 메모리 박살남

import java.util.*;

public class bj11725_fail {
	static int n=0;
	static boolean[][] tree = null;
	static int[] root = null;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		n = sc.nextInt();
		tree = new boolean[n+1][n+1];
		root = new int[n+1];

		int a=0,b=0;
		for(int i=0;i<n-1;i++){
			a = sc.nextInt();
			b = sc.nextInt();

			tree[a][b]=true;
			tree[b][a]=true;
		}

		root[1]=1;
		dfs(1);

		for(int i=2;i<=n;i++){
			System.out.printf("%d\n",root[i]);
		}

		sc.close();
	}

	static void dfs(int idx){

		for(int i=1;i<=n;i++){
			if(tree[idx][i] && root[i]==0){

				root[i]=idx;
				dfs(i);
			}
		}
	}
}
/*
#include <stdio.h>

int n=0,a=0,b=0;
int tree[100001][100001];
int root[100001];

void dfs(int idx){
    for(int i=1;i<=n;i++){
        if(tree[idx][i] && !root[i]){
            root[i]=idx;
            dfs(i);
        }
    }
}

int main(){

    scanf("%d",&n);

    for(int i=1;i<=n;i++){
        scanf("%d %d",&a,&b);

        tree[a][b]=1;
        tree[b][a]=1;
    }

    root[1]=1;
    dfs(1);

    for(int i=2;i<=n;i++){
        printf("%d\n",root[i]);
    }

    return 0;
}

 */