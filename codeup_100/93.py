#93
temp = int(input())
a = list(map(int, input().split()))
result = [0 for i in range(23)]
for i in a :
  result[i-1] = result[i-1]+1

for i in result :
  print(i, end=" ")