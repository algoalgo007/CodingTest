import copy

graph = [[0] * 4 for _ in range(4)]
for i in range(4):
  data = list(map(int, input().split()))
  for j in range(4):
    graph[i][j] = [data[j*2],data[j*2+1]-1]
result = 0

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def turn_left(direction):
  return (direction + 1) % 8

def find_fish(graph, index):
  for i in range(4):
    for j in range(4):
      if graph[i][j][0] == index:
        return (i, j)
  return None

def move_all_fishes(graph, now_x, now_y):
  for i in range(1, 17):
    position = find_fish(graph, i)
    if position != None:
      x, y = position[0], position[1]
      dir = graph[x][y][1]
      for i in range(8):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx < 4 and 0 <= ny < 4:
          if not (nx == now_x and ny == now_y):
            graph[x][y][1] = dir
            graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
            break
        dir = turn_left(dir)

def get_possible_positions(graph, now_x, now_y):
  positions = []
  dir = graph[now_x][now_y][1]
  for i in range(4):
    now_x += dx[dir]
    now_y += dy[dir]
    if 0 <= now_x < 4 and 0 <= now_y < 4:
      if graph[now_x][now_y][0] != -1:
        positions.append((now_x, now_y))
  return positions

def dfs(graph, now_x, now_y, total):
  global result
  graph = copy.deepcopy(graph)

  total += graph[now_x][now_y][0]
  graph[now_x][now_y][0] = -1

  move_all_fishes(graph, now_x, now_y)

  positions = get_possible_positions(graph, now_x, now_y)

  if len(positions) == 0:
    result = max(result, total)
    return
  
  for next_x, next_y in positions:
    dfs(graph, next_x, next_y, total)

dfs(graph, 0, 0, 0)
