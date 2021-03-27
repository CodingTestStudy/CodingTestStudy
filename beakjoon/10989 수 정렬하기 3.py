
#10989 수 정렬하기 3
import sys
input = sys.stdin.readline

array = [0]*10001
n = int(input())
for _ in range(1, n+1):
  array[int(input())] += 1

for i in range(1, 10001):
  if array[i] != 0:
    for _ in range(array[i]) :
      print(i)