N = int(input())
data = list(map(int, input().split()))
data.sort()

count = 0
count2 = 0
for i in range(N):
  count += 1
  if data[i] <= count:
    count2 += 1
    count = 0

print(count2)
