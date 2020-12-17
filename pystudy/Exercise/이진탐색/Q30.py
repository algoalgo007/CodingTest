from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    left_index = bisect_left(a, left_value)
    right_index = bisect_right(a, right_value)
    return right_index - left_index

def solution(words, queries):
    answer = []
    array = [[] for _ in range(10001)]
    reverse_array = [[] for _ in range(10001)]
    
    for word in words:
        array[len(word)].append(word)
        reverse_array[len(word)].append(word[::-1])
        
    for i in range(10001):
        array[i].sort()
        reverse_array[i].sort()
        
    for i in queries:
        if i[0] != "?":
            ans = count_by_range(array[len(i)], i.replace('?', 'a'), i.replace('?','z'))
        else:
            ans = count_by_range(reverse_array[len(i)], i[::-1].replace('?','a'), i[::-1].replace('?','z'))
        answer.append(ans)
    return answer
