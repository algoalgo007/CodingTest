def binary_search(array, start, end):
  while start <= end:
    mid = (start + end) // 2
    target = mid
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return None

n = int(input())
data = list(map(int, input().split()))
result = binary_search(data, 0, n-1)
if result == None:
  print(-1)
else:
  print(result)
