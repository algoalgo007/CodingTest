/*
[input]
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
[output]
159
 */
import java.util.*;
import java.io.*;

public class Kruskal {
    public static int v, e, ans = 0;
    public static int[] parent;
    public static ArrayList<Node> arr = new ArrayList<>();

    static class Node implements Comparable<Node> {
        int nodeA;
        int nodeB;
        int cost;

        public Node(int nodeA, int nodeB, int cost) {
            this.nodeA = nodeA;
            this.nodeB = nodeB;
            this.cost = cost;
        }

        @Override
        public int compareTo(Node o) {
            return this.cost - o.cost;
        }
    }

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

        for(int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());

            arr.add(new Node(a, b, cost));
        }

        Collections.sort(arr);

        for(int i = 0; i < arr.size(); i++) {
            Node node = arr.get(i);
            int a = node.nodeA;
            int b = node.nodeB;
            int cost = node.cost;

            if(findParent(parent, a) != findParent(parent, b)){
                ans += cost;
                unionParent(parent, a, b);
            }
        }

        System.out.println(ans);
    }
}
