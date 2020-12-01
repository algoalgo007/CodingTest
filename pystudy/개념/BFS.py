from collections import deque # deque라이브러리 사용하기 위함

def bfs(graph, visited, start):
  queue = deque([start])
  visited[start] = True # 시작노드 방문처리 
  while queue:
    v = queue.popleft() # popleft로 왼쪽에서 pop함 큐와 같은 구현 위함 
    print(v, end = " ")
    for i in graph[v]: # v와 연결되어있는 노드 중
      if not visited[i]: # 방문하지 않은 노드가 있다면 
        visited[i] = True # 방문처리 
        queue.append(i) # deque에 append 해줌

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
bfs(graph, visited, 1)
