#sol1) 위에서 아래로, 178p

N = int(input())
array = []
for i in range(N) :
  array.append(int(input()))

array.sort(reverse=True)
for i in array :
  print(i, end=" ")