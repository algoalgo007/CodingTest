n = int(input())
graph = [[0] * n for _ in range(n)]
x = 0
y = -1
idx = 1
a = n
num = 1
while num <= n * n:
  for _ in range(a):
    y += idx
    graph[x][y] = num
    num += 1
  a -= 1
  for _ in range(a):
    x += idx
    graph[x][y] = num
    num += 1
  idx *= -1

for i in range(n):
  for j in range(n):
    print(graph[i][j], end=" ")
  print()
