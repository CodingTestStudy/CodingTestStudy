#sol2) 게임 개발, 118p

#재시도
N, M = map(int, input().split())
x, y, direction = map(int, input().split()) #시작위치, 방향 입력
map = [list(map(int, input().split())) for i in range(N)] #맵 저장

map_status = [[0 for i in range(M)] for j in range(N)] #플레이어 이동상태 기록
move = [(-1,0), (0,1), (1,0), (0,-1)] #방향에 따른 이동위치

def rotation() : #왼쪽회전 함수
  global direction
  direction -= 1
  if direction == -1 :
    direction = 3

result = 1 #이동회수
turn_count = 0 #회전회수

while True : #본게임
  map_status[x][y] = 1
  rotation() #왼쪽 회전
  turn_count += 1 #회전수 증가
  if turn_count == 4 : #만약 4방향 다 확인한 경우
    next_x = x-move[direction][0]
    next_y = y-move[direction][1]
    if map[next_x][next_y] == 0 : #뒤로 이동 가능한 경우
      x = next_x
      y = next_y
      turn_count = 0
      continue
    else : #게임 종료
      break
  else : #회전 후 확인작업
    next_x = x+move[direction][0]
    next_y = y+move[direction][1]
    if map[next_x][next_y] == 0 and map_status[next_x][next_y] == 0 : #육지이며 안가본 경우 움직인다
      result += 1
      x = next_x
      y = next_y
      turn_count = 0
      continue
    else : #못갈경우 다음회전 실행
      continue

print(result)
  

#풀이방법
n, m = map(int, input().split())
d = [[0]*m for _ in range(n)]

x, y, direction = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n) :
  array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
  global direction
  direction -= 1
  if direction == -1 :
    direction = 3

count = 1
turn_time = 0
while True :
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]

  if d[nx][ny] == 0 and array[nx][ny] == 0 :
    d[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue
  else :
    turn_time += 1
  if turn_time == 4 :
    nx = x - dx[direction]
    ny = y - dy[direction]

    if array[nx][ny] == 0 :
      x = nx
      y = ny
    else :
      break
    turn_time = 0

print(count)