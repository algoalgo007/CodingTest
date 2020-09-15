N = int(input()) # 학생의 수 입력 받음
data = []

for i in range(N):
  name, score = input().split()
  data.append((name, score))

data.sort(key = lambda x : x[1])

for i in range(N):
  print(data[i][0], end=" ")
