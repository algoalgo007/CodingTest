from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
  left_index = bisect_left(a, left_value)
  right_index = bisect_right(a, right_value)
  return right_index - left_index

n, x = map(int, input().split())
data = list(map(int, input().split()))

if count_by_range(data, x, x) == 0:
  print(-1)
else:
  print(count_by_range(data, x, x,))
