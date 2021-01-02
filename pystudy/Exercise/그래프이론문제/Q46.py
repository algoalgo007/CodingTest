# DFS or BFS 방식
# 처음 상어의 크기는 2 위치 9
# 상하좌우로 탐색 -> dx, dy 리스트 생성
# 상어와 크기가 같은 물고기가 있는 칸 까지는 이동가능
# 상어보다 크기가 작은 물고기는 먹을 수 있음
# 거리순, 거리가 가까운 물고기가 많다면 가장 위, 왼쪽 순으로 섭취
# 자신의 크기와 같은 수의 물고기 먹으면 크기 증가 -> 계속적으로 먹은 수 확인
# 몇 초 동안? -> cnt 생각 가능

from collections import deque

n = int(input())
graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))
  for j in range(n):
    if graph[i][j] == 9: #상어의 위치 찾음
      now_x = i
      now_y = j

now_size = 2
graph[now_x][now_y] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
  q = deque()
  q.append((now_x, now_y))
  dist = [[-1] * n for _ in range(n)]
  dist[now_x][now_y] = 0
  
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n:
        if dist[nx][ny] == -1 and graph[nx][ny] <= now_size:
          dist[nx][ny] = dist[x][y] + 1
          q.append((nx, ny))
  return dist

def eat(dist):
  mini = int(1e9)
  for i in range(n):
    for j in range(n):
      if dist[i][j] != -1 and 1 <= graph[i][j] < now_size:
        if dist[i][j] < mini:
          mini = dist[i][j]
          a = i; b = j
  if mini != int(1e9):
    return a, b, mini
  return None

ans = 0
count = 0

while True:
  res = eat(bfs())
  if res == None:
    print(ans)
    break
  now_x = res[0]; now_y = res[1]
  ans += res[2]
  count += 1
  graph[now_x][now_y] = 0
  if count >= now_size:
    now_size += 1
    count = 0
