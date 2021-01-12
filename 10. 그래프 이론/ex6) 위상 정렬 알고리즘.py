#ex6) 위상 정렬 알고리즘, 296p

from collections import deque

#노드, 간선수 입력
v, e = map(int, input().split())
#입력간선값 리스트 0으로 초기화
indegree = [0]*(v+1)
#인접리스트 초기화
graph = [[] for i in range(v+1)]

#간선을 입력받아 넣으며, b의 입력간선수를 증가한다
for i in range(e) :
  a, b = map(int, input().split())
  graph[a].append(b)
  indegree[b] += 1

#위상정렬함수
def topology_sort() :
  result = []
  q = deque()

  #입력간선수가 0인 시작점을 큐에 넣는다
  for i in range(1, v+1) :
    if indegree[i] == 0 :
      q.append(i)
  
  #큐기 빌동안 하나씩 빼며 반복
  while q :
    now = q.popleft()
    result.append(now)
    #인접 간선을 없앤다
    for i in graph[now] :
      indegree[i] -= 1
      
      #만약 간선수가 0이면 큐에 넣는다
      if indegree[i] == 0 :
        q.append(i)
  
  for i in result :
    print(i, end = " ")

topology_sort()