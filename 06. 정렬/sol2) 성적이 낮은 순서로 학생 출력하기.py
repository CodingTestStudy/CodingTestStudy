#sol2) 성적이 낮은 순서로 학생 출력하기

N = int(input())
array = []
for i in range(N) :
  name, score = map(str, input().split())
  array.append((name, int(score)))

array = sorted(array, key = lambda data: data[1])

for i in array :
  print(i[0], end=" ")