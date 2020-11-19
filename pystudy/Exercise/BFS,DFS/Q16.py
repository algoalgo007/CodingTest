from itertools import combinations
from collections import deque
import copy

N, M = map(int, input().split())
graph = []
virus = []
blank = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(N):
  graph.append(list(map(int, input().split())))
  for j in range(M):
    if graph[i][j] == 2:
      virus.append((i, j))
    elif graph[i][j] == 0:
      blank.append((i, j))

def bfs():
  queue = deque(virus)
  testgraph = copy.deepcopy(graph)
  count = 0

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
      if testgraph[nx][ny] == 0:
        testgraph[nx][ny] = 2
        queue.append((nx, ny))

  for i in range(N):
    for j in range(M):
      if testgraph[i][j] == 0:
        count += 1

  return count

maximum = 0
for data in combinations(blank, 3):
  for x, y in data:
    graph[x][y] = 1
  maximum = max(maximum, bfs())
  for x, y in data:
    graph[x][y] = 0

print(maximum)
