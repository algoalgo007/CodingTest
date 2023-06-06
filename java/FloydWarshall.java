/*
[input]
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
[output]
0 4 8 6
3 0 7 9
5 9 0 4
7 11 2 0
 */
import java.util.*;
import java.io.*;

public class FloydWarshall {
    public static int n, m;
    public static int INF = (int) 1e9;
    public static int[][] graph;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());

        graph = new int[n + 1][n + 1];
        for(int i = 0; i < n + 1; i++) {
            for(int j = 0; j < n + 1; j++) {
                graph[i][j] = INF;
            }
        }
        for(int i = 1; i < n + 1; i++) {
            for(int j = 1; j < n + 1; j++) {
                if(i == j)
                    graph[i][j] = 0;
            }
        }
        for(int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            graph[a][b] = c;
        }

        for(int k = 1; k < n + 1; k++) {
            for(int a = 1; a < n + 1; a++) {
                for(int b = 1; b < n + 1; b++) {
                    graph[a][b] = Math.min(graph[a][b], graph[a][k] + graph[k][b]);
                }
            }
        }

        for(int a = 1; a < n + 1; a++) {
            for(int b = 1; b < n + 1; b++) {
                System.out.print(graph[a][b] + " ");
            }
            System.out.println();
        }
    }
}
