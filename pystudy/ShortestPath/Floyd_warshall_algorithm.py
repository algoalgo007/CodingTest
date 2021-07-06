INF = int(1e9)
N = int(input())
M = int(input())

# 2차원 리스트 만들기 모든 값 무한으로 초기화
graph = [[INF] * (1 + N) for _  in range(1 + N)]

# 자기 자신에게 가는 경우 거리를 0 으로 초기화
for i in range(1, 1 + N):
  for j in range(1, 1 + N):
    if i == j:
      graph[i][j] = 0

for _ in range(M):
  a, b, c = map(int, input().split())
  graph[a][b] = c

for k in range(1, 1 + N):
  for a in range(1, 1 + N):
    for b in range(1, 1 + N):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, 1 + N):
  for j in range(1, 1+ N):
    if graph[i][j] == INF:
      print("INFINITY", end=" ")
    else:
      print(graph[i][j], end=" ")
  print()

'''
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4 
4 3 2
'''
