/*
[INPUT]
3 3
1 2
1 3
2 3
[OUTPUT]
사이클이 발생했습니다.
 */
import java.util.*;
import java.io.*;

public class Cycle {
    public static int v, e;
    public static int[] parent;

    public static int findParent(int[] parent, int x) {
        if(parent[x] != x) {
            parent[x] = findParent(parent, parent[x]);
        }
        return parent[x];
    }

    public static void unionParent(int[] parent, int a, int b) {
        a = findParent(parent, a);
        b = findParent(parent, b);
        if(a < b)
            parent[b] = a;
        else
            parent[a] = b;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        v = Integer.parseInt(st.nextToken());
        e = Integer.parseInt(st.nextToken());

        parent = new int[v + 1];
        for(int i = 1; i < v + 1; i++) {
            parent[i] = i;
        }

        boolean cycle = false;

        for(int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            if(findParent(parent, a) != findParent(parent, b))
                unionParent(parent, a, b);
            else {
                cycle = true;
                break;
            }
        }

        if(cycle) {
            System.out.println("사이클이 발생했습니다");
        } else{
            System.out.println("사이클이 발생하지 않았습니다");
        }
    }
}
