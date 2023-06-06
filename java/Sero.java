/*
[input]
6 4
1 4
2 3
2 4
5 6
[output]
각 원소가 속한 집합: 1 1 1 1 5 5
부모 테이블: 1 1 1 1 5 5
 */
import java.util.*;
import java.io.*;

public class Sero {
    public static int v, e;
    public static int[] parent;

    public static int findParent(int[] parent, int x) {
        if(parent[x] != x) {
            parent[x] =
                    findParent(parent, parent[x]);
        }
        return parent[x];
    }

    public static void unionParent(int[] parent, int a, int b) {
        a = findParent(parent, a);
        b = findParent(parent, b);
        if (a < b)
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

        for(int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            unionParent(parent, a, b);
        }

        System.out.print("각 원소가 속한 집합: ");
        for(int i = 1; i < v + 1; i++) {
            System.out.print(findParent(parent, i) + " ");
        }
        System.out.println();

        System.out.print("부모 테이블: ");
        for(int i = 1; i < v + 1; i++) {
            System.out.print(parent[i] + " ");
        }
    }
}
