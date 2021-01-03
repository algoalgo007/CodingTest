data = input()
data += "2"
length = len(data)
num_of_zero = 0
num_of_one = 0

for i in range(length-1):
  num1 = int(data[i])
  num2 = int(data[i+1])
  if num1 == 0 and num2 != 0:
    num_of_zero +=1
  if num1 == 1 and num2 != 1:
    num_of_one +=1

print(min(num_of_zero, num_of_one))
