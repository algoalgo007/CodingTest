# CodingTest

## 1. 그리디
 - 만들 수 없는 금액: ([Python 코드](/pystudy/Exercise/Greedy/Q04.py))
 
   - 동전 개수: 5, 동전의 종류 3, 2, 1, 1, 9 일때 target을 1로 지정, 동전의 종류 오름차순<br>
     target이 첫번째 원소 1보다 작지 않으므로 target += 첫번째 원소. target이 2가 됨. <br>
     target이 두번째 원소 1보다 작지 않으므로 target += 두번쨰 원소. target이 3이 됨. <br>
     target이 세번째 원소 2보다 작지 않으므로 target += 세번째 원소. target이 5가 됨. <br>
     target이 네번째 원소 3보다 작지 않으므로 target += 네번째 원소. target이 8이 됨. <br>
     target이 다섯번째 원소 9보다 작으므로 target 8을 반환함. 
     
## 2. 구현

## 3. DFS / BFS
 - 그래프
<img src = "pystudy/res/graph.PNG">

- DFS소스코드: ([Python 코드](/pystudy/개념/DFS.py))
  - 출력결과: 1, 2, 9, 3, 4, 7, 6, 8, 5

- BFS소스코드: ([Python 코드](/pystudy/개념/BFS.py))
  - 출력결과: 1, 2, 3, 7, 9, 6, 8, 4, 5

## 4. 정렬

## 5. 이진탐색

## 6. 다이나믹 프로그래밍
 - 가장 긴 증가하는 부분 수열: ([Python 코드](/pystudy/Exercise/다이나믹프로그래밍/Q34.py))
    - 백준 문제(18353번) : https://www.acmicpc.net/problem/18353
    
- 편집 거리 알고리즘: ([Python 코드](/pystudy/개념/편집거리.py))
  - 백준 문제(15483) : https://www.acmicpc.net/problem/15483
  - str1 = sunday, str2 = saturday로 가정 교체, 삽입, 삭제 3가지의 연산이 가능하다면 <br>
    두 문자가 같은 경우: 왼쪽 위에 해당하는 수를 그대로 대입. <br>
    두 문자가 다른 경우: 왼쪽(삽입), 위쪽(삭제), 왼쪽 위(교체)중 최소의 값에 1을 더해 대입. <br>
  <img src = "pystudy/res/Edt_Distance.PNG">
  

## 7. 최단경로
- 다익스트라 알고리즘: 한 점에서 다른 특정한 점까지의 최단 거리를 구할때 사용 ([Python 코드](/pystudy/개념/dijkstra.py))
  - 출력 결과(시작지점을 1로 설정한 결과) : 0 2 3 1 2 4
  <img src = "pystudy/res/dijkstra.PNG">
  
- 플로이드 와샬 알고리즘: 모든 점에서 다른 모든 점까지의 최단 거리를 구할때 사용 ([Python 코드](/pystudy/개념/floyd.py))
  - 출력 결과 [[0, 4, 8, 6], [3, 0, 7, 9], [5, 9, 0, 4], [7, 11, 2, 0]]
  <img src = "pystudy/res/floyd.PNG">
  
## 8. 그래프 

## 9. 기타 
- bisect를 이용한 이진탐색: ([Python 코드](/pystudy/개념/bisect.py))
