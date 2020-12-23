import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(1+n)]
distance = [INF] * (1 + n)

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append((b, 1))
  graph[b].append((a, 1))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))
  
dijkstra(1)
answer = []
for i in range(1, n+1):
  answer.append((i, distance[i]))

answer.sort(key = lambda x: x[1], reverse = True)
  
ans1 = []
for i in range(len(answer)-1):
  if answer[i][1] != answer[i+1][1]:
    ans1.append(answer[i][0])
    break
  else:
    ans1.append(answer[i][0])
ans1.sort()

print(ans1[0], end=" ")
print(answer[0][1], end=" ")
print(len(ans1))  
