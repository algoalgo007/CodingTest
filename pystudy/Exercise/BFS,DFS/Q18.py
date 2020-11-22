
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
def balanced(p):
    num_of_left = 0
    num_of_right = 0
    for i in range(len(p)):
        if p[i] == '(':
            num_of_left += 1
        elif p[i] == ')':
            num_of_right += 1
        if num_of_left == num_of_right:
            return i

def correct(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        elif p[i] == ')':
            count -= 1
            if count < 0:
                return False
    if count != 0:
        return False
    else:
        return True

def solution(p):
    if p == '': # 빈 문자열이면 그냥 return
        return p
    answer = ""
    index = balanced(p)
    u = p[:index+1]
    v = p[index+1:]
    if correct(u) == True:
        answer = u + solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            elif u[i] == ')':
                u[i] = '('
        answer += "".join(u)
    return answer
