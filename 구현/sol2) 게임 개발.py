#sol2) 게임 개발, 118p

#도전
def left_rotation(direction) :
  return (direction+1)%4

move = [(0,-1), (-1,0), (0,1), (1,0)]
column, row = map(int, input().split())
x, y, direction = map(int, input().split())
map = [map(int, input().split()) for i in range(column)]

count_rotation = 0
result = 0


while True :
  dx, dy = move[direction]
  


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