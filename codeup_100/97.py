#97
def flip(temp) :
  if temp == 1 :
    return 0
  else :
    return 1

result = [list(map(int, input().split())) for _ in range(19)]
s = int(input())
for i in range(s) :
  x, y = map(int, input().split())
  flip(result[x-1][y-1])
  for k in range(19) :
    result[k][y-1] = flip(result[k][y-1])
    result[x-1][k] = flip(result[x-1][k])

for i in result :
  for j in i :
    print(j, end=" ")
  print()