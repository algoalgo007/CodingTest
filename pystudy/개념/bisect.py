from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
  left_index = bisect_left(array, left_value)
  right_index = bisect_right(array, right_value)
  result = right_index - left_index
  return result

array = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print(count_by_range(array, 3, 4))
