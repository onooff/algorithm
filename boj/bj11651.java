import java.util.*;
public class bj11651{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		v[] arr = new v[n];

		for(int i=0;i<n;i++) {
			arr[i] = new v(sc.nextInt(),sc.nextInt());
		}

		Arrays.sort(arr, new Comparator<v>() {
			public int compare(v o1, v o2) {
				return Integer.compare(o1.x, o2.x);
			}
		});
		Arrays.sort(arr, new Comparator<v>() {
			public int compare(v o1, v o2) {
				return Integer.compare(o1.y, o2.y);
			}
		});
		
		for(int i=0;i<n;i++) {
			System.out.println(arr[i].x+" "+arr[i].y);
		}
		
		sc.close();
	}

	static class v{
		int x;
		int y;
		public v(int x, int y) {
			super();
			this.x = x;
			this.y = y;
		}
	}
}