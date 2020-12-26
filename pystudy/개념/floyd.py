INF = int(1e9)
 
n = 4
m = 7
graph = [[INF] * (1+n) for _ in range(1+n)]
 
for i in range(1, 1 + n):
  for j in range(1, 1 + n):
    if i == j:
      graph[i][j] = 0
 
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a][b] = c
 
for k in range(1, 1 + n):
  for a in range(1, 1 + n):
    for b in range(1, 1 + n):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
 
for i in range(1, 1 + n):
  for j in range(1, 1 + n):
    if graph[a][b] == INF:
      print("INF", end=" ") 
    else:
      print(graph[i][j], end=" ")
  print()
