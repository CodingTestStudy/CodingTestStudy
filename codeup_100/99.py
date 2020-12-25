#99
matrix = [list(map(int, input().split())) for _ in range(10)]
x = 1
y = 1
start = True
#만약 오른쪽 칸이 움직일 수 있는경우 또는 아래로 움직일 수 있는 경우
if matrix[1][1] == 2 :
  start = False
matrix[1][1] = 9
while start :
  if matrix[x][y] == 2 :
    matrix[x][y] = 9
    break
  elif matrix[x][y+1] == 0 or matrix[x][y+1] == 2 :
    matrix[x][y] = 9
    y = y+1
    continue
  elif matrix[x+1][y] == 0 or matrix[x+1][y] == 2 :
    matrix[x][y] = 9
    x = x+1
    continue
  else :
    matrix[x][y] = 9
    break
for i in matrix :
  for j in i :
    print(j, end=" ")
  print()