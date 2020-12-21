import math
N = int(input())
n = 20
array = [True] * (n + 1)

# 소수인걸 구함 
for i in range(2, int(math.sqrt(n))+ 1):
  if array[i] == True:
    j = 2
    while i * j <= n:
      array[i * j] = False
      j += 1

array[1] = False
array[2] = False
array[3] =  False
array[5] = False

for i in range(2, n+1):
  if array[i] == True:
    j = 1
    while i * j <= n:
      array[i * j] = True
      j +=1 

ans = []
for i in range(1, n+1):
  if array[i] == False:
    ans.append(i)

print(ans[N-1])
