import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.math.BigInteger;
public class bj1793 {
   public static void main(String[] args) throws Exception{
      //Scanner sc = new Scanner(System.in);
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
       //StringBuilder sb = new StringBuilder();
      BigInteger[] dp = new BigInteger[251];
      dp[0] = new BigInteger("1");
      dp[1] = new BigInteger("1");
      String tmp = br.readLine();

      while(tmp!=null) {
         int n = Integer.parseInt(tmp);
         if(BigInteger.ZERO.equals(dp[n])) {System.out.println(dp[n].toString()); continue;}

         for(int i=2;i<=n; i++) {
            if(BigInteger.ZERO.equals(dp[i])) continue;
            dp[i]=(dp[i-1].add(dp[i-2].multiply(new BigInteger("2"))));
         }

         System.out.println(dp[n].toString());
         tmp = br.readLine();
      }

      br.close();
   }
}