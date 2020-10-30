data = input()
result = 0

for i in range(0, len(data)):
  a = int(data[i])
  if a  == 0:
    result += a
  elif a == 1 or result == 0:
    result += a
  else:
    result *= a
    
print(result)
