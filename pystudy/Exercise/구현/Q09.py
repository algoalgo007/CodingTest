https://programmers.co.kr/learn/courses/30/lessons/60057
def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2+1):
        prev = s[0:0+i]
        count = 1
        ans = ""
        for j in range(i,len(s)+i,i):
            now = s[j:j+i]
            if now == prev:
                count += 1
            else:
                if count != 1:
                    ans += (str(count)+prev)
                else:
                    ans += prev
                count = 1
            prev = now
        answer = min(answer, len(ans))
    return answer

s = 'aabbaccc'
