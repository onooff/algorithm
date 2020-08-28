import java.util.Arrays;
import java.util.Scanner;
 
public class swea5656_answer{
    static int N, W, H, result;
    static int popnum,cnt2,totalnum;
    static int MAP[][],MAPinint[][];
    static int order[];
    static boolean check[];
    static int[] dx = { 0, 0, 1, -1 };
    static int[] dy = { 1, -1, 0, 0 };
    static Scanner sc = new Scanner(System.in);
 
    static class data {
        int x;
        int y;
 
        data(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
 
    public static void main(String[] args) {
        int T = Integer.parseInt(sc.nextLine());
        for (int tc = 1; tc <= T; tc++) {
            input();
            sol();
            System.out.println("#" + tc + " " + (totalnum-result));
        }
    }
 
    static void sol() { 
        dfs(0);//중복 순열
     
    }
 
    private static void dfs(int cnt) {// w개 중 n개를 뽑는다
        if (cnt == N) {
            check = new boolean[H + 1];
            solution();
            if(cnt2>result)
                result=cnt2;
            return;
        }
        for (int i = 1; i <= W; i++) {
            order[cnt] = i;
            dfs(cnt + 1);
        }
 
    }
 
    private static void pop(int x, int y, int num) {
        //System.out.println(x + " " + y);
        cnt2++;
        MAP[x][y] = 0;
        if (num > 1) {
            for (int k = 0; k < 4; k++) {
                for (int i = 1; i < num; i++) {
                    int nx = x + dx[k] * i;
                    int ny = y + dy[k] * i;
 
                    if (nx <= 0 || ny <= 0 || nx > H || ny > W)
                        continue;
                    if (MAP[nx][ny] == 0)
                        continue;
                    if (check[nx] != true)
                        check[nx] = true;
 
                    pop(nx, ny, MAP[nx][ny]);
                }
            }
        }
     
    }
    private static void push(int x,int y) {
        //System.out.println(x+","+y);
        int nx=x-1;
        if(nx<=0) {
            MAP[x][y]=0;
        }
        else
        {
            MAP[x][y]=MAP[nx][y];
            push(nx,y);
        }
         
    }
    private static void solution() {
        cnt2=0;
        for (int i = 1; i <= H; i++) {
            for (int j = 1; j <= W; j++) {
                MAP[i][j]=MAPinint[i][j];
            }
        }
         
        for (int n = 0; n < N; n++) {
            int y = order[n];
            for (int m = 1; m <= H; m++) {
                if (MAP[m][y] != 0) {
                    Arrays.fill(check, false);
                    pop(m, y, MAP[m][y]);
                    break;
                }
            }
             
             
            for(int i=1;i<=H;i++)
            {
                if(check[i]==true)
                {
                    for(int j=1;j<=W;j++)
                    {
                        if(MAP[i-1][j]!=0&&MAP[i][j]==0)
                        {
                            push(i,j);
                             
                        }
                    }
                }
            }
//          System.out.println("**********"+cnt);
//          for (int i = 1; i <= H; i++)
//              System.out.println(Arrays.toString(MAP[i]));
             
        }
 
    }
 
    static void input() {
         
        String s = sc.nextLine();
        String[] arr = s.split(" ");
        N = Integer.parseInt(arr[0]);
        W = Integer.parseInt(arr[1]);
        H = Integer.parseInt(arr[2]);
        cnt2=0;
        totalnum=0;
        result=Integer.MIN_VALUE;
        MAPinint = new int[H + 1][W + 1];
        MAP = new int[H + 1][W + 1];
        order=new int[N];
        for (int i = 1; i <= H; i++) {
            s = sc.nextLine();
            for (int j = 1; j <= W; j++) {
                MAPinint[i][j] = Integer.parseInt(s.split(" ")[j - 1]);
                if(MAPinint[i][j]!=0) totalnum++;
            }
        }
     
    }
}