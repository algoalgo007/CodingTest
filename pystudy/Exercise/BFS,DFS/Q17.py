from collections import deque

N, K = map(int, input().split())
graph = []
virus = []
for i in range(N):
  graph.append(list(map(int, input().split())))
  for j in range(N):
    if graph[i][j] != 0:
      virus.append((graph[i][j], i, j))
S, X, Y = map(int, input().split())

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, S, virus):
  queue = deque(virus)
  count = 0
  while queue:
    if count == S:
      break
    for _ in range(len(queue)):
      type, x, y = queue.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
          continue
        if graph[nx][ny] == 0:
          graph[nx][ny] = graph[x][y]
          queue.append((graph[nx][ny], nx, ny))
    count += 1

virus.sort()
bfs(graph, S, virus)
print(graph[X-1][Y-1])
