import heapq
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    q = []
    length = len(food_times)
    for i in range(length):
        heapq.heappush(q, (food_times[i], i+1))
    prev = 0
    while k:
        food = heapq.heappop(q)
        minus = length*(food[0]-prev)
        if k - minus <= 0:
            heapq.heappush(q, (food[0], food[1]))
            break
        length -= 1
        k -= minus
        prev = food[0]
    q.sort(key = lambda x: x[1])
    return q[(k) % length][1]
