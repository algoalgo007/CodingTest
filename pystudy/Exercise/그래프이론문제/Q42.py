def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

n = int(input())
m = int(input())
parent = [0] * (1 + n)

for i in range(1, 1+n):
  parent[i] = i

result = 0
for _ in range(m):
  data = find_parent(parent, int(input()))
  if data == 0:
    break
  union_parent(parent, data, data-1)
  result += 1
print(result)
