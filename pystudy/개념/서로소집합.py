def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x]) # 경로 압축기법 적용
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent ,b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

v, e = map(int, input().split())
parent = [0] * (1 + v)

for i in range(1, 1 + v):
  parent[i] = i
  
for i in range(e):
  a, b = map(int, input().split())
  union_parent(parent, a, b)

print("각 원소가 속한 집합: ")
for i in range(1, 1 + v):
  print(find_parent(parent, i), end=" ")
print()

print("부모 테이블")
for i in range(1, 1 + v):
  print(parent[i], end=" ")
