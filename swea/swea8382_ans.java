import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class swea8382_ans {
    static class Point{
        int x, y, cnt;
        boolean dir;
        Point(int x, int y, int cnt, boolean dir){
            this.x = x;
            this.y = y;
            this.cnt = cnt;
            this.dir = dir;
        }
    }
    
    static int sx;
    static int sy;
    static int fx;
    static int fy;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for(int tc = 1; tc <= T; tc++) {
            sx = sc.nextInt() + 100;
            sy = sc.nextInt() + 100;
            fx = sc.nextInt() + 100;
            fy = sc.nextInt() + 100;
            
            //BFSŽ���� ���� Queue�ڷᱸ���� �غ�
            Queue<Point> queue = new LinkedList<>();
            //�湮üũ�� ���� �湮üũ ������ �غ�
            boolean[][][] visited = new boolean[201][201][2];
            //�������� ť�� ����
            queue.add( new Point(sx, sy, 0, true) );
            queue.add( new Point(sx, sy, 0, false) );
            //  ù �������� ���� ��ġ��, ���� �̵��� ���η� �̵��� �� �ִ� ����
            //  ù �������� ���� ��ġ��, ���� �̵��� ���η� �̵��� �� �ִ� ����
            //ť�� �̹� ���Ե� ���¿� ���ؼ��� �湮üũ
            visited[sx][sy][0] = true;
            visited[sx][sy][1] = true;
            
            //ť�� �������� ���¸� Ž��
            while( !queue.isEmpty() ) {
                Point point = queue.poll();
                //���� ������ ������ ��ǥ�� ��������� ����.
                if( point.x == fx && point.y == fy ) {
                    System.out.println("#" + tc + " " + point.cnt);
                    break;
                }
                if( point.dir ) {
                    //  ���� �ڽ��� ������ ���η� ���� ���
                    //     �ΰ��� �����̵��� ���ؼ� ��ȿ�ϴٸ�(����üũ, �湮üũ), ���³�带 ť�� �߰� �� �湮 üũ
                    for(int d = 0; d < 2; d++) {
                        int nx = point.x + dx[d];
                        int ny = point.y + dy[d];
                        if( nx < 0 || ny < 0 || nx > 200 || ny > 200 ) 
                            continue;
                        if( visited[nx][ny][0] )
                            continue;
                        queue.add( new Point(nx, ny, point.cnt + 1, !point.dir ));
                        visited[nx][ny][0] = true;
                    }
                }
                else {
                    //  ���� �ڽ��� ������ ���η� ���� ���
                    //     �ΰ��� ���� �̵��� ���ؼ� ��ȿ�ϴٸ�, ���³�带 ť�� �߰� �� �湮 üũ
                    for(int d = 2; d < 4; d++) {
                        int nx = point.x + dx[d];
                        int ny = point.y + dy[d];
                        if( nx < 0 || ny < 0 || nx > 200 || ny > 200 ) 
                            continue;
                        if( visited[nx][ny][1] )
                            continue;
                        queue.add( new Point(nx, ny, point.cnt + 1, !point.dir ));
                        visited[nx][ny][1] = true;
                    }
                }
            }
        }
    }
    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,-1,1};
}