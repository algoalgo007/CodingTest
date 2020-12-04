def check(ans):
    for i in range(len(ans)):
        x, y, a = ans[i]
        if a == 0: # 기둥인 경우
            if y == 0 or [x-1, y, 1] in ans or [x, y, 1] in ans or [x, y-1, 0] in ans:
                continue
            else:
                return False
        if a == 1: # 보 인경우
            if [x, y-1, 0] in ans or [x+1, y-1, 0] in ans or ([x-1, y, 1] in ans and [x+1, y, 1] in ans):
                continue
            else:
                return False
    return True
        
def solution(n, build_frame):
    ans = []
    for i in range(len(build_frame)):
        x, y, a, b = build_frame[i]
        if b == 0: #삭제인 경우
            ans.remove([x, y, a])
            if check(ans) == False:
                ans.append([x, y, a])
        elif b == 1: #설치인 경우
            ans.append([x, y, a]) 
            if check(ans) == False:
                ans.remove([x, y, a])
    return sorted(ans)
