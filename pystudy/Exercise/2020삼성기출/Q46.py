from collections import deque
n = int(input())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
size = 2
for i in range(n):
  graph.append(list(map(int, input().split())))
  for j in range(n):
    if graph[i][j] == 9:
      xPos, yPos = i, j
      graph[i][j] = 0
    
def bfs(xPos, yPos):
  q = deque()
  q.append((xPos, yPos))
  visited[xPos][yPos] = 0
  while q:
    for _ in range(len(q)):
      x, y = q.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1 and graph[nx][ny] <= size:
          if graph[nx][ny] <= size:
              visited[nx][ny] = visited[x][y] + 1
              q.append((nx, ny))
          if 0 < graph[nx][ny] < size:
            eat.append((visited[nx][ny], nx, ny))

cnt = 0
def fish(eat):
  eat.sort()
  global cnt, size
  global xPos, yPos
  global count
  e = eat.pop(0)
  dist, x, y = e
  graph[x][y] = 0
  cnt += 1
  count += dist
  xPos, yPos = x, y
  if cnt >= size:
    size += 1
    cnt = 0

count = 0
while True:
  visited = [[-1] * n for _ in range(n)]
  eat = []
  bfs(xPos, yPos)
  if len(eat) == 0:
    print(count)
    break
  fish(eat)
  
