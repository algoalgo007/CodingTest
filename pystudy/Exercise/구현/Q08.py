data = input()
al = []
num = []

for i in range(len(data)):
  if data[i].isalpha():
    al.append(data[i])
  else:
    num.append(int(data[i]))

al.sort()

if sum(num) != 0:
  al.append(str(sum(num)))
  
print(''.join(al))
