import java.util.*;

class Solution {
    public static int[] solution(String[] operations) {
		PriorityQueue<Integer> minQ = new PriorityQueue<Integer>();
		PriorityQueue<Integer> maxQ = new PriorityQueue<>((Integer o1, Integer o2) -> (-Integer.compare(o1,o2)));
		Map<Integer, int[]> map = new HashMap<>(); 

        String[] tmp;
        char c;
        int n;
        PriorityQueue<Integer> where;
        for(String o : operations){
            tmp = o.split(" ");
            c = tmp[0].charAt(0);
            n = Integer.parseInt(tmp[1]);
            switch(c){
                case 'I':
                    minQ.offer(n);
                    maxQ.offer(n);
                    map.putIfAbsent(n,new int[1]);
                    map.get(n)[0]+=1;
                    break;
                case 'D':
                    if(n==1) where = maxQ;
                    else where = minQ;
                    while(!where.isEmpty() && map.get(where.peek())[0]==0) where.poll();
                    if(where.isEmpty()) break;
                    n = where.poll();
                    map.get(n)[0]--;
                    break;
            }
        }
        int[] answer = {0,0};
        while(!minQ.isEmpty() && map.get(minQ.peek())[0]==0) minQ.poll();
        while(!maxQ.isEmpty() && map.get(maxQ.peek())[0]==0) maxQ.poll();
        if(!minQ.isEmpty() && !maxQ.isEmpty()){
            answer[0]=maxQ.peek();
            answer[1]=minQ.peek();
        }
        return answer;
    }
}