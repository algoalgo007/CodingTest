from itertools import permutations

N = int(input())
data = list(map(int, input().split()))
a, b, c, d = map(int, input().split())
check = []

while True:
  if a > 0:
    check.append('+')
    a -= 1
  elif b > 0:
    check.append('-')
    b -= 1
  elif c > 0:
    check.append('*')
    c -= 1
  elif d > 0:
    check.append('//')
    d -= 1
  if a <= 0 and b <= 0 and c <= 0 and d <= 0:
    break

result = list(permutations(check, N-1))

def solve(now):
  for i in range(N-1):
    arr.append(str(data[i]))
    arr.append(result[now][i])
  arr.append(str(data[-1])) 
  
def calcul(arr):
  prev = 0
  i = 0
  while True:
    if i > len(arr)-1:
      break
    if arr[i].isdigit():
      prev = int(arr[i])
      i += 1
    else:
      if arr[i] == "+":
        prev = (prev + int(arr[i+1]))
      elif arr[i] == "-":
        prev = (prev - int(arr[i+1]))
      elif arr[i] == '*':
        prev = (prev * int(arr[i+1]))
      else:
        if prev > 0:
            prev = (prev // int(arr[i+1]))
        else:
            prev = (((prev*-1) // int(arr[i+1]))*-1)
      i += 2
  return prev
maxvalue = int(1e9)*-1
minvalue = int(1e9)
for i in range(len(result)):
  arr = []
  solve(i)
  ans = int(calcul(arr))
  maxvalue = max(maxvalue, ans)
  minvalue = min(minvalue, ans)

print(maxvalue)
print(minvalue)
