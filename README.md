# CodingTestStudy - FreeDeveloper
## 나동빈 - 이것이 코딩테스트이다 : 문제풀이 코드저장소

### 자주쓰이는 파이썬 코드
* 빠른 입력 코드
```python
import sys
input = sys.stdin.readline
#이후에 input()으로 사용
#입력 후 한줄개행의 경우 .rstrip() 사용
```
* 시간측정코드
```python
import time
start_time = time.time()
end_time = time.time()
print(end_time - start_time)
```
* 이중탐색코드
```python
def binary_search(array, target, start, end) :
  if start > end :
    return None

  mid = (start+end)//2

  if target == array[mid] :
    return mid
  elif target < array[mid] :
    return binary_search(array, target, start, mid-1)
  else :
    return binary_search(array, target, mid+1, end)
```
* 다익스트라
```python
import heapq
import sys
INF = int(1e9)
input = sys.stdin.readline

#노드의 개수, 간선의 개수
n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

#간선 입력
for _ in range(m) :
  a, b, c = map(int, input().split()) #a->b 간선의 비용 : c
  graph[a].append((b, c))

def dijkstra(start) :
  #큐를 설정하여 시작점을 큐에 넣는다
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  #큐가 빌때까지 반복하여 실시한다
  while q :
    #최단거리, 해당 노드를 가져온다
    dist, now = heapq.heappop(q)

    #이미 처리된 값인 경우 무시한다
    if distance[now] < dist :
      continue
    
    #인접한 노드 개수만큼 반복한다
    for i in graph[now] :
      cost = dist + i[1] #i[0] : 노드값, i[1] : 간선비용

      #갱신값이 작은경우 갱신한다
      if cost < distance[i[0]] :
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1) :
  if distance[i] == INF :
    print("INFINITY")
  else :
    print(distance[i])
```
* 플로이드 워셜
```python
INF = int(1e9)
#노드수, 간선수
n = int(input())
m = int(input())

#무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

#시작 = 종료 간선값을 0으로 저장
for a in range(1, n+1) :
  for b in range(1, n+1) :
    if a == b :
      graph[a][b] = 0

#a->b : 간선 c
for _ in range(m) :
  a, b, c = map(int, input().split())
  graph[a][b] = c

#현재값과 현재를 거치는 모든경우를 계산하여 최소값으로 갱신한다
for k in range(1, n+1) :
  for a in range(1, n+1) :
    for b in range(1, n+1) :
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

#N*N 전체 경우를 출력한다
for a in range(1, n+1) :
  for b in range(1, n+1) :
    if graph[a][b] == INF :
      print("INFINITY", end=" ")
    else :
      print(graph[a][b], end=" ")
  print()
```


### 책내용 정리 블로그
[Tistory - 자유로운 개발자 FDEE](https://fdee.tistory.com/category/나동빈%20코딩테스트%20정리)
    
### codeup 기초문법 100제 사이트
[codeup 기초문법 100제](https://codeup.kr/problemsetsol.php?psid=23)

### 파이썬 기초문법 정리
[파이썬 기초문법 정리](https://fdee.tistory.com/entry/Phython-파이썬-기초문법-정리-codeup-기초-100제)

## Chapter3 그리디 정리
[그리디 정리](https://fdee.tistory.com/entry/Chapter3-그리디-정리)

## Chapter4 구현 정리
[구현 정리](https://fdee.tistory.com/entry/이것이-코딩-테스트다-Chapter4-구현-정리)

## Chapter5 DFS, BFS 정리
[DFS, BFS 정리](https://fdee.tistory.com/entry/이것이-코딩-테스트다-Chapter5-DFS-BFS-정리)

## Chapter6 정렬 정리
[정렬 정리](https://fdee.tistory.com/entry/이것이-코딩-테스트다-Chapter6-정렬-정리)

## Chapter7 이진 탐색 정리
[이진 탐색 정리](https://fdee.tistory.com/entry/이것이-코딩-테스트다-Chapter7-이진-탐색)

## Chapter8 다이나믹 프로그래밍 정리
[DP 정리](https://fdee.tistory.com/entry/이것이-코딩-테스트다-Chapter8-다이나믹-프로그래밍-정리)
