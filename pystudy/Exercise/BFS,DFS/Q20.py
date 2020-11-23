from itertools import combinations
from collections import deque
import copy

N = int(input())
graph = []
teacher = []
blank = []

for i in range(N):
  graph.append(list(input().split())) 
  for j in range(N):
    if graph[i][j] == 'T':
      teacher.append((i, j))
    elif graph[i][j] == 'X':
      blank.append((i, j))

def dir(x, y, dir): # 학생 찾은 경우 True 반환 못찾은경우 False반환
  if dir == 0: # 상
    while x >= 1:
      x -= 1
      if graph[x][y] == 'S':
        return True
      elif graph[x][y] == 'O':
        return False
  elif dir == 1: # 하
    while x < N-1:
      x += 1
      if graph[x][y] == 'S':
        return True
      elif graph[x][y] == 'O':
        return False
  elif dir == 2: # 좌
    while y >= 1:
      y -= 1
      if graph[x][y] == 'S':
        return True
      elif graph[x][y] == 'O':
        return False
  elif dir == 3: # 우
    while y < N-1:
      y += 1
      if graph[x][y] == 'S':
        return True
      elif graph[x][y] == 'O':
        return False
  return False

def process():
  for x, y in teacher:
    for i in range(4):
      if dir(x, y, i):
        return True # 학생 찾은 경우
  return False # 학생 못 찾은 경우

check = False
for data in combinations(blank, 3):
  for x, y, in data:
    graph[x][y] = 'O'
  if process() == False:
    check = True # 못찾은 경우
    break
  for x, y, in data:
    graph[x][y] = 'X'
    

if check:
  print("YES")
else:
  print("NO")
