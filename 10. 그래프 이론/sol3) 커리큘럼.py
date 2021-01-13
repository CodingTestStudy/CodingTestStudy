#sol3) 커리큘럼, 303p
from collections import deque

N = int(input())
graph = [[] for i in range(N+1)]
indeg = [0]*(N+1)
#간선과 별개로 시간을 저장하는 테이블이 필요
time = [0]*(N+1)

for i in range(1, N+1) :
  data = list(map(int, input().split()))
  #시간값 저장
  time[i] = data[0]
  #인덱스 1 ~ 인덱스 끝-1까지 선수강 데이터를 통해
  #인접리스트에 추가, 간선수를 증가시킨다
  for x in data[1:-1] :
    graph[x].append(i)
    indeg[i] += 1

#위상정렬함수
def topology_sort() :
  #time값을 그대로 복제하여 result로 저장한다
  result = time[:]
  q = deque()

  for i in range(1, N+1) :
    if indeg[i] == 0 :
      q.append(i)
  
  while q :
    now = q.popleft()
    #인접리스트
    for i in graph[now] :
      indeg[i] -= 1
      #선수강시간 + 수강시간 값으로 갱산한다
      result[i] = max(result[i], result[now] + time[i])
      #큐에 추가
      if indeg[i] == 0 :
        q.append(i)

  for i in range(1, N+1) :
    print(result[i], end=" ")

topology_sort()