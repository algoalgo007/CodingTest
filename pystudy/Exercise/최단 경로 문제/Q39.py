import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

T = int(input())
for i in range(T):
  N = int(input())
  graph = []
  visited = [[0] * (N) for _ in range(N)]
  # 상 하 좌 우
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  for _ in range(N):
    graph.append(list(map(int, input().split())))

  distance = [[INF]*N for _ in range(N)]

  def dijkstra(xPos, yPos):
    q = []
    heapq.heappush(q, (graph[xPos][yPos], xPos, yPos))
    distance[xPos][yPos] = graph[xPos][yPos]
    while q:
      dist, x, y = heapq.heappop(q)
      if distance[x][y] < dist:
        continue
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
          continue
        cost = graph[nx][ny] + dist
        if cost < distance[nx][ny]:
          distance[nx][ny] = cost
          heapq.heappush(q, (cost, nx, ny))

  dijkstra(0, 0)
  print(distance[N-1][N-1])
  




