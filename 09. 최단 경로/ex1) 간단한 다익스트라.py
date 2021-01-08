#ex1) 간단한 다익스트라, 237p

import sys
INF = int(1e9)
input = sys.stdin.readline

#노드수, 간선수
N, M = map(int, input().split())
start = int(input())
graph = [[] for i in range(N+1)]
visited = [False]*(N+1)
distance = [INF]*(N+1)

for i in range(M) :
  #a->b 간선의 비용 : c
  a,b,c = map(int, input().split())
  graph[a].append((b,c))

#방문하지 않은 노드 중 최소값 노드의 인덱스를 반환
def get_smallest_node() :
  min_value = INF
  index = 0

  for i in range(1, N+1) :
    if distance[i] < min_value and not visited[i] :
      min_value = distance[i]
      index = i
  
  return index

def dijkstra(start) :
  #시작 조건 설정
  distance[start] = 0
  visited[start] = True
  
  #시작점 인근노드의 distance를 수정
  for j in graph[start] :
    distance[j[0]] = j[1] #j[0] : 노드값, j[1] : 간선값
  
  #N-1번 반복하며 distance를 갱신
  for i in range(N-1) :
    #방문안한 최소노드의 값을 찾아 방문표시한다
    now = get_smallest_node()
    visited[now] = True

    #인접한 노드들의 현재값 + 간선값을 비교하며 갱신한다
    for j in graph[now] :
      cost = distance[now] + j[1]
      
      #현재값보다 갱신값이 작은경우 갱신한다
      if cost < distance[j[0]] :
        distance[j[0]] = cost

dijkstra(start)

for i in range(1, N+1) :
  if distance[i] == INF :
    print("INFINITY")
  else :
    print(distance[i])