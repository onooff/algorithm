
//Main
import java.util.*;

public class p12904 {
	public static void main(String[] args) {
//		Scanner sc = new Scanner(System.in);
		System.out.println(solution("fdsafvevewveefsf"));
//		sc.close();
	}

	public static int solution(String s)
    {
        int answer = 1;
        int len=s.length();
        int l,r,ans;
        char[] arr = s.toCharArray();
        for(int i=0;i<len;i++) {
        	if(i+1<len && arr[i]==arr[i+1]) {
        		ans=2;
        		l=i;
        		r=i+1;
        		while(true) {
                    l--;
                    r++;
            		if(l>=0 && r<len) {
            			if(arr[l]!=arr[r]) break;
            		}
            		else {
            			break;
            		}
            		ans+=2;
            	}
            	if(answer<ans) answer=ans;
        	}
        	
    		ans=1;
    		l=i;
    		r=i;
    		
    		while(true) {
    			l--;
    			r++;
    			if(l>=0 && r<len) {
    				if(arr[l]!=arr[r]) break;
    			}
    			else {
    				break;
    			}
    			ans+=2;
    		}
    		if(answer<ans) answer=ans;
        	
        }
        return answer;
    }
}