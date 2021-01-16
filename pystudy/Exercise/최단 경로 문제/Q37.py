INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF] * (1+n) for _ in range(1+n)]

for _ in range(m):
  a, b, c = map(int, input().split()) 
  if c < graph[a][b]: # 시작 도시와 도착 도시를 연결하는 노선이 하나가 아닐 수 있으므로 최소의 값만 
    graph[a][b] = c

for i in range(1, 1+n):
  for j in range(1, 1+n):
    if i == j:
      graph[i][j] = 0

for k in range(1, 1+n):
  for a in range(1, 1+n):
    for b in range(1, 1+n):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, 1+n):
  for j in range(1, 1+n):
    if graph[i][j] == INF:
      print(0, end=" ")
    else:
      print(graph[i][j], end=" ")
  print()
