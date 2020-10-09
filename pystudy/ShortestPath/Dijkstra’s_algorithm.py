import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
N, M = map(int, input().split())
graph = [[] for _ in range(1 + N)]
distance = [INF] * (1 + N)
start = int(input())

for i in range(M):
  a, b, c = map(int, input().split()) 
  graph[a].append((b, c))

def dijkstra(start):
  q = []
  distance[start] = 0
  heapq.heappush(q, (0, start))
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, N + 1):
  if distance[i] == INF:
    print("INFINITY")
  else:
    print(distance[i])
