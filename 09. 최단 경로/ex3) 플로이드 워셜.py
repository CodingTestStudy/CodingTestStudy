#ex3) 플로이드 워셜, 257p

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