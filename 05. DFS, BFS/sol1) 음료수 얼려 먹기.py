#sol1) 음료수 얼려 먹기, 149p

#재도전 (dfs 사용숙지후)
graph = []
def dfs(x,y) :
  if x<0 or x>N-1 or y<0 or y>M-1 : #범위를 벗어나는 경우
    return False
  else :
    if graph[x][y] == 0 :
      graph[x][y] = 1 #빈칸의 경우 방문으로 변경한다
      dfs(x-1,y)
      dfs(x+1,y)
      dfs(x,y+1)
      dfs(x,y-1) #사방을 재귀로 확인한다
      return True #최종적으로 주위의 반환이 모두 끝난경우(False) 최종으로 반환한다
    else :
      return False

N, M = map(int, input().split())
for i in range(1,N+1) :
  temp = list(map(int, input()))
  graph.append(temp)

result = 0
for i in range(N) :
  for j in range(M) :
    if dfs(i,j) == True : #0이 있는경우 1로 변경을 거친 후 얼음개수를 증가한다
      result += 1

print(result)

#풀이방법

n, m = map(int, input().split())
graph = []

for i in range(n) :
  graph.append(list(map(int, input())))

def dfs(x, y) :
  if x<=-1 or x>= n or y<=-1 or y>=m :
    return False
  
  if graph[x][y] == 0 :
    graph[x][y] = 1
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x+1,y)
    dfs(x,y+1)
    return True
  return False

result = 0
  
for i in range(n) :
    for j in range(m) :
      if dfs(i, j) == True :
        result += 1

print(result)