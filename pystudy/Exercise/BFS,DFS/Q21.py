from collections import deque
N, L, R = map(int, input().split())
graph = []
for i in range(N):
  graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  q = deque()  
  q.append((x, y))
  cnt = 1
  visited[x][y] = 1
  sum = graph[x][y]
  arr = [(x, y)]
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= N or ny >= N:
        continue
      if L <= abs(graph[nx][ny] - graph[x][y]) <= R and visited[nx][ny] == 0:
        q.append((nx, ny))
        cnt += 1
        sum += graph[nx][ny]
        visited[nx][ny] = 1 
        arr.append((nx, ny))

  if cnt >= 2:
    for a, b in arr:
      graph[a][b] = sum // cnt
    return True
  else:
    return False

count = 0
while True:
  check = False
  visited = [[0]*N for _ in range(N)]
  count += 1
  for i in range(N):
    for j in range(N):
      if visited[i][j] == 0:
        if bfs(i, j) == True:
          check = True
  if check == False:
    break

print(count-1)
