#96
temp = int(input())
result = [[0 for i in range(19)] for j in range(19)]
for i in range(temp) :
  x, y = map(int, input().split())
  result[x-1][y-1] = 1
for i in result :
  for j in i :
    print(j, end=" ")
  print()