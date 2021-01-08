#98
h, w = map(int, input().split())
result = [[0 for i in range(w)] for j in range(h)]
n = int(input())
for _ in range(n) :
  l, d, x, y = map(int, input().split())
  x = x-1
  y = y-1
  for i in range(l) :
    if d==0 :
      result[x][y+i] = 1
    else :
      result[x+i][y] = 1

for i in result:
  for j in i:
    print(j, end=" ")
  print()