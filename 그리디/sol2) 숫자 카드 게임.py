#실전2) 숫자 카드 게임, 96p

#도전
N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
max = 0
for i in range(N) :
  temp = data[i]
  temp.sort()
  if temp[0]>max :
    max = temp[0]
print(max)

#풀이방법
N, M = map(int, input().split())
result = 0
#한줄 리스트를 입력받아 그중 min값을 찾아 result에 저장한다
for i in range(N) :
  data = list(map(int, input().split()))
  temp = min(data)
  result = max(result, temp)
print(result)