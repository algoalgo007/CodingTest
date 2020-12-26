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

v, e = map(int, input().split())
parent = [0] * (1+v)

for i in range(1, v+1):
  parent[i] = i

for i in range(v):
  data = list(map(int, input().split()))
  for j in range(v):
    if data[j] == 1:
      union_parent(parent, i+1, j+1) 

route = list(map(int, input().split()))

result = True

for i in range(e-1):
  if find_parent(parent, route[i]) != find_parent(parent, route[i+1]):
    result = False
    break

if result:
  print("YES")
else:
  print("NO")
