//Main
import java.util.*;
public class bj17256 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		cake a = new cake(sc.nextInt(),sc.nextInt(),sc.nextInt());
		cake c = new cake(sc.nextInt(),sc.nextInt(),sc.nextInt());
		cake b = new cake(c.x-a.z,c.y/a.y,c.z-a.x);
		System.out.println(b.x+" "+b.y+" "+b.z);
		sc.close();
	}

	static class cake{
		int x;
		int y;
		int z;

		public cake(int x, int y, int z) {
			super();
			this.x = x;
			this.y = y;
			this.z = z;
		}
	}
}