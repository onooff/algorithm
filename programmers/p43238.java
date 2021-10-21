import java.util.*;

class Solution {
    public long solution(int n, int[] times) {
        Arrays.sort(times);
        long low = 0;
        long high = (long)times[times.length-1]*(long)n;
        long mid = 0;
        long chk = 0;
        long answer = 0;
        while(low<=high){
            mid = (low+high)/2;
            // System.out.println(mid);
            chk = 0;
            for(int i=0;i<times.length;i++) chk+=mid/times[i];
            if(chk>=n){
                high = mid-1;
                answer = mid;
            }else low = mid+1;
        }
        return answer;
    }
}