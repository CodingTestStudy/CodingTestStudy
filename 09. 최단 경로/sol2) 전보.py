#sol2) 전보, 262p
#C -> 연결노드 개수, 총 시간
import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

N, M, C = map(int, input().split())

graph = [[] for i in range(N+1)]
distance = [INF] * (N+1)

#간선 입력
for _ in range(M) :
  x, y, z = map(int, input().split())
  graph[x].append((y, z))

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

dijkstra(C)
sum = 0
time = 0
for i in range(1, N+1) :
  if i == C :
    continue
  if distance[i] != INF :
    sum += 1
    if distance[i] > time :
      time = distance[i]

print(sum, time)