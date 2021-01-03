n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))
result = []

for i in range(n):
  result.append(min(graph[i]))

print(max(result))
