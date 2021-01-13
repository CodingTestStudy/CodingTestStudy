#do1) 모험가 길드, 311p
#그리디 유형

#1차 : 접근 실패
#정렬 후 작은수부터 개수를 증가시키며 현재 비교수보다 크거나 같아지는 순간 한 그룹으로 묶는 원리이다.

N = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for i in data :
  count += 1
  if count >= i :
    result += 1
    count = 0

print(result)