/*
[input]
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
[output]
0
2
3
1
2
4
 */
import java.util.*;
import java.io.*;

public class Dijkstra {
    public static int v, e, start;
    public static int INF = (int)1e9;
    public static int[] distance;
    public static ArrayList<ArrayList<Node>> graph = new ArrayList<ArrayList<Node>>();

    static class Node implements Comparable<Node> {
        int node;
        int dist;

        public Node(int node, int dist) {
            this.node = node;
            this.dist = dist;
        }

        @Override
        public int compareTo(Node o) {
            return this.dist - o.dist;
        }
    }

    public static void dijkstra(int start) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(start, 0));
        distance[start] = 0;

        while(!pq.isEmpty()) {
            Node node = pq.poll();
            int dist = node.dist;
            int now = node.node;
            if (distance[now] < dist)
                continue;
            for(int i = 0; i < graph.get(now).size(); i++) {
                int cost = dist + graph.get(now).get(i).dist;
                if(cost < distance[graph.get(now).get(i).node]) {
                    distance[graph.get(now).get(i).node] = cost;
                    pq.offer(new Node(graph.get(now).get(i).node, cost));
                }
            }
        }
    }

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        v = Integer.parseInt(st.nextToken());
        e = Integer.parseInt(st.nextToken());
        start = Integer.parseInt(br.readLine());

        for(int i = 0; i < v + 1; i++) {
            graph.add(new ArrayList<>());
        }
        distance = new int[v + 1];
        for(int i = 0; i < v + 1; i++){
            distance[i] = INF;
        }

        for(int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            graph.get(a).add(new Node(b, c));
        }
        dijkstra(start);

        for(int i = 1; i < v + 1; i++) {
            if (distance[i] == INF)
                System.out.println("INFINITY");
            else
                System.out.println(distance[i]);
        }
    }
}
