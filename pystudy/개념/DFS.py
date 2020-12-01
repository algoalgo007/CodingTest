def dfs(graph, visited, start):
  visited[start] = True
  print(start, end=" ")
  for i in graph[start]: # start와 연결이 되어 있는 노드 탐색 중
    if not visited[i]: # 방문하지 않은 노드가 있다면
      dfs(graph, visited, i) # 재귀적으로 호출
    
graph = [
  [],
  [2, 3, 7],
  [1, 9],
  [1, 9],
  [9],
  [8],
  [7],
  [1, 6, 8],
  [5, 7],
  [2, 3, 4]
]

visited = [False] * 10
dfs(graph, visited, 1)
