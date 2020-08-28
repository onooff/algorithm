import java.util.*;

public class bj1786_sanghyeon {
   static List<Integer> list = new ArrayList<>();
   static int cnt = 0;
   
   static int[] getPi(String pattern) {
      int[] pi = new int[pattern.length()];
      int j = 0;

      for (int i = 1; i < pattern.length(); i++) {
         while (j > 0 && pattern.charAt(i) != pattern.charAt(j)) j = pi[j - 1];
         if (pattern.charAt(i) == pattern.charAt(j)) pi[i] = ++j;   
      }

      return pi;
   }
   
   static void KMP(String parent, String pattern) {
      int[] table = getPi(pattern);
      int j = 0; 
      
      for(int i = 0 ; i< parent.length(); i++) {
         while(j >0 && parent.charAt(i) != pattern.charAt(j)) j = table[j - 1];
         
         if(parent.charAt(i) == pattern.charAt(j)) {
            if(j == pattern.length()-1) {
               cnt++;
               list.add((i-pattern.length()+2));
               j = table[j];
            }
            else j++;         
         }
      }
   }
   
   public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
      
      String a = sc.nextLine();
      String b = sc.nextLine();
      
      KMP(a, b);
      
      System.out.println(cnt);
      for(int i=0;i<list.size();i++) System.out.println(list.get(i));
   }
   
}