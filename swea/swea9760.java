import java.util.*;
//swea9760
public class swea9760{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int t = sc.nextInt();

		for(int tc=1;tc<=t;tc++) {
			String tmp = sc.nextLine();
			Card[] cards = new Card[5];
			List<Integer> suitChk = new ArrayList<Integer>(4);//0 1 2 3 스페이스 다이아 하트 클로버
			List<Integer> numChk = new ArrayList<Integer>(13);//인덱스 1부터 사용함
			int cardSuit = 0;
			int cardNum = 0;
			String result = "";

			for(int i=0;i<5;i++) {
				tmp = sc.nextLine();
				switch(tmp.charAt(0)) {
				case 'S':{cardSuit=0; break;}
				case 'D':{cardSuit=1; break;}
				case 'H':{cardSuit=2; break;}
				case 'C':{cardSuit=3;}
				}
				switch(tmp.charAt(1)) {
				case 'T':{cardNum=10; break;}
				case 'J':{cardNum=11; break;}
				case 'Q':{cardNum=12; break;}
				case 'K':{cardNum=13; break;}
				case 'A':{cardNum=1; break;}
				default:{cardNum=tmp.charAt(1)-'0';}
				}

				cards[i] = new Card(cardSuit, cardNum);
				suitChk.set(cardSuit, suitChk.get(cardSuit)+1);
				numChk.set(cardNum, numChk.get(cardNum)+1);
			}
			
			//if()



			System.out.printf("#%d %d%n",tc,tc);
		}

		sc.close();
	}

}

class Card{
	int suit;
	int num;
	public Card(int suit, int num) {
		super();
		this.suit = suit;
		this.num = num;
	}
}