from collections import deque

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (1 + N)
answer = []
for i in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)

def bfs(start, visited, graph):
  queue = deque([start])
  visited[start] = True
  count = 1
  while queue:
    for _ in range(len(queue)):
      v = queue.popleft()
      for i in graph[v]:
        if not visited[i] and count == K:
          answer.append(i)
        if not visited[i]:
          visited[i] = True
          queue.append(i)
    count += 1
    
    
bfs(X, visited, graph)
answer.sort()

if len(answer) != 0:
  for data in answer:
    print(data)
else:
  print(-1)
