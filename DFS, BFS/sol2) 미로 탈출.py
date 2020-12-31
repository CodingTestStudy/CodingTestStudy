#sol2) 미로 탈출, 152p

#재도전 (bfs 사용숙지후)
from collections import deque
graph = [] #게임저장
move = [(-1,0), (1,0), (0,-1), (0,1)] #이동을 위한 리스트

N, M = map(int, input().split())
for i in range(N) :
  graph.append(list(map(int, input())))

def bfs() :
  queue = deque()
  queue.append((0,0)) #시작점 추가

  while queue :
    x, y = queue.popleft() #하나씩 제거
    for i in range(4) :
      next_x = x+move[i][0]
      next_y = y+move[i][1]

      if next_x<0 or next_x>N-1 or next_y<0 or next_y>M-1 :
        continue #위치를 벗어나는 경우(outofrange) : 다음 queue 제거
      if graph[next_x][next_y] == 0 :
        continue #장애물의 경우 : 다음 queue 제거
      if graph[next_x][next_y] == 1 :
        graph[next_x][next_y] = graph[x][y]+1
        queue.append((next_x, next_y))
        continue #길의 경우 : 현재위치의 숫자+1로 변경 후 queue에 넣는다.

bfs()
print(graph[N-1][M-1]) #최종적으로 적힌 숫자를 반환한다