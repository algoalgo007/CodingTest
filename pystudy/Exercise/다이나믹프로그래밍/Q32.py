n = int(input())
array = [[0] * n for _ in range(n)]
for i in range(n):
  input_data = list(map(int, input().split()))
  for j in range(len(input_data)):
    array[i][j] = input_data[j]

for i in range(1, n):
  for j in range(n):
    if j == 0:
      array[i][j] += array[i-1][j]
    else:
      array[i][j] += max(array[i-1][j-1], array[i-1][j])

answer = 0
for i in range(n):
  answer = max(answer, array[n-1][i])
print(answer)        
