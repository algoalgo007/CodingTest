t = int(input())
for i in range(t):
  n, m = map(int, input().split())
  array = []
  input_data = list(map(int, input().split()))
  for i in range(n):
    array.append(input_data[i*m:(i+1)*m])
  
  for i in range(1, m):
    for j in range(n):
      if j == 0:
        array[j][i] += max(array[j][i-1], array[j+1][i-1]) 
      elif j == n-1:
        array[j][i] += max(array[j-1][i-1], array[j][i-1])
      else:
        array[j][i] += max(array[j-1][i-1], array[j][i-1], array[j+1][i-1])
  print(array)
