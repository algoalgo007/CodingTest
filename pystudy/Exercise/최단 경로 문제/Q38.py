INF = int(1e9)
cost = 1

n, m = map(int, input().split())
graph = [[INF] * (1+n) for _ in range(1+n)]

for i in range(1, 1+n):
  for j in range(1, 1+n):
    if i == j:
      graph[i][j] = 0
    
for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = cost
  

for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0
for i in range(1, n+1):
  count = 0
  for j in range(1, n+1):
    if graph[i][j] != INF or graph[j][i] != INF:
      count += 1
  if count == n:
    result += 1

print(result)
