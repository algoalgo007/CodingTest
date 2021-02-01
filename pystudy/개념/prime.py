import math

def is_prime_number(x):
  for i in range(2, int(math.sqrt(x)) + 1): # 제곱근까지만 확인하면 
    if i % 2 == 0:
      return False
  return True

print(is_prime_number(10))
print(is_prime_number(3))
