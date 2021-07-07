import java.util.Scanner;

public class bj4354_java {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        while (!s.equals(".")) {
            int sl = s.length();
            int ans = 1;
            for (int i = 1; i < sl; i++) {
                if (sl % i == 0) {
                    String chk = s.substring(0, i);
                    Boolean isAns = true;
                    for (int j = i; j < sl; j += i) {
                        if (!chk.equals(s.substring(j, j + i))) {
                            isAns = false;
                            break;
                        }
                    }
                    if (isAns) {
                        ans = sl / i;
                        break;
                    }
                }
            }
            System.out.println(ans);
            s = sc.nextLine();
        }
        sc.close();
    }
}