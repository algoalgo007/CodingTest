/*
[intput]
6
1 2
1 2
2 3
1 3
1 2
2 3
[output]
1 2
2 3
1 3
 */
import java.util.*;
import java.io.*;

public class CheckDuplicateValByEquals {
    public static int n;
    public static HashSet<Pos> set = new HashSet<>();

    static class Pos {
        int x;
        int y;

        public Pos(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object o) {
            if(this.x == ((Pos)o).x && this.y == ((Pos)o).y)
                return true;
            else
                return false;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());

        for(int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            set.add(new Pos(x, y));
        }

        for(Pos p : set) {
            System.out.println(p.x + " " + p.y);
        }
    }
}
