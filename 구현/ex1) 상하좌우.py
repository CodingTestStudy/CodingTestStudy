#ex1) 상하좌우, 110p

#도전
N = int(input())
x = 1
y = 1

control = list(map(str, input().split()))

for i in control :
  if i == 'L' and x>1 :
    x -= 1
  elif i == 'R' and x<N :
    x += 1
  elif i == 'U' and y>1 :
    y -= 1
  elif i == 'D' and y<N :
    y += 1
print(y, x)

#풀이방법
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans :
  for i in range(len(move_types)) :
    if plan == move_types[i] :
      nx = x + dx[i]
      ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n :
      continue
    x, y = nx, ny

print(x, y)

#1. 왜 2중for를 사용했을까
#2. 해당케이스를 for로 일일이 확인해야 하는가?
#-> 일종의 모든케이스를 대비할 수 있는 구조!